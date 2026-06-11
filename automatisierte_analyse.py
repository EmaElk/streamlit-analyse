import streamlit as st
import pandas as pd

st.set_page_config(page_title="Automatisierte ABC-Analyse", layout="wide")

st.title("Automatisierte ABC-Analyse in Streamlit")

st.write(
    "Diese App liest die ursprünglichen Bestelldaten ein. "
    "Eine Firma kann dabei mehrmals vorkommen, weil es mehrere Bestellungen oder Artikelpositionen geben kann. "
    "Danach werden die Umsätze automatisch pro Firma zusammengefasst und daraus wird die ABC-Analyse berechnet."
)


@st.cache_data
def lade_daten():
    daten = pd.read_csv("abc_rohdaten.csv", sep=";", decimal=",")
    return daten


df_original = lade_daten()

st.subheader("1. Ausgangsdaten")

st.write(
    "Hier sieht man die ursprünglichen Daten. "
    "Ein Unternehmen kann mehrmals vorkommen, weil jede Zeile eine einzelne Bestellposition darstellt."
)

st.dataframe(df_original)


st.subheader("2. Automatische Zusammenfassung pro Unternehmen")

# Nur die Spalten verwenden, die für die ABC-Analyse wichtig sind
ausgangsdaten = df_original[["Kname", "Umsatz"]].copy()

# Falls Umsatz als Text mit Komma eingelesen wird, wird er sicher in eine Zahl umgewandelt
ausgangsdaten["Umsatz"] = (
    ausgangsdaten["Umsatz"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Umsätze pro Unternehmen zusammenrechnen
kundenumsatz = (
    ausgangsdaten
    .groupby("Kname", as_index=False)["Umsatz"]
    .sum()
)

kundenumsatz = kundenumsatz.rename(columns={"Kname": "Kunde"})

st.write(
    "Hier wurden alle Umsätze eines Unternehmens automatisch addiert. "
    "Dadurch gibt es jedes Unternehmen nur noch einmal mit seinem Gesamtumsatz."
)

st.dataframe(kundenumsatz)


st.subheader("3. Automatisch berechnete ABC-Analyse")

analyse = kundenumsatz.copy()

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

st.write(
    "Jetzt berechnet Streamlit automatisch den Umsatzanteil, "
    "den kumulierten Umsatzanteil und die ABC-Klasse."
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


st.subheader("Umsatz je Unternehmen")

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
    f"Die ABC-Analyse wurde automatisch aus den Rohdaten berechnet. "
    f"Zuerst wurden alle Bestellpositionen pro Unternehmen zusammengefasst. "
    f"Danach wurden die Unternehmen nach Umsatz sortiert und in ABC-Klassen eingeteilt. "
    f"Es gibt {anzahl_a} A-Unternehmen, {anzahl_b} B-Unternehmen und {anzahl_c} C-Unternehmen."
)