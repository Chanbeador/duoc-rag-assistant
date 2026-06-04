import streamlit as st
from agent_engine import agent_answer

st.set_page_config(
    page_title="Asistente DUOC UC",
    page_icon="🎓"
)

st.title("🎓 Asistente Virtual DUOC UC Plaza Oeste")

pregunta = st.text_input(
    "Ingrese su consulta académica"
)

if st.button("Consultar"):

    if pregunta:

        respuesta = agent_answer(pregunta)

        st.success(respuesta)