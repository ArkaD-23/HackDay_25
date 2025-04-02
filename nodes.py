from langchain.schema import SystemMessage, HumanMessage
from models import llm

def best_practices_review(state):
    code = state["code"]
    prompt = f"Review the following code for best coding practices:\n{code}"
    return {"best_practices": llm([HumanMessage(content=prompt)]).content}

def readability_review(state):
    code = state["code"]
    prompt = f"Review the following code for readability and maintainability:\n{code}"
    return {"readability_review": llm([HumanMessage(content=prompt)]).content}

def merge_results(state):
    comments = "\n\n".join([
        state.get("static_analysis", "No static analysis results."),
        state.get("security_review", "No security review results."),
        state["best_practices"],
        state["readability_review"]
    ])
    return {"final_review": f"### AI Code Review Report:\n{comments}"}
