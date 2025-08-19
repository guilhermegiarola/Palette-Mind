import requests

def llm_call(history=None, customPrompt=None):
    MODEL = "llama3.2"
    OLLAMA_API = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}

    try:
        promptMessage ="You're an assistant that is designed to help with interactions between an independent artist and its clients. The messages you return shall be designed to keep some kind of informality, but keeping the conversation as polite as it can be. These messages sent by the user compose a conversation, you should always answer as the artist. " + customPrompt
        prompt = { 
            "role": "system", 
            "content": promptMessage 
        }

        messages = [prompt]
        if history:
            for msg in history:
                messages.append({"role": "user", "content": str(msg)})
        
        payload = {
            "model": MODEL,
            "messages": messages,
            "stream": False 
        }
        
        response = requests.post(OLLAMA_API, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        print(result)
        return result.get("message", {}).get("content", "No response received")
        
    except Exception as e:
        return f"Error: {str(e)}"


