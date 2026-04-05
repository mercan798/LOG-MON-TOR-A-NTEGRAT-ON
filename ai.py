import requests

def analyze_log(log_line):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Kısa ve net açıkla, ve sorunu nasıl en iyi çözüleceğini de belirt:\n{log_line}",
            "stream": False
        }
    )

    return response.json()["response"]