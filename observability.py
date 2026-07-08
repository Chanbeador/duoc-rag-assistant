import json
import os
from datetime import datetime


LOG_FILE = "logs.json"


def save_log(
    question,
    tool,
    latency,
    success,
    response_valid=True,
    response_length=0,
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
        "response_valid": response_valid,
        "response_length": response_length,

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
    
def calculate_metrics():

    logs = load_logs()

    if len(logs) == 0:
        return {
            "total_requests": 0,
            "average_latency": 0,
            "success_rate": 0,
            "consistency_rate": 0,
            "average_response_length": 0,
            "tools": {}
        }


    total_requests = len(logs)


    average_latency = sum(
        log["latency"]
        for log in logs
    ) / total_requests


    successful_requests = sum(
        1
        for log in logs
        if log["success"]
    )


    success_rate = (
        successful_requests / total_requests
    ) * 100
    
    valid_responses = sum(
        1
        for log in logs
        if log["response_valid"]
    )


    consistency_rate = (
        valid_responses / total_requests
    ) * 100


    average_response_length = sum(
        log["response_length"]
        for log in logs
    ) / total_requests


    tools = {}

    for log in logs:

        tool = log["tool"]

        if tool in tools:
            tools[tool] += 1
        else:
            tools[tool] = 1


    return {
        "total_requests": total_requests,

        "average_latency": round(
            average_latency,
            3
        ),

        "success_rate": round(
            success_rate,
            2
        ),

        "consistency_rate": round(
            consistency_rate,
            2
        ),

        "average_response_length": round(
            average_response_length,
            2
        ),

        "tools": tools
    }