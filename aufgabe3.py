import streamlit as st
import pandas as pd

st.set_page_config(page_title="ABC-Analyse Dashboard", layout="wide")

st.title("Aufgabe 3 - Mini-Dashboard mit Layout & Caching")

st.write(
    "Dieses Dashboard zeigt die ABC-Analyse aus der CSV-Datei. "
    "Die Daten werden geladen, gefiltert und als Tabelle sowie Diagramm dargestellt."
)

# Mit @st.cache_data werden die CSV-Daten zwischengespeichert.
# Dadurch muss die Datei nicht bei jeder Änderung neu geladen werden.
@st.cache_data
def lade_daten():
    daten = pd.read_csv("abc_analyse_aus_excel.csv", sep=";", decimal=",")
    return daten


df = lade_daten()

st.subheader("Gesamte Daten")

st.dataframe(df)

st.subheader("Filter nach ABC-Klasse")

abc_auswahl = st.selectbox(
    "Welche ABC-Klasse möchtest du anzeigen?",
    ["Alle", "A", "B", "C"]
)

if abc_auswahl == "Alle":
    gefilterte_daten = df
else:
    gefilterte_daten = df[df["ABC"] == abc_auswahl]

st.subheader("Kennzahlen")

gesamtumsatz = gefilterte_daten["Umsatz"].sum()
anzahl_kunden = len(gefilterte_daten)

if anzahl_kunden > 0:
    bester_kunde = gefilterte_daten.loc[gefilterte_daten["Umsatz"].idxmax(), "Kunde"]
    hoechster_umsatz = gefilterte_daten["Umsatz"].max()
else:
    bester_kunde = "-"
    hoechster_umsatz = 0

spalte1, spalte2 = st.columns(2)

with spalte1:
    st.metric("Gesamtumsatz", f"{gesamtumsatz:.2f} €")

with spalte2:
    st.metric("Anzahl Kunden", anzahl_kunden)

spalte3, spalte4 = st.columns(2)

with spalte3:
    st.metric("Bester Kunde", bester_kunde)

with spalte4:
    st.metric("Höchster Umsatz", f"{hoechster_umsatz:.2f} €")

st.subheader("Gefilterte Tabelle")

st.dataframe(gefilterte_daten)

st.subheader("Umsatz je Kunde")

if anzahl_kunden > 0:
    diagramm_daten = gefilterte_daten.set_index("Kunde")["Umsatz"]
    st.bar_chart(diagramm_daten)
else:
    st.warning("Für diese Auswahl gibt es keine Daten.")

st.subheader("Kurze Interpretation")

anzahl_a = len(df[df["ABC"] == "A"])
anzahl_b = len(df[df["ABC"] == "B"])
anzahl_c = len(df[df["ABC"] == "C"])

st.write(
    f"In der gesamten Analyse gibt es **{anzahl_a} A-Kunden**, "
    f"**{anzahl_b} B-Kunden** und **{anzahl_c} C-Kunden**."
)

st.info(
    "A-Kunden haben den größten Umsatzanteil und sind daher besonders wichtig. "
    "B-Kunden sind mittelwichtig. C-Kunden haben einen kleineren Umsatzanteil."
)