import json
import os
from datetime import datetime


LOG_FILE = "logs.json"


def save_log(
    question,
    tool,
    latency,
    success,
    error=None
):
    """
    Guarda el registro de ejecución del agente.
    """

    log_entry = {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "question": question,
        "tool": tool,
        "latency": round(latency, 3),
        "success": success,
        "error": error
    }


    if os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            logs = json.load(file)

    else:

        logs = []


    logs.append(log_entry)


    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            logs,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_logs():

    if not os.path.exists(LOG_FILE):

        return []

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)