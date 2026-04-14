from github import Github
import os
import time
from dotenv import load_dotenv

load_dotenv()


def generate_project_readme():
    return """# 🤖 AI LeetCode Solver

This project automatically solves coding problems using AI and pushes them to GitHub.

## 🚀 Features
- Auto problem solving using AI
- Extracts clean code solutions
- Uploads structured solutions to GitHub
- Organized by problem folders

## 📁 Structure
problems/
  two_sum/
    README.md
    solution.py

## 🧠 How it works
1. Input problem
2. AI generates solution
3. Code extracted
4. Files pushed to GitHub automatically

## ⚙️ Tech Used
- Python
- PyGithub
- AI API

## 🔥 Goal
Build a fully automated AI coding assistant + portfolio generator.
"""


def create_repo_and_push(problem_name, readme_content, code_content):
    print("🚀 FUNCTION STARTED")

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ GitHub token not found")
        return

    g = Github(token)
    user = g.get_user()
    print("👤 User:", user.login)

    # 🔥 MAIN REPO NAME (CHANGE IF YOU WANT)
    repo_name_main = "ai-leetcode-solutions"

    # ✅ GET OR CREATE REPO
    try:
        repo = g.get_repo(f"{user.login}/{repo_name_main}")
        print("📂 Using existing repo")

    except:
        print("📦 Creating main repo...")
        repo = user.create_repo(repo_name_main, private=False)

        # Give GitHub a second to register repo
        time.sleep(2)

        # Create main README
        repo.create_file(
            "README.md",
            "Initial commit",
            generate_project_readme()
        )

    # 📁 STRUCTURE: problems/<problem_name>/
    folder_path = f"problems/{problem_name}"

    print(f"📁 Adding problem: {problem_name}")

    try:
        repo.create_file(
            f"{folder_path}/README.md",
            "Add problem explanation",
            readme_content
        )

        if code_content:
            repo.create_file(
                f"{folder_path}/solution.py",
                "Add solution",
                code_content
            )

        print(f"✅ Successfully added: {problem_name}")

    except Exception as e:
        print("⚠️ File already exists or error:", e)