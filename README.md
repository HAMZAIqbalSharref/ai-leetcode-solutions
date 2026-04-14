# 🚀 AI LeetCode Agent

An intelligent AI-powered assistant designed to help users **understand, solve, and automate LeetCode problems** using both **online and offline AI models**.

---

## 🧠 Overview

AI LeetCode Agent is a multi-mode AI system that allows users to:

* 📘 Understand coding problems step-by-step
* 💻 Generate optimized Python solutions
* 🌐 Use cloud AI (OpenAI)
* 🖥️ Run fully offline using local models (Ollama)
* 🔗 Access remotely via ngrok
* 📦 Distribute as a standalone EXE application

---

## ⚙️ Features

### 🔍 1. Understand Mode

* Explains problems in simple terms
* Provides step-by-step logic
* Includes example walkthroughs
* No code — purely conceptual understanding

---

### 💻 2. Code Generation Mode

* Generates clean Python solutions
* No extra explanation
* Competitive programming optimized

---

### 🌐 3. Online Mode (OpenAI)

* Uses cloud AI models
* High-quality responses
* Requires API key

---

### 🖥️ 4. Offline Mode (Ollama)

* Runs locally on user machine
* No internet required
* Automatically detects installed models

---

### 🔗 5. Remote Mode (ngrok)

* Exposes local AI over internet
* Allows others to use your local model
* Useful for testing and sharing

---

## 🏗️ Architecture

```
User Input
   ↓
Mode Selection
   ↓
-----------------------------------
| Online  → OpenAI API            |
| Offline → Ollama (localhost)    |
| Remote  → ngrok tunnel          |
-----------------------------------
   ↓
AI Processing
   ↓
Output (Explanation / Code)
```

---

## 📦 Installation

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd AI-LeetCode-Agent
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Setup environment (optional for online mode)

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run application

```
python main.py
```

---

## 🖥️ Offline Setup (Ollama)

Install Ollama and run:

```
ollama pull mistral
ollama serve
```

---

## 🔗 Remote Setup (ngrok)

```
ngrok http 11434
```

Then paste the URL inside the application.

---

## 📦 EXE Distribution

The project can be compiled into a standalone executable using:

```
pyinstaller main.spec
```

---

## ⚠️ Notes

* `.env` file is not included for security reasons
* Ollama must be running for offline mode
* ngrok must be active for remote mode

---

## 🚀 Future Improvements

* GUI interface (Tkinter / Electron)
* Persistent chat memory
* Multi-language support
* Web-based deployment (SaaS)

---

## 👨‍💻 Author

Developed as a full-stack AI project integrating:

* Local AI inference
* Cloud APIs
* Dev tooling & automation
* Executable distribution

---

## ⭐ Final Thoughts

This project demonstrates a hybrid AI system combining:

* Local intelligence (privacy + speed)
* Cloud intelligence (accuracy)
* Deployment flexibility

A step toward building real-world AI-powered developer tools.
