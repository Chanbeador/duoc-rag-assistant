import streamlit as st
from agent_engine import agent_answer

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================

st.set_page_config(
    page_title="Asistente Virtual DUOC UC",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.image("assets/logo_duoc.png", width=180)

    st.header("📚 Herramientas del Agente")

    st.success("Consulta Académica (RAG)")
    st.success("Redacción de Correos")
    st.success("Memoria Conversacional")

    st.divider()

    st.markdown("""
    ### Tecnologías

    - GPT-4o-mini
    - LangChain
    - FAISS
    - Streamlit
    - GitHub Models
    """)

    st.divider()

    if st.button("🗑️ Limpiar Conversación"):

        st.session_state.messages = []

        st.rerun()

# ==========================================
# ENCABEZADO PRINCIPAL
# ==========================================

st.image("assets/logo_duoc.png", width=250)

st.markdown("""
<div style='text-align: center; margin-bottom: 30px;'>

<h1 style='color:#003DA5;'>
🎓 Asistente Virtual DUOC UC Plaza Oeste
</h1>

<p style='font-size:18px; color:#555;'>
Consultas Académicas | Redacción de Correos | Memoria Conversacional
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "Consulta información institucional, redacta correos formales y utiliza memoria conversacional."
)

# ==========================================
# HISTORIAL DE CHAT
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# MENSAJE DE BIENVENIDA
# ==========================================

if len(st.session_state.messages) == 0:

    with st.chat_message("assistant"):

        st.markdown("""
¡Bienvenido al Asistente Virtual DUOC UC Plaza Oeste! 🎓

Puedo ayudarte con:

- Matrícula
- Becas y gratuidad
- Reglamentos académicos
- Procesos institucionales
- Redacción de correos formales
- Memoria conversacional

¿En qué puedo ayudarte hoy?
""")

# ==========================================
# MOSTRAR HISTORIAL
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ==========================================
# ENTRADA DE USUARIO
# ==========================================

prompt = st.chat_input(
    "Escribe tu consulta aquí..."
)

if prompt:

    # Mostrar mensaje usuario
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta
    with st.spinner("Pensando..."):

        respuesta = agent_answer(prompt)

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": respuesta
        }
    )