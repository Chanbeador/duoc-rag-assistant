from rag_engine import rag_answer
from rag_engine import llm
from observability import save_log
import time

def show_memory():

    if not conversation_history:

        return "No hay conversaciones almacenadas."

    result = ""

    for item in conversation_history:

        result += (
            f"Pregunta: {item['question']}\n"
            f"Respuesta: {item['response']}\n\n"
        )

    return result

# Memoria simple
conversation_history = []

def write_email(request):

    prompt = f"""
    Eres un asistente académico de DUOC UC.

    Redacta un correo formal y profesional basado en la siguiente solicitud:

    {request}

    El correo debe incluir:
    - Asunto
    - Saludo formal
    - Desarrollo claro y respetuoso
    - Despedida formal

    Entrega únicamente el correo final.
    """

    response = llm.invoke(prompt)

    return response.content


def choose_tool(question):

    q = question.lower()

    if "memoria" in q:
        return "memory"

    email_keywords = [
        "correo",
        "mail",
        "redacta",
        "redactar",
        "email",
        "solicitud"
    ]

    if any(word in q for word in email_keywords):
        return "email"

    return "rag"



def agent_answer(question):

    start_time = time.time()

    tool = choose_tool(question)

    success = True
    error = None

    try:

        if tool == "memory":

            response = show_memory()

        elif tool == "email":

            response = write_email(question)

        else:

            response = rag_answer(question)


    except Exception as e:

        response = (
            "Ocurrió un error al procesar la solicitud."
        )

        success = False
        error = str(e)


    latency = time.time() - start_time


    save_log(
        question,
        tool,
        latency,
        success,
        response_valid=len(response) > 0,
        response_length=len(response),
        error=error
    )


    conversation_history.append(
        {
            "question": question,
            "response": response
        }
    )


    return response