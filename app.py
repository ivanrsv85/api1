from fastapi import FastAPI
import requests
import os

app = FastAPI()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "40e98986-3486-471e-8c5d-6a27d01f3d78"
FLOW_ID = "a4bb8b81-8469-4cd6-8898-d31597bed217"
APPLICATION_TOKEN = os.getenv("AstraCS:bqqnymgWUllnyMosZyutIDmm:901d81a553e8af935853e65022e0eeb8473d1ae51888c0df1cf5a6ab12e69871")

@app.get("/chat")
def chat(query: str):
    headers = {"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}
    payload = {"input_value": query, "output_type": "chat", "input_type": "chat"}
    response = requests.post(f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}", json=payload, headers=headers)
    return response.json()
