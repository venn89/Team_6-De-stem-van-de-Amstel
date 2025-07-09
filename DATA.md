# Data 
Dit bestand beschrijft de data die beschikbaar word gesteld in de hackathon.

## Beschrijving

De data bevat metingen van oppervlaktewaterkwaliteit, van het eerste data punt in 1963 tot 2025. De bestanden staan op sharepoint en worden met je gedeeld op de dag van de hackathon. Oppervlakte kwaliteit word gemeten aan de hand van hydrobiologische en chemische toetsing. In de file 'FYCHEM_alleParamtrs_alleJaren_Amstelland_1900tmjuni.csv' staan de ruwe meetgegevens voor de fysisch chemische toetsing. In de file 'HB_alleKwalelementen_alleJaren_Amstelland.csv' staan de ruwe meetgegevens voor hydrobiologische toetsing. Vanaf 2006 zijn de meetwaardes via een bepaalde standaard gemeten, in de jaren hiervoor is dit niet het geval. In [oppervlaktewater kwaliteit analyse notebook](./notebooks/oppervlaktewater_kwaliteit_analyse.ipynb) staat wat meer informatie over de data, hoe je dit inleest, eruit ziet, welke kolommen relevant zijn, en dit kunt visualiseren.

## Mappenstructuur

data/
├─ factsheets/
│ ├─ 2013_factsheet_NL11_1_1.pdf
│ ├─ 2014_factsheet_NL11_1_1.pdf
│ ├─ 2015_factsheet_NL11_1_1.pdf
│ ├─ 2016_factsheet_NL11_1_1.pdf
│ ├─ 2017_factsheet_NL11_1_1.pdf
│ ├─ 2018_factsheet_NL11_1_1.pdf
│ ├─ 2019_factsheet_NL11_1_1.pdf
│ ├─ 2020_factsheet_NL11_1_1.pdf
│ ├─ 2021_factsheet_NL11_1_1.pdf
│ ├─ 2022_factsheet_NL11_1_1.pdf
│ ├─ 2023_factsheet_NL11_1_1.pdf
│ ├─ 2024_factsheet_NL11_1_1.pdf
│ ├─ factsheet_Amstel.png
├─ shapefiles/
│ ├─ amstelland.zip
│ ├─ Beheerregister_EAG_20241218.zip
│ ├─ Beheerregister_Water_20241218.zip
├─ uitvoer aquo-kit/
│ ├─ Toetsresultaat_fytoplankton.csv
│ ├─ Toetsresultaat_macrofauna.csv
│ ├─ Toetsresultaat_macrofyten.csv
│ ├─ Toetsresultaat_vissen.csv
├─ waternet FEWS data/
│ ├─ FYCHEM_alleParamtrs_alleJaren_Amstelland_1900tmjuni.csv
│ ├─ HB_alleKwalelementen_alleJaren_Amstelland.csv
│ ├─ Parameter_uitleg.xlsx
├─ watersysteemkaarten/
│ ├─ WSK_{code}.pdf
│ ├─ Codes Afvoergebieden.xlsx
├─ Lijst van scorende soorten - M-typen_202507071242.csv
├─ Normen_stoffen_zoetwater.xlsx
├─ STOWA_2018-49-Maatlatten v2024 DEF.pdf

### factsheets/

| Bestand | Beschrijving | Opmerkingen |
|---------|---------------|--------------|
| `{jaar}_factsheet_NL11_1_1.csv` | Factsheets oppervlaktewaterkwaliteit van Het Waterschapshuis | Beoordeling en maatregelen per jaar in factsheets |
| `factsheet_Amstel.png` | Factsheet 2025 door waternet | |

### shapefiles/

| Bestand | Beschrijving | Opmerkingen |
|---------|---------------|--------------|
| `Beheerregister_EAG_20241218.zip` | Shapefile ecologisch analyse gebied |  |
| `Beheerregister_Water_20241218.zip` | Shapefile Afaanvoergebieden | |

### uitvoer aquo-kit/

| Bestand | Beschrijving | Opmerkingen |
|---------|---------------|--------------|
| `Toetsresultaat_fytoplankton.csv` | Aquo-kit resultaten voor fytoplankton |  |
| `Toetsresultaat_macrofauna.csv` | Aquo-kit resultaten voor macrofauna | |
| `Toetsresultaat_macrofyten.csv` | Aquo-kit resultaten voor macrofyten | |
| `Toetsresultaat_vissen.csv` | Aquo-kit resultaten voor vissen | |

### waternet FEWS data/

| Naam | Beschrijving | Opmerkingen |
|------|---------------|--------------|
| `FYCHEM_alleParamtrs_alleJaren_Amstelland_1900tmjuni.csv` | Fysische Chemische data voor alle jaren | Meetwaardes |
| `HB_alleKwalelementen_alleJaren_Amstelland.csv` | Hydrobiologische data voor alle jaren | Meetwaardes |
| `Parameter_uitleg.xlsx` | Uitleg parameter meetwaardes | |

### watersysteemkaarten/ 

| Naam | Beschrijving | Opmerkingen |
|------|---------------|--------------|
| `WSK_{code}.pdf` | In een watersysteemkaart zijn per af aanvoergebied de kunstwerken (gemalen, stuwen, schotten, inlaten, duikers, dammen, enz ) de watergangen en de peilgebieden met peilen te vinden | Ter informatie |
| `Codes Afvoergebieden.xlsx` | Codes en namen van afvoergebieden in de watersysteemkaarten |  |

### Losse bestanden
| Naam | Beschrijving | Opmerkingen |
|------|---------------|--------------|
| `normen_stoffen_zoetwater.csv` | Bevat normen van het RIVM per stof voor zoetwater | Chemische toetsing |
| `STOWA_2018-49-Maatlatten v2024 DEF.pdf` | Maatlatten STOWA kader richtlijn water| Uitleg hoe de berekening oppervlaktewater kwaliteit word gedaan en wat de eisen zijn |
| `lijst van scorende soorten - M-typen_202507071242` | Lijst van stoffen gewenste en ongewenste soortent | 1-3 gewenst, 4-5 ongewenst, Amstellandboezem = M6b |

## Gebruik

- Data is ruwe export uit het systeem.
- Bevat geen persoonsgegevens.
- Publiekelijke data
