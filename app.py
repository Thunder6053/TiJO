import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Prompty SOLID i inne
from prompts import (
    PROMPT_QA, PROMPT_SEC,
    PROMPT_SRP, PROMPT_OCP,
    PROMPT_LSP, PROMPT_ISP, PROMPT_DIP
)

# Wczytaj zmienne środowiskowe
load_dotenv()

# Inicjalizacja aplikacji
app = Flask(__name__)

# Konfiguracja Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# === ROUTY ===

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-tests', methods=['POST'])
def generate_tests():
    user_input = request.json.get("text", "")
    response = model.generate_content(PROMPT_QA + "\n" + user_input)
    return jsonify({"output": response.text.strip()})

@app.route('/analyze-security', methods=['POST'])
def analyze_security():
    user_input = request.json.get("text", "")
    response = model.generate_content(PROMPT_SEC + "\n" + user_input)
    return jsonify({"output": response.text.strip()})

@app.route('/check-solid', methods=['POST'])
def check_solid():
    user_input = request.json.get("text", "")
    principle = request.json.get("principle", "").upper()

    prompts = {
        "SRP": PROMPT_SRP,
        "OCP": PROMPT_OCP,
        "LSP": PROMPT_LSP,
        "ISP": PROMPT_ISP,
        "DIP": PROMPT_DIP
    }

    prompt = prompts.get(principle)
    if not prompt:
        return jsonify({"output": f"Nieznana zasada SOLID: {principle}"}), 400

    response = model.generate_content(prompt + "\n" + user_input)
    return jsonify({"output": response.text.strip()})

# === URUCHOMIENIE ===
if __name__ == '__main__':
    app.run(debug=True)