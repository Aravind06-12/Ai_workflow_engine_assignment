from .nodes.extract_functions import extract_functions
from .nodes.check_complexity import check_complexity
from .nodes.detect_issues import detect_issues
from .nodes.suggest_improvements import suggest_improvements

def code_review_workflow(code_text):
    """
    Runs the full code review workflow:
    1. Extract functions from the code
    2. Check complexity of functions
    3. Detect code issues
    4. Suggest improvements
    """

    functions = extract_functions(code_text)
    complexity_report = check_complexity(functions)
    issues = detect_issues(functions)
    suggestions = suggest_improvements(issues, complexity_report)

    return {
        "functions": functions,
        "complexity_report": complexity_report,
        "issues": issues,
        "suggestions": suggestions,
    }
