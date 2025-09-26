import './App.css'

function App() {
  return (
    <div style={{
      width: "100vw",
      minHeight: "100vh",
      background: "linear-gradient(to bottom, #3DD0F4, #2967A5)",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      color: "white",
    }}>
      {/* Welcome Heading */}
      <h1 className="daphne" style={{marginBottom: "5rem"}}>
        Welkom bij Daphne
      </h1>

      {/* Chat Info */}
      <p className="chat-info">
        Daphne is een chatbot die gebruikers informatie kan verstrekken over de huidige ecologische stand en waterkwaliteit in de amstelregio
      </p>

      {/* Start Button */}
      <button href="#Chat" style={{
        backgroundColor: "#2967A5",
        color: "white",
        border: "none",
        borderRadius: "5px",
        padding: "1rem 7rem",
        fontSize: "1.5rem",
        cursor: "pointer",
        marginTop: "3rem",
      }}>
        Probeer het nu!
      </button>
    </div>
  );
}


export default App
