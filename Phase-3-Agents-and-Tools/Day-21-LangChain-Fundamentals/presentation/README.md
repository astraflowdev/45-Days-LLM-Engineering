# Day 21 · Presentation — LangChain: Intro, Chains & Agents

A self-contained, branded slide deck (`index.html`) introducing LangChain: what it is, why it's
used, its core pieces (LCEL), and a first look at **agents** and LangGraph. Same Softpro deck
template as the Day-17 embeddings deck.

## How to present
- Open `index.html` in any browser (double-click — no server, no build).
- **→ / Space** next · **←** back · **F** fullscreen · click right/left half of the screen to move.
- ~16 slides ≈ a 20–30 min talk. Progress bar + slide counter at the edges.

## Slide map (speaker notes)
| # | Slide | Talk track |
|---|-------|-----------|
| 1 | Cover | We can call an LLM; real apps need more — prompts reused, steps chained, memory, tools, agents. |
| 2 | The problem | A raw `create(...)` is fine for a demo; a product re-writes the same plumbing. Frameworks remove it. |
| 3 | What is LangChain | Everything is a **Runnable** (`.invoke()` + `|`). Show the 3 layers: core / integrations / langgraph. |
| 4 | Why it's used | Swap models · compose (LCEL) · batteries · ecosystem. Be honest: overkill for one-off scripts. |
| 5 | Building blocks | The 5–6 pieces students use daily — maps 1:1 to modules 01–06. |
| 6 | LCEL | The core. `prompt \| model \| parser`; output flows left→right; batch/stream free. |
| 7 | Prompts + parsers | Templates reuse & validate; `with_structured_output` returns typed Pydantic objects. |
| 8 | Memory | `MessagesPlaceholder` + a history list. Note: `RunnableWithMessageHistory` is deprecated in 1.x. |
| 9 | What is an agent | Chain = fixed path *you* wrote; agent = the *model* decides. **Agent = LLM + tools + loop.** |
| 10 | ReAct loop | Think → Act → Observe → repeat → Answer. The diagram is the whole idea. |
| 11 | Tools | A tool is a Python function; the **docstring is the API** the model reads. `@tool`, `bind_tools`. |
| 12 | LangGraph | Chains are lines; loops/branches need a state machine. `create_agent` runs on LangGraph. |
| 13 | Roadmap | Day 21 → 22 (LangChain in practice: RAG + Streamlit) → 23 (LangGraph) → 24 (tools) → 25 (agent) → … → Mini-project 3. |
| 14 | Recap | Five takeaways. |
| 15 | Your move | Run modules 01→06 (they run with no key), then the two exercises. |
| 16 | Close | "Learn `invoke` and `|`, and everything composes." Tease Day 22. |

## Note
Content is intentionally aligned with the Day-21 code modules and forward-references the next Phase-3
days (LangGraph, tools, ReAct agents). Uses the latest LangChain 1.x framing throughout.
