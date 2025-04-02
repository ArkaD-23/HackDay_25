import os
import requests
from langgraph.graph import StateGraph
from nodes import best_practices_review, readability_review, merge_results
from tools import static_analysis_tool, security_tool

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PR_NUMBER = os.getenv("PR_NUMBER")
REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER")
REPO_NAME = os.getenv("GITHUB_REPOSITORY").split("/")[-1]

def fetch_pr_changes():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/files"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    return "\n".join([file["patch"] for file in response if "patch" in file])

sg = StateGraph(dict)
sg.add_node("static_analysis", lambda state: {"static_analysis": static_analysis_tool.invoke(state["file"])})
sg.add_node("security_review", lambda state: {"security_review": security_tool.invoke(state["file"])})
sg.add_node("best_practices", best_practices_review)
sg.add_node("readability_review", readability_review)
sg.add_node("merge_results", merge_results)

sg.set_entry_point("static_analysis")
sg.add_edge("static_analysis", "security_review")
sg.add_edge("security_review", "best_practices")
sg.add_edge("best_practices", "readability_review")
sg.add_edge("readability_review", "merge_results")

graph = sg.compile()

code = fetch_pr_changes()
output = graph.invoke({"code": code, "file": "example.py"})  # Pass file path
final_review = output["final_review"]

def post_github_comment(review):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{PR_NUMBER}/comments"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"body": review}
    requests.post(url, headers=headers, json=data)

post_github_comment(final_review)
print("AI Code Review Completed!")
