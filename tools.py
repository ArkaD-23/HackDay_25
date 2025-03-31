from langchain.tools import Tool
import subprocess

def run_static_analysis(file_path):
    try:
        result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

static_analysis_tool = Tool(
    name="Static Analysis",
    func=run_static_analysis,
    description="Runs pylint on the given Python file to detect issues."
)

def run_security_scan(file_path):
    try:
        result = subprocess.run(["bandit", "-r", file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

security_tool = Tool(
    name="Security Scanner",
    func=run_security_scan,
    description="Runs bandit security analysis on the given Python file."
)