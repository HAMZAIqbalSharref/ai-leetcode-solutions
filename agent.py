import os
import requests
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ================================
# 🌐 GLOBAL CONFIG
# ================================
NGROK_URL = ""

# ================================
# 🔑 OPENAI (OPTIONAL)
# ================================
client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ================================
# 🌐 HEADERS (NGROK FIX)
# ================================
HEADERS = {
    "ngrok-skip-browser-warning": "true",
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

# ================================
# 🤖 GET OLLAMA MODEL
# ================================
def get_ollama_model(base_url):
    try:
        response = requests.get(
            f"{base_url}/api/tags",
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            print("STATUS:", response.status_code)
            print("RAW TEXT:", response.text)
            return None

        data = response.json()
        models = data.get("models")

        if not models:
            return None

        model_name = models[0].get("name")
        print("DETECTED MODEL:", model_name)

        return model_name

    except Exception as e:
        print("MODEL ERROR:", e)
        return None


# ================================
# 🧠 OLLAMA REQUEST (STREAMING)
# ================================
def ollama_request(prompt, base_url):
    try:
        model = get_ollama_model(base_url)

        if not model:
            return "❌ No Ollama model found. Run: ollama pull mistral"

        print("USING MODEL:", model)

        response = requests.post(
            f"{base_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True
            },
            headers=HEADERS,
            timeout=120,
            stream=True
        )

        if response.status_code != 200:
            return f"❌ HTTP Error {response.status_code}\n{response.text}"

        # 🔥 STREAMING LOGIC
        full_response = ""

        for line in response.iter_lines():
            if line:
                try:
                    chunk = line.decode("utf-8")
                    data = json.loads(chunk)
                    full_response += data.get("response", "")
                except:
                    pass

        return full_response

    except Exception as e:
        return f"❌ Ollama Error: {str(e)}"


# ================================
# 🧠 UNDERSTAND MODE
# ================================
def solve_problem(problem, mode):
    prompt = f"""
You are a coding tutor.

Explain the following problem clearly in simple terms.

DO NOT write any code.

Include:
- What the problem is asking
- Step-by-step logic
- Example walkthrough

Problem:
{problem}
"""

    # 🌐 ONLINE MODE
    if mode == "online":
        if not client:
            return "❌ No OpenAI API key found"

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenAI Error: {str(e)}"

    # 🌐 REMOTE MODE (NGROK)
    elif mode == "remote":
        if not NGROK_URL:
            return "❌ NGROK URL not set"
        return ollama_request(prompt, NGROK_URL)

    # 💻 OFFLINE MODE
    else:
        return ollama_request(prompt, "http://localhost:11434")


# ================================
# 💻 CODE MODE
# ================================
def generate_code_only(problem, mode):
    prompt = f"""
You are a competitive programmer.

Solve the following problem and return ONLY Python code.

Rules:
- No explanation
- No markdown
- Only pure Python code

Problem:
{problem}
"""

    # 🌐 ONLINE MODE
    if mode == "online":
        if not client:
            return "❌ No OpenAI API key found"

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenAI Error: {str(e)}"

    # 🌐 REMOTE MODE
    elif mode == "remote":
        if not NGROK_URL:
            return "❌ NGROK URL not set"
        return ollama_request(prompt, NGROK_URL)

    # 💻 OFFLINE MODE
    else:
        return ollama_request(prompt, "http://localhost:11434")