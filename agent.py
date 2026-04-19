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

HEADERS = {
    "ngrok-skip-browser-warning": "true",
    "User-Agent": "Mozilla/5.0"
}

# ================================
# 🔑 OPENAI (OPTIONAL)
# ================================
client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ================================
# 🤖 GET OLLAMA MODEL
# ================================
def get_ollama_model(base_url):
    try:
        print(f"\n🔍 Attempting to connect to: {base_url}/api/tags")
        response = requests.get(
            f"{base_url}/api/tags",
            headers=HEADERS,
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("RAW TEXT:", response.text[:300])

        if response.status_code != 200:
            print(f"⚠️ Failed to get models. Status: {response.status_code}")
            return None

        data = response.json()
        models = data.get("models")

        if not models:
            print("⚠️ No models found on Ollama instance")
            return None

        model_name = models[0].get("name")
        print("DETECTED MODEL:", model_name)

        return model_name

    except Exception as e:
        print("MODEL ERROR:", e)
        print("⚠️ Make sure:")
        print("   1. Ollama is running")
        print("   2. ngrok tunnel is active (ngrok http 11434)")
        print("   3. ngrok URL is correct")
        return None


# ================================
# 🧠 OLLAMA REQUEST (STREAM FIX)
# ================================
def ollama_request(prompt, base_url):
    try:
        model = get_ollama_model(base_url)
        if not model:
            model = "mistral:latest"

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

        final_text = ""

        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    final_text += chunk.get("response", "")
                except:
                    pass

        return final_text.strip() if final_text else "❌ Empty response"

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