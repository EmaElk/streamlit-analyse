# Streamlit Aufgaben

Dieses Repository enthält die Streamlit-Aufgaben aus dem Unterricht.

## Übersicht

| Aufgabe   | Datei                                       | Beschreibung                                                                  |
| --------- | ------------------------------------------- | ----------------------------------------------------------------------------- |
| Aufgabe 1 | `aufgabe1.py`                               | Erste Streamlit-App mit Titel, Widgets, bedingter Ausgabe und Rerun-Kommentar |
| Aufgabe 2 | `aufgabe2.py`                               | Zähler-App mit `st.session_state` und Reset-Button                            |
| Aufgabe 3 | `aufgabe3.py` + `abc_analyse_aus_excel.csv` | Mini-Dashboard mit CSV-Datei, Cache, Filter, Metriken und Tabelle             |
| Aufgabe 4 | `aufgabe4.py`                               | Kurze Reflexion zu Streamlit, Django und FastAPI                              |
| Bonus     | optional                                    | Deployment auf Streamlit Community Cloud                                      |

---

## Aufgabe 1 — Erste App & Rerun-Verständnis

In `aufgabe1.py` wurde eine einfache Streamlit-App erstellt.

Die App enthält:

* einen Titel mit `st.title()`
* ein Texteingabefeld mit `st.text_input()`
* einen Slider mit `st.slider()`
* eine bedingte Ausgabe mit `if`/`else`
* einen Kommentar, der erklärt, wann Streamlit das Skript neu ausführt

### Starten

```bash
streamlit run aufgabe1.py
```

---

## Aufgabe 2 — Session State: Zähler-App

In `aufgabe2.py` wurde eine Zähler-App erstellt.

Die App zeigt zuerst als Kommentar den falschen Ansatz mit einer normalen Variable. Dieser Ansatz funktioniert nicht richtig, weil Streamlit das Skript bei jeder Änderung neu ausführt.

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

Die App enthält:

* Laden der CSV-Datei mit `pandas`
* Caching mit `@st.cache_data`
* Kennzahlen mit `st.metric()`
* Spaltenlayout mit `st.columns()`
* interaktiven Filter mit `st.selectbox()`
* Anzeige der Daten mit `st.dataframe()`
* Balkendiagramm mit `st.bar_chart()`

### Starten

```bash
streamlit run aufgabe3.py
```

---

## Aufgabe 4 — Reflexion

Die Reflexion befindet sich in der Datei `aufgabe4.py`.

In der Reflexion wird kurz erklärt, wann Streamlit sinnvoll ist und wann man eher Django oder FastAPI verwenden würde.

---

## Verwendete Dateien

Der Ordner enthält folgende Dateien:

```text
Streamlit/
├── aufgabe1.py
├── aufgabe2.py
├── aufgabe3.py
├── aufgabe4.py
├── abc_analyse_aus_excel.csv
├── requirements.txt
└── README.md
```

---

## Benötigte Pakete

Die benötigten Python-Pakete stehen in der Datei `requirements.txt`.

```text
streamlit
pandas
```

---

## Installation und Ausführung

Zuerst müssen die benötigten Pakete installiert werden:

```bash
pip install -r requirements.txt
```

Danach kann eine App gestartet werden, zum Beispiel:

```bash
streamlit run aufgabe3.py
```

---

## Bonusaufgabe — Deployment

Die Bonusaufgabe ist optional.

Falls die App später auf Streamlit Community Cloud veröffentlicht wird, kann der Link hier ergänzt werden:

```text
Deployment-Link: noch nicht vorhanden
```
                                                     |
