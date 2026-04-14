import os
import agent
from agent import solve_problem, generate_code_only
from github_handler import create_repo_and_push
import json

# ================================
# 🔑 SETUP KEYS
# ================================
def setup_keys():
    if not os.path.exists(".env"):
        print("🔑 First time setup:\n")

        github_token = input("Enter your GitHub Token: ")
        openai_key = input("Enter your OpenAI API Key (optional): ")

        with open(".env", "w") as f:
            f.write(f"GITHUB_TOKEN={github_token}\n")
            f.write(f"OPENAI_API_KEY={openai_key}\n")

        print("\n✅ Keys saved!\n")


# ================================
# 🌐 MODE SELECTION
# ================================
def select_mode():
    print("""
===============================
 Select Mode
===============================

1. Online Mode (API)
2. Offline Mode (Ollama)
3. Remote Mode (ngrok)
""")

    choice = input("Select option: ")

    if choice == "1":
        return "online"
    elif choice == "2":
        return "offline"
    elif choice == "3":
        return "remote"
    else:
        print("❌ Invalid choice\n")
        return select_mode()


# ================================
# 📋 MAIN MENU
# ================================
def main_menu():
    print("""
===============================
 🤖 AI LeetCode Agent
===============================

1. Pick Problem
2. Exit
""")
    return input("Select option: ")


# ================================
# 🎯 MODE MENU
# ================================
def mode_menu():
    print("""
Choose Mode:

A) Understand Problem
B) Generate Code
C) Push to GitHub
D) Back
""")
    return input("Select option: ").upper()


# ================================
# 📚 PROBLEM SELECTION
# ================================
def get_problem():
    problems = [
        {
            "name": "two_sum",
            "title": "Two Sum",
            "description": "Given an array of integers nums and a target..."
        },
        {
            "name": "valid_parentheses",
            "title": "Valid Parentheses",
            "description": "Given a string containing brackets..."
        },
        {
            "name": "binary_search",
            "title": "Binary Search",
            "description": "Given a sorted array and a target..."
        },
        {
            "name": "palindrome_number",
            "title": "Palindrome Number",
            "description": "Check if a number is palindrome..."
        }
    ]

    print("\n📚 Choose a problem:\n")

    for i, prob in enumerate(problems, 1):
        print(f"{i}. {prob['title']}")

    try:
        choice = int(input("\nSelect problem (1-4): "))
        selected = problems[choice - 1]
    except:
        print("❌ Invalid selection\n")
        return get_problem()

    print(f"\n✅ Selected: {selected['title']}\n")
    return selected["name"], selected["description"]


# ================================
# 🧠 UNDERSTAND
# ================================
def understand_problem(problem, mode):
    print("\n🧠 Understanding...\n")
    result = solve_problem(problem, mode)
    print(result)
    return result


# ================================
# 💻 CODE
# ================================
def generate_code(problem, mode):
    print("\n💻 Generating Code...\n")
    result = generate_code_only(problem, mode)
    print(result)
    return result


# ================================
# 🚀 PUSH
# ================================
def push_to_github(problem_name, explanation, code):
    print("\n🚀 Pushing to GitHub...\n")

    os.makedirs(problem_name, exist_ok=True)

    with open(f"{problem_name}/README.md", "w", encoding="utf-8") as f:
        f.write(explanation or "No explanation")

    with open(f"{problem_name}/solution.py", "w", encoding="utf-8") as f:
        f.write(code)

    create_repo_and_push(problem_name, explanation, code)

    print("✅ Done!\n")


# ================================
# 🔁 MAIN LOOP
# ================================
def main():
    setup_keys()

    mode = select_mode()

    # 🔥 NGROK SETUP
    if mode == "remote":
        print("\n🌐 Enter your ngrok URL (example: https://abc.ngrok-free.app)\n")
        url = input("URL: ").strip()

        agent.NGROK_URL = url
        print(f"✅ Connected to: {url}\n")

    while True:
        choice = main_menu()

        if choice == "1":
            problem_name, problem = get_problem()

            explanation = None
            code = None

            while True:
                action = mode_menu()

                if action == "A":
                    explanation = understand_problem(problem, mode)

                elif action == "B":
                    code = generate_code(problem, mode)

                elif action == "C":
                    if not code:
                        print("⚠️ Generate code first\n")
                    else:
                        if not explanation:
                            explanation = solve_problem(problem, mode)

                        push_to_github(problem_name, explanation, code)

                elif action == "D":
                    break

                else:
                    print("❌ Invalid option\n")

        elif choice == "2":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option\n")


# ================================
# ▶ ENTRY
# ================================
if __name__ == "__main__":
    main()