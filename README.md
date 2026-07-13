# Softpro School of AI — 46-Day AI Development Summer Training

> Course code: **SSAI-101** · Duration: 46 days · Build real, deployed LLM & agentic-AI apps on free tiers.

This repository holds **all course code, organized day-by-day**. Each day lives under its phase
folder and is broken into small, numbered, runnable modules so you can learn one idea at a time.

## How this repo is organized

```
45-Days-LLM-Engineering/
├── Phase-1-Foundations/         Days 1–15
├── Phase-2-RAG-and-Memory/      Days 16–20
├── Phase-3-Agents-and-Tools/    Days 21–32
├── Phase-4-Capstone/            Days 39–46
└── docs/                        Syllabus & reference material
```

> Full day-by-day breakdown (3 hrs/day, 3 projects + 1 capstone): see [`COURSE-PLAN.md`](COURSE-PLAN.md).

> 🎯 **Career Launchpad** — a parallel **30-min daily talk** on getting hired & winning clients
> (build-in-public + specialization). Plan: [`CAREER-PLAN.md`](CAREER-PLAN.md). Each day's deck lives
> in that day's `career-talk/` folder.

Inside every day:

```
Day-XX-Topic/
├── README.md            What you'll learn + how to run it
├── 01-first-concept/    A focused module: README.md + runnable .py files
├── 02-next-concept/
└── exercises/           Practice problems (+ solutions)
```

Run any example from inside its folder, e.g.:

```bash
python Phase-1-Foundations/Day-01-Python-Setup-Variables-and-Data-Types/02-numbers/numbers.py
```

## Curriculum at a glance

### Phase 1 — Foundations (Days 1–15)
Days **1–7 are a Python power-up** (everything you need before touching an LLM):

| Day | Topic |
|----:|-------|
| 1 | Python setup, data types, operators & variables |
| 2 | Strings, f-strings & string methods |
| 3 | Booleans, conditionals & logical operators |
| 4 | Loops (while, for, range, break/continue) |
| 5 | Functions, scope & `*args`/`**kwargs` |
| 6 | Data structures: lists, dicts, tuples, sets |
| 7 | Errors, modules & OOP |

Days **8–15** begin the AI track: HTTP/`requests`, async, `dotenv`, Pydantic, the **first Groq API call**, prompt engineering, multi-provider patterns, data handling, and Streamlit — leading into **Mini-project 1: AI Content Summarizer**.

### Phase 2 — RAG & Memory (Days 16–20)
CLI chatbot (conversation memory), embeddings, semantic search, Chroma, Streamlit → **Mini-project 1: Chat With Your Documents** (Day 20).

### Phase 3 — Agents & Tools (Days 21–32)
LangChain fundamentals (LCEL, prompts, parsers, memory), LangChain in practice (RAG + Streamlit apps), LangGraph, function calling & tools, ReAct agents, CrewAI, AutoGen, observability (Langfuse), guardrails → **Mini-project 3: Research Agent**.

### Phase 4 — Capstone + Placement (Days 39–46)
Capstone build sprint, deployment, demo day, resume/portfolio.

## The free-tier stack
Groq (primary) · Ollama (local) · Hugging Face · Gemini · Chroma / pgvector + Supabase · Streamlit / Gradio · Langfuse · deployed free on HF Spaces / Streamlit Cloud / Render.

> **Everything ships. Free-tier first. Multi-provider.** You can complete this whole course at ₹0 infra cost.

## Setup

> 🐍 First time installing Python? Follow the detailed
> [**Python Installation Guide**](Phase-1-Foundations/Python-Installation-Guide.md) (Windows / macOS / Linux).

```bash
# 1. Python 3.10+ recommended (3.12 used in this repo)
python --version

# 2. Create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies (Days 1–7 need almost nothing beyond the stdlib)
pip install -r requirements.txt
```

Start here → [`Phase-1-Foundations/Day-01-Python-Setup-Variables-and-Data-Types/`](Phase-1-Foundations/Day-01-Python-Setup-Variables-and-Data-Types/)
