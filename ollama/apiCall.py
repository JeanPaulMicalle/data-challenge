import requests
from config.configLoader import load_config

# Load configuration
config = load_config()

def my_llm_api(prompt, url=config["ollama_url"], model=config["ollama_model_name"]):
    # Append the correct endpoint
    endpoint = f"{url}/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,  
    }
    
    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.RequestException as e:
        print("HTTP API error:", e)
        return ""