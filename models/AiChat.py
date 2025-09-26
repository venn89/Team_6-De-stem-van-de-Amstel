from __future__ import annotations

import json
import os
from typing import Optional, Dict, Any

import pandas as pd
from openai import OpenAI

# ─────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────
API_KEY = os.getenv("OPENAI_API_KEY").strip()
if not API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY environment variable.")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5")  # e.g. "gpt-4.1-mini" if needed
client = OpenAI(api_key=API_KEY)

# ─────────────────────────────────────────────────────────────
# Mock Water Quality Data (Amsterdam swimming spots – sample)
# You can replace/extend this with your real columns later.
# ─────────────────────────────────────────────────────────────
def load_mock_data() -> pd.DataFrame:
    data = [
        # date, location, e_coli_cfu, cyanobacteria_risk, temperature_c,
        # oxygen_mg_l, nutrients_mg_l, clarity_cm, ph, status, advisory

        # Sloterplas
        ("2025-06-29", "Sloterplas", 180, "Low", 21.3, 8.1, 0.35, 120, 7.6, "Good", "Safe to swim."),
        ("2025-07-15", "Sloterplas", 420, "Medium", 23.0, 6.9, 0.55, 80, 7.2, "Caution", "Monitor algae risk."),
        ("2025-08-05", "Sloterplas", 720, "High", 24.1, 5.8, 0.70, 60, 7.0, "Poor", "Avoid swimming – bloom and bacteria."),

        # Nieuwe Meer
        ("2025-07-02", "Nieuwe Meer", 220, "Low", 22.5, 8.3, 0.28, 130, 7.6, "Good", "Safe to swim."),
        ("2025-07-20", "Nieuwe Meer", 390, "Medium", 23.8, 7.2, 0.44, 95, 7.3, "Caution", "E. coli slightly high."),
        ("2025-08-12", "Nieuwe Meer", 510, "High", 25.0, 6.4, 0.62, 75, 7.1, "Poor", "Avoid – cyanobacteria detected."),

        # IJmeer / Blijburg
        ("2025-07-14", "IJmeer (Blijburg)", 95, "Low", 20.2, 9.0, 0.29, 140, 7.7, "Good", "Safe to swim."),
        ("2025-07-28", "IJmeer (Blijburg)", 300, "Medium", 22.1, 7.8, 0.47, 100, 7.4, "Caution", "Monitor water clarity."),
        ("2025-08-15", "IJmeer (Blijburg)", 620, "High", 24.3, 6.2, 0.69, 70, 7.2, "Poor", "Do not swim – algal bloom."),

        # Ouderkerkerplas
        ("2025-07-10", "Ouderkerkerplas", 140, "Low", 21.8, 8.7, 0.31, 125, 7.5, "Good", "Safe to swim."),
        ("2025-08-01", "Ouderkerkerplas", 460, "Medium", 23.9, 6.9, 0.59, 85, 7.2, "Poor", "Advisory posted."),
        ("2025-08-23", "Ouderkerkerplas", 280, "Low", 22.7, 8.1, 0.40, 115, 7.5, "Good", "Improved conditions."),

        # Amstel bij Omval
        ("2025-07-05", "Amstel (Omval)", 200, "Low", 21.2, 8.4, 0.33, 130, 7.6, "Good", "Safe for recreation."),
        ("2025-07-25", "Amstel (Omval)", 370, "Medium", 22.7, 7.3, 0.49, 95, 7.3, "Caution", "Monitor E. coli."),
        ("2025-08-18", "Amstel (Omval)", 480, "High", 23.5, 6.6, 0.65, 70, 7.1, "Poor", "Avoid – algal risk."),

        # Vinkeveense Plassen
        ("2025-06-30", "Vinkeveense Plassen", 120, "Low", 20.8, 9.1, 0.27, 150, 7.8, "Good", "Safe to swim."),
        ("2025-07-22", "Vinkeveense Plassen", 210, "Low", 22.9, 8.6, 0.32, 140, 7.6, "Good", "No issues."),
        ("2025-08-10", "Vinkeveense Plassen", 340, "Medium", 23.6, 7.5, 0.45, 105, 7.4, "Caution", "Monitor algae."),
    ]
    df = pd.DataFrame(
        data,
        columns = [
            "date",
            "location",
            "e_coli_cfu",
            "cyanobacteria_risk",
            "temperature_c",
            "oxygen_mg_l",
            "nutrients_mg_l",
            "clarity_cm",
            "ph",
            "status",
            "advisory",
        ],
    )
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

# ─────────────────────────────────────────────────────────────
# Optional manual filter (you can call it directly)
# ─────────────────────────────────────────────────────────────
def filter_rows(
        df: pd.DataFrame,
        location: Optional[str] = None,
        year: Optional[int] = None,
) -> pd.DataFrame:
    out = df.copy()
    if location:
        out = out[out["location"].str.contains(location, case=False, na=False)]
    if year is not None and "date" in out.columns:
        out = out[out["date"].dt.year == int(year)]
    return out.sort_values("date", ascending=False)

# ─────────────────────────────────────────────────────────────
# Ask the LLM to infer filters (location, year) from free text
# ─────────────────────────────────────────────────────────────
def llm_suggest_filters(question: str, df_columns: list[str]) -> Dict[str, Any]:
    want_location = "location" in df_columns
    want_year = "date" in df_columns

    system = (
        "Extract filters from the user's question about Amsterdam water quality.\n"
        "Only output a single JSON object with keys: location, year.\n"
        "Use null if unknown. Year must be an integer like 2025 or null."
    )
    msg_user = (
        f"Question:\n{question}\n\n"
        "Return JSON ONLY (no extra text). Example:\n"
        '{"location":"Sloterplas","year":2025}'
    )

    resp = client.chat.completions.create(
        model=MODEL,
        temperature=1,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": msg_user},
        ],
    )
    text = resp.choices[0].message.content.strip()
    try:
        data = json.loads(text)
    except Exception:
        data = {"location": None, "year": None}

    out = {
        "location": (data.get("location") if isinstance(data.get("location"), str) and data.get("location").strip() else None),
        "year": (int(data.get("year")) if str(data.get("year", "")).isdigit() else None),
    }
    if not want_location:
        out["location"] = None
    if not want_year:
        out["year"] = None
    return out

# ─────────────────────────────────────────────────────────────
# Build a compact, row-grounded prompt
# ─────────────────────────────────────────────────────────────
def build_prompt(user_question: str, rows: pd.DataFrame, max_rows: int = 20) -> str:
    # Keep it small; include only fields we care about
    cols = ["date", "location", "e_coli_cfu", "cyanobacteria_risk", "temperature_c", "status", "advisory"]
    cols = [c for c in cols if c in rows.columns]
    snippet = rows[cols].head(max_rows).to_csv(index=False)
    instructions = (
        "You are a helpful assistant for Amsterdam swimming water quality.\n"
        "Use ONLY the rows below to answer. If the answer is not in the rows, say you don't know.\n\n"
        "ROWS (CSV):\n"
    )
    return f"{instructions}{snippet}\nQUESTION: {user_question}"

# ─────────────────────────────────────────────────────────────
# Ask model for the final answer
# ─────────────────────────────────────────────────────────────
def ask_llm(prompt: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=1,
        messages=[
            {"role": "system", "content": "Be concise, factual, and cite specific dates/locations from the rows when possible."},
            {"role": "user", "content": prompt},
        ],
    )
    return resp.choices[0].message.content.strip()

# ─────────────────────────────────────────────────────────────
# High-level: answer a question with LLM-derived filters
# ─────────────────────────────────────────────────────────────
def answer_question(question: str, df: pd.DataFrame, max_rows: int = 20) -> str:
    inferred = llm_suggest_filters(question, df.columns.tolist())
    # Try inferred filters first; if empty, give the model more to look at
    df_inferred = filter_rows(df, location=inferred["location"], year=inferred["year"])
    rows = df_inferred if not df_inferred.empty else df.sort_values("date", ascending=False)
    prompt = build_prompt(question, rows, max_rows=max_rows)
    return ask_llm(prompt)

# ─────────────────────────────────────────────────────────────
# CLI Loop
# ─────────────────────────────────────────────────────────────
def main():
    df = load_mock_data()
    print("Water Quality AI Bot (mock data)\nType your question, or 'exit' to quit.")
    print("Examples:")
    print(" - Compare the swimming status and advisories between Vinkeveense Plassen and Sloterplas in July 2025.")
    print(" - Which location had the poorest swimming status or strictest advisory in August 2025?")
    print(" - What is the latest swimming advisory for Nieuwe Meer, and what were the recent cyanobacteria (algae) risk levels?\n")

    while True:
        try:
            q = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not q:
            continue
        if q.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        try:
            ans = answer_question(q, df, max_rows=20)
            print("\n" + ans + "\n")
        except Exception as e:
            print(f"[Error] {e}\n")

if __name__ == "__main__":
    main()

