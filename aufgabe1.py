import streamlit as st

st.title("Meine erste Streamlit-App")

# Streamlit führt das Skript jedes Mal neu aus,
# wenn sich ein Widget-Wert ändert oder ein Button geklickt wird.

name = st.text_input("Wie heißt du?")
alter = st.slider("Wie alt bist du?", 10, 100, 18)

st.write("Deine Eingaben:")
st.write("Name:", name)
st.write("Alter:", alter)

if name == "":
    st.warning("Bitte gib zuerst deinen Namen ein.")
else:
    st.success(f"Hallo {name}, schön dass du da bist!")

if alter >= 18:
    st.info("Du bist volljährig.")
else:
    st.info("Du bist noch nicht volljährig.")