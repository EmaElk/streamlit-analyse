import streamlit as st

st.title("Aufgabe 2 - Session State: Zähler-App")

st.write("Diese App zeigt den Unterschied zwischen einer normalen Variable und `st.session_state`.")

# ---------------------------------------------------------
# FALSCHER ANSATZ:
# Dieser Zähler funktioniert nicht richtig, weil Streamlit das Skript
# bei jedem Klick neu ausführt. Dadurch wird zaehler immer wieder auf 0 gesetzt.
#
# zaehler = 0
#
# if st.button("Falsch zählen"):
#     zaehler += 1
#
# st.write("Falscher Zähler:", zaehler)
# ---------------------------------------------------------

# RICHTIGER ANSATZ MIT SESSION STATE:
# st.session_state speichert den Wert auch nach einem Rerun der App.

if "zaehler" not in st.session_state:
    st.session_state.zaehler = 0

if st.button("Zähler erhöhen"):
    st.session_state.zaehler += 1

if st.button("Reset"):
    st.session_state.zaehler = 0

st.write("Aktueller Zählerstand:", st.session_state.zaehler)

if st.session_state.zaehler == 0:
    st.info("Der Zähler steht noch bei 0.")
else:
    st.success("Der Zähler wurde bereits erhöht.")