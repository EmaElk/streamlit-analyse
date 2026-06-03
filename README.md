# Streamlit Aufgaben

Dieses Repository enthält die Streamlit-Aufgaben aus dem Unterricht.

## Übersicht

| Aufgabe    | Datei                                       | Beschreibung                                                                  |
| ---------- | ------------------------------------------- | ----------------------------------------------------------------------------- |
| Aufgabe 1  | `aufgabe1.py`                               | Erste Streamlit-App mit Titel, Widgets, bedingter Ausgabe und Rerun-Kommentar |
| Aufgabe 2  | `aufgabe2.py`                               | Zähler-App mit `st.session_state` und Reset-Button                            |
| Aufgabe 3  | `aufgabe3.py` + `abc_analyse_aus_excel.csv` | Mini-Dashboard mit CSV-Datei, Cache, Filter, Metriken, Tabelle und Diagramm   |
| Aufgabe 4  | `aufgabe4.py`                               | Kurze Reflexion zu Streamlit, Django und FastAPI                              |
| Deployment | PythonAnywhere-Test                         | Deployment wurde getestet, ist aber mit dem Free Account fehlgeschlagen       |

---

## Aufgabe 1 — Erste App & Rerun-Verständnis

In `aufgabe1.py` wurde eine einfache Streamlit-App erstellt.

Die App enthält:

* einen Titel mit `st.title()`
* ein Texteingabefeld mit `st.text_input()`
* einen Slider mit `st.slider()`
* eine bedingte Ausgabe mit `if`/`else`
* einen Kommentar zum Rerun-Prinzip

### Starten

```bash
streamlit run aufgabe1.py
```

---

## Aufgabe 2 — Session State: Zähler-App

In `aufgabe2.py` wurde eine Zähler-App umgesetzt.

Zuerst ist im Code der falsche Ansatz als Kommentar sichtbar. Dieser Ansatz funktioniert nicht richtig, weil normale Variablen bei Streamlit nach einem Rerun wieder neu gesetzt werden.

Danach wurde der richtige Ansatz mit `st.session_state` umgesetzt.

Die App enthält:

* einen auskommentierten falschen Ansatz ohne `st.session_state`
* einen funktionierenden Klick-Zähler mit `st.session_state`
* einen Reset-Button, der den Zähler wieder auf 0 setzt

### Starten

```bash
streamlit run aufgabe2.py
```

---

## Aufgabe 3 — Mini-Dashboard mit Layout & Caching

In `aufgabe3.py` wurde ein kleines Dashboard zur ABC-Analyse erstellt.

Als Datengrundlage wird die CSV-Datei `abc_analyse_aus_excel.csv` verwendet.
Die Daten stammen aus der zuvor manuell erstellten Excel-Auswertung.

Die App enthält:

* Laden der CSV-Datei mit `pandas`
* Caching mit `@st.cache_data`
* Kennzahlen mit `st.metric()`
* Spaltenlayout mit `st.columns()`
* interaktiven Filter mit `st.selectbox()`
* Anzeige der gefilterten Daten mit `st.dataframe()`
* Balkendiagramm mit `st.bar_chart()`

### Starten

```bash
streamlit run aufgabe3.py
```

---

## Aufgabe 4 — Reflexion

Die Reflexion befindet sich in der Datei `aufgabe4.py`.

Darin wird kurz erklärt, wann Streamlit sinnvoll ist und wann man eher Django oder FastAPI verwenden würde.

---

## Verwendete Dateien

Der Ordner enthält folgende Dateien:

```text
Streamlit/
├── README.md
├── abc_analyse_aus_excel.csv
├── aufgabe1.py
├── aufgabe2.py
├── aufgabe3.py
├── aufgabe4.py
└── requirements.txt
```

---

## Benötigte Pakete

Die benötigten Python-Pakete stehen in der Datei `requirements.txt`.

```text
streamlit
pandas
```

Installation:

```bash
pip install -r requirements.txt
```

---

## Deployment

Das Deployment der Streamlit-App wurde mit PythonAnywhere getestet.

Beim Installieren der benötigten Pakete aus `requirements.txt` ist folgender Fehler aufgetreten:

```text
ERROR: Could not install packages due to an OSError: [Errno 122] Disk quota exceeded
```

Dadurch konnte Streamlit im PythonAnywhere-Free-Account nicht vollständig installiert werden.

Aus diesem Grund erfolgt die Abgabe über das Bitbucket-Repository.

---

## Repository

Die vollständigen Projektdateien befinden sich im Bitbucket-Repository.

URL: bitte hier den Bitbucket-Link einfügen
