import streamlit as st
import pandas as pd

st.set_page_config(page_title="Automatisierte ABC-Analyse", layout="wide")

st.title("Automatisierte ABC-Analyse in Streamlit")

st.write(
    "Diese App liest die Ausgangsdaten aus einer CSV-Datei ein und berechnet die ABC-Analyse automatisch. "
    "Bereits vorhandene berechnete Spalten aus der CSV werden nicht verwendet."
)

@st.cache_data
def lade_daten():
    daten = pd.read_csv("abc_analyse_aus_excel.csv", sep=";", decimal=",")
    return daten


df_original = lade_daten()

# Nur die echten Ausgangsdaten verwenden
ausgangsdaten = df_original[["Kunde", "Umsatz"]].copy()

st.subheader("Ausgangsdaten")

st.write(
    "Hier werden nur die ursprünglichen Daten angezeigt, also Kunde und Umsatz. "
    "Berechnete Spalten aus der CSV werden bewusst ignoriert."
)

st.dataframe(ausgangsdaten)

# Automatische ABC-Analyse
analyse = ausgangsdaten.copy()

analyse = analyse.sort_values(by="Umsatz", ascending=False).reset_index(drop=True)

gesamtumsatz = analyse["Umsatz"].sum()

analyse["Umsatzanteil in %"] = analyse["Umsatz"] / gesamtumsatz * 100
analyse["Kumuliert in %"] = analyse["Umsatzanteil in %"].cumsum()

def berechne_abc(kumuliert):
    if kumuliert <= 80:
        return "A"
    elif kumuliert <= 95:
        return "B"
    else:
        return "C"

analyse["ABC"] = analyse["Kumuliert in %"].apply(berechne_abc)

st.subheader("Automatisch berechnete ABC-Analyse")

st.write(
    "Hier berechnet Streamlit die Umsatzanteile, die kumulierten Werte und die ABC-Klassen automatisch."
)

st.dataframe(analyse)

st.subheader("Filter nach ABC-Klasse")

abc_auswahl = st.selectbox(
    "Welche ABC-Klasse möchtest du anzeigen?",
    ["Alle", "A", "B", "C"]
)

if abc_auswahl == "Alle":
    gefilterte_daten = analyse
else:
    gefilterte_daten = analyse[analyse["ABC"] == abc_auswahl]

st.subheader("Kennzahlen")

anzahl_kunden = len(gefilterte_daten)
umsatz_auswahl = gefilterte_daten["Umsatz"].sum()

if anzahl_kunden > 0:
    bester_kunde = gefilterte_daten.loc[gefilterte_daten["Umsatz"].idxmax(), "Kunde"]
    hoechster_umsatz = gefilterte_daten["Umsatz"].max()
else:
    bester_kunde = "-"
    hoechster_umsatz = 0

spalte1, spalte2, spalte3, spalte4 = st.columns(4)

with spalte1:
    st.metric("Gesamtumsatz", f"{gesamtumsatz:.2f} €")

with spalte2:
    st.metric("Umsatz Auswahl", f"{umsatz_auswahl:.2f} €")

with spalte3:
    st.metric("Anzahl Kunden", anzahl_kunden)

with spalte4:
    st.metric("Bester Kunde", bester_kunde)

st.subheader("Gefilterte Tabelle")

st.dataframe(gefilterte_daten)

st.subheader("Umsatz je Kunde")

if anzahl_kunden > 0:
    diagramm_daten = gefilterte_daten.set_index("Kunde")["Umsatz"]
    st.bar_chart(diagramm_daten)
else:
    st.warning("Für diese Auswahl gibt es keine Daten.")

st.subheader("Zusammenfassung nach ABC-Klassen")

abc_zusammenfassung = analyse.groupby("ABC").agg(
    Anzahl_Kunden=("Kunde", "count"),
    Umsatz=("Umsatz", "sum"),
    Durchschnittlicher_Umsatz=("Umsatz", "mean")
).reset_index()

abc_zusammenfassung["Umsatzanteil in %"] = (
    abc_zusammenfassung["Umsatz"] / gesamtumsatz * 100
)

st.dataframe(abc_zusammenfassung)

st.subheader("Interpretation")

anzahl_a = len(analyse[analyse["ABC"] == "A"])
anzahl_b = len(analyse[analyse["ABC"] == "B"])
anzahl_c = len(analyse[analyse["ABC"] == "C"])

st.info(
    f"Die ABC-Analyse wurde automatisch berechnet. "
    f"Es gibt {anzahl_a} A-Kunden, {anzahl_b} B-Kunden und {anzahl_c} C-Kunden. "
    "A-Kunden haben den größten Umsatzanteil und sind daher besonders wichtig. "
    "B-Kunden sind mittelwichtig. C-Kunden haben einen kleineren Umsatzanteil."
)