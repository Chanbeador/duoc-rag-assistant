import streamlit as st
import pandas as pd

from observability import calculate_metrics, load_logs


# Configuración página

st.set_page_config(
    page_title="Dashboard Observabilidad IA",
    page_icon="",
    layout="wide"
)


st.title(" Dashboard de Observabilidad - Asistente DUOC UC")


st.markdown(
    """
    Este dashboard permite monitorear el comportamiento
    del agente IA mediante métricas de ejecución,
    trazabilidad y rendimiento.
    """
)


# Obtener métricas

metrics = calculate_metrics()


# ==========================
# TARJETAS DE MÉTRICAS
# ==========================

col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Consultas realizadas",
        metrics["total_requests"]
    )


with col2:
    st.metric(
        "Latencia promedio",
        f'{metrics["average_latency"]} segundos'
    )


with col3:
    st.metric(
        "Tasa de éxito",
        f'{metrics["success_rate"]}%'
    )

with col4:
    st.metric(
        "Consistencia",
        f'{metrics["consistency_rate"]}%'
    )


with col5:
    st.metric(
        "Respuesta promedio",
        f'{metrics["average_response_length"]} caracteres'
    )

st.divider()


# ==========================
# USO DE HERRAMIENTAS
# ==========================

st.subheader("🛠 Uso de herramientas del agente")


tools = metrics["tools"]


if len(tools) > 0:

    tool_df = pd.DataFrame(
        {
            "Herramienta": tools.keys(),
            "Cantidad": tools.values()
        }
    )


    st.bar_chart(
        tool_df.set_index("Herramienta")
    )

else:

    st.warning(
        "No existen datos de herramientas."
    )


st.divider()


# ==========================
# LOGS
# ==========================

st.subheader("📋 Registros de ejecución")


logs = load_logs()


if len(logs) > 0:

    df_logs = pd.DataFrame(logs)

    st.dataframe(
        df_logs,
        use_container_width=True
    )

else:

    st.info(
        "No existen registros disponibles."
    )