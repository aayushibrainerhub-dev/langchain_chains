from typing import Callable, Dict, Any

from langchain_core.runnables import RunnableBranch, RunnableLambda


def runnable_branch(use_llm: Callable[[], bool]) -> Dict[str, Any]:
    """Return a runnable-style branch decision for LLM versus fallback logic."""
    available = use_llm()
    try:
        branch_selector = RunnableBranch(
            branches={
                "llm": RunnableLambda(lambda _: {"use_llm": True, "branch": "llm"}),
                "fallback": RunnableLambda(lambda _: {"use_llm": False, "branch": "fallback"}),
            },
            default="fallback",
            condition=RunnableLambda(lambda _: "llm" if available else "fallback"),
        )
        result = branch_selector.run(None)
        if isinstance(result, dict):
            return result
    except Exception:
        pass

    return {"use_llm": available, "branch": "llm" if available else "fallback"}


def branch_on_model_availability(use_llm: Callable[[], bool]) -> Dict[str, Any]:
    """Legacy alias for runnable_branch."""
    return runnable_branch(use_llm)
