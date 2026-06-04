from dotenv import load_dotenv
import os
import json

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# Cargar variables de entorno
load_dotenv()

# Configuración de embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base=os.getenv("GITHUB_BASE_URL")
)

# Cargar índice FAISS ya creado
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Cargar memoria
try:
    with open("memory.json", "r", encoding="utf-8") as f:
        chat_history = json.load(f)
except FileNotFoundError:
    chat_history = []
    
def guardar_memoria(historial):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)

# Prompt institucional
template = """
Eres un asistente virtual del Instituto DUOC UC Plaza Oeste.

Debes responder exclusivamente utilizando la información entregada en el contexto.

Si la información solicitada no aparece en el contexto:

- Indica amablemente que no dispones de información oficial para responder.
- No inventes información.
- Sugiere al usuario revisar fuentes oficiales de DUOC UC como:
  - Portal del Alumno
  - Sitio web institucional
  - Dirección de Carrera
  - Mesa de Ayuda DUOC UC
  - Secretaría Académica

Mantén siempre un lenguaje formal, cordial y orientado a ayudar.

Historial de conversación:
{history}

Contexto:
{context}

Pregunta del usuario:
{question}

Respuesta:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=[
        "history",
        "context",
        "question"
    ]
)

# Modelo LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base=os.getenv("GITHUB_BASE_URL")
)

def decidir_accion(docs):

    if len(docs) == 0:
        return "SIN_INFORMACION"

    return "RESPONDER"

def rag_answer(question):

    global chat_history

    # Buscar documentos relevantes
    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    # Decidir acción
    accion = decidir_accion(docs)

    if accion == "SIN_INFORMACION":
        return (
            "No dispongo de información oficial "
            "para responder esta consulta. "
            "Te recomiendo revisar el Portal del Alumno, "
            "el sitio institucional de DUOC UC o contactar "
            "a tu Dirección de Carrera."
        )

    history_text = "\n".join([
        f"Usuario: {item['question']}\nAsistente: {item['answer']}"
        for item in chat_history[-5:]
    ])

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.format(
        history=history_text,
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    # Guardar memoria
    chat_history.append({
        "question": question,
        "answer": response.content
    })

    # Limitar historial SIN reasignar la lista completa
    del chat_history[:-20]

    guardar_memoria(chat_history)

    return response.content