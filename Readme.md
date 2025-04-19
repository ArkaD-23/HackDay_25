# 🚀 AI Code Reviewer using LangGraph & GitHub Actions

## 📌 Overview
This project is an **AI-powered code reviewer** that integrates with GitHub PRs. It uses **LangGraph** and **Azure OpenAI** to analyze pull requests, provide feedback, and suggest improvements automatically.

## 🎯 Features
- **PR Analysis**: Reviews code changes in GitHub pull requests.
- **AI-Powered Suggestions**: Uses GPT-4o via Azure OpenAI for intelligent feedback.
- **Security Checks**: Runs `pylint` and `bandit` to identify security risks.
- **Automated Workflow**: Uses GitHub Actions to trigger reviews on PR events.

## 🛠️ Tech Stack
- **LangGraph**: For AI workflow management.
- **Azure OpenAI (GPT-4o)**: For generating code reviews.
- **GitHub Actions**: For automating PR reviews.
- **pylint & bandit**: For static code analysis.

## 📂 Project Structure
```
/ai-code-reviewer
├── agent.py          # AI agent handling LLM interaction
├── nodes.py          # LangGraph nodes for workflow execution
├── config.py         # Environment configurations
├── .github/
│   ├── workflows/
│   │   ├── code-review.yml  # GitHub Actions workflow
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation
```

## 🚀 Setup & Installation
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables
Create a `.env` file similar to example.env.txt

### 4️⃣ Run the agent locally
```sh
python agent.py
```

## ⚙️ GitHub Actions Integration
The **GitHub Actions workflow** (`.github/workflows/code-review.yml`) automatically runs on **pull request events**:
- Fetches PR changes.
- Runs `pylint` and `bandit` for static analysis.
- Uses the AI agent to generate review comments.
- Posts feedback in the PR discussion.

## 🧠 Agent Graph Workflow

This project uses **LangGraph's `StateGraph`** to define a structured, sequential AI workflow for reviewing code in pull requests. Each step in the workflow analyzes the PR code from different perspectives and feeds its results into the next.

### 🔗 Workflow Structure

The agent uses a **directed graph** of LangGraph nodes, which execute in order to produce a complete, multi-dimensional review. Here's a breakdown of the nodes:

1. **`static_analysis`**  
   Runs traditional linting tools like `pylint` to catch syntax issues and code smells.

2. **`security_review`**  
   Uses tools like `bandit` to perform static security analysis on the code.

3. **`best_practices`**  
   AI-based evaluation of whether the code follows industry best practices (naming conventions, patterns, etc).

4. **`readability_review`**  
   Evaluates the clarity and maintainability of the code using GPT-4o.

5. **`merge_results`**  
   Collects feedback from all previous steps and compiles it into a single, cohesive review.

### ⚙️ Graph Construction Flow

```python
sg = StateGraph(dict)
sg.add_node("static_analysis", ...)
sg.add_node("security_review", ...)
sg.add_node("best_practices", ...)
sg.add_node("readability_review", ...)
sg.add_node("merge_results", ...)

sg.set_entry_point("static_analysis")
sg.add_edge("static_analysis", "security_review")
sg.add_edge("security_review", "best_practices")
sg.add_edge("best_practices", "readability_review")
sg.add_edge("readability_review", "merge_results")

graph = sg.compile()


## 📜 Example GitHub Actions Workflow
```yaml
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install Dependencies
        run: pip install -r requirements.txt
      
      - name: Run AI Code Review
        run: python agent.py
```

## 🏆 Future Enhancements
- Support for JavaScript (ESLint) and other languages.
- More advanced AI feedback using **LangChain memory**.
- Customizable PR feedback settings.

