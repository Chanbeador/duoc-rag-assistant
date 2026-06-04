from dotenv import load_dotenv
import os

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

# Prompt institucional
template = """
Eres un asistente virtual del Instituto DUOC UC Plaza Oeste.

Debes responder exclusivamente utilizando la información entregada en el contexto.

Si la información no está presente en el contexto, indica que dichos datos están fuera de tu área de atención.

No inventes información.

Usa lenguaje formal y claro.

Contexto:
{context}

Pregunta del usuario:
{question}

Respuesta:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# Modelo LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base=os.getenv("GITHUB_BASE_URL")
)


def rag_answer(question):
    """
    Recupera información desde FAISS y genera una respuesta.
    """

    # Buscar documentos relevantes
    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    # Construir contexto
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Crear prompt final
    final_prompt = prompt.format(
        context=context,
        question=question
    )

    # Consultar modelo
    response = llm.invoke(final_prompt)

    return response.content