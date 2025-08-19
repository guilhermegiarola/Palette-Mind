from flask import Flask, request
from services.api_services import llm_call

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/llm_api/get_answer', methods=['POST'])
def get_answer():
    try:
        if request.is_json:
            data = request.get_json()
            history = data.get('history', []) if isinstance(data, dict) else data
            customPrompt = data.get('prompt')
            return {"response": llm_call(history, customPrompt)}
        else:
            return {"error": "Request must be JSON"}, 400
    except Exception as e:
        return {"error": str(e)}, 500



