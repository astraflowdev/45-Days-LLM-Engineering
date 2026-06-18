"""
The provider problem -- scattered vs centralized (no API key needed).

Illustrates why every LLM call should go through ONE function, using a fake
"call" so it runs anywhere.

Run:
    python provider_problem.py
"""


# Imagine this is the only place in your app that knows about providers.
def ask(prompt, provider="gemini"):
    # In the real modules this dispatches to Gemini/Groq/Ollama. Here it's faked.
    return f"[{provider}] answer to: {prompt!r}"


# The rest of the app never mentions a provider by name -- it just calls ask().
print(ask("Summarize today's lesson."))
print(ask("Translate 'hello' to Hindi.", provider="groq"))
print(ask("Run this offline.", provider="ollama"))

print()
print("Switching providers, adding a fallback, or fixing a model name now happens")
print("in ONE function -- not scattered across the whole codebase.")
