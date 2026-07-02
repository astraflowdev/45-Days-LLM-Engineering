# Day 17 Presentation — Embeddings Fundamentals (Speaker Notes)

A self-contained, branded slide deck that explains every Day 17 concept visually, for absolute
beginners. Open **`index.html`** in any browser — no build step, no internet needed.

- **Navigate:** `→` / `Space` (next), `←` (back), `F` (fullscreen), or click the right/left half of
  the screen. Progress bar + slide counter at the edges.
- **Length:** 16 slides ≈ 25–30 min with discussion.
- **Style:** same Softpro deck template as the Day 5 logic-building / career decks, plus inline SVG
  diagrams (meaning map, cosine angle, score bars, RAG pipeline).

## Slide-by-slide (what to say)

| # | Slide | Talking point |
|--:|-------|---------------|
| 1 | Cover | Hook: how does a computer find the *right* note when no words match? Meaning, not letters. |
| 2 | The problem | "motor vehicle" vs "automobile" — keyword search misses it; semantic search doesn't. This whole phase rests here. |
| 3 | The big idea | **Embedding = text → list of numbers.** Repeat the one line: *similar meaning → similar numbers → close together.* |
| 4 | Meaning as a map | The 2-D map (animal-ness × vehicle-ness). cat/dog cluster; car/truck cluster. Close on map = close in meaning. Ties to module 01. |
| 5 | From 2 to 384 | We hand-picked 2 features to *see* it; a trained model picks hundreds. Today's model = 384. Can't picture 384-D, but "nearest" math is identical. |
| 6 | First embedding | The 3-line code. Free, local, `(384,)`. Show the real number row — looks like noise (next slide fixes that). |
| 7 | Similar = nearby | The query sits close to both vehicle docs (green), far from pasta/plants (grey). "automobile" is close with zero shared words. |
| 8 | Measuring close | Cosine = compare **direction**. Small angle → similar; big angle → different. Length doesn't matter. |
| 9 | The formula | Walk it slowly: dot product = multiply-and-add; norm = length; divide so only direction counts. One numpy line. Unit-vector shortcut → cosine = dot product. |
| 10 | The scale | −1 … 0 … +1. Related ≈ 0.3–0.9, unrelated ≈ 0. Scores are **relative within a set**, not a grade. |
| 11 | Worked ranking | Real `compare.py` scores as bars. "automobile" 0.642 wins. Return the top doc = semantic search. |
| 12 | Local vs cloud | Default = free/local/private. Gemini = optional cloud, same code shape. Provider is swappable. |
| 13 | Where this goes | The RAG pipeline diagram: docs→embed→DB, question→embed→query, cosine→nearest→answer. Today = the "embed" box. |
| 14 | Recap | The five takeaways. |
| 15 | Your move | Run modules 01→05, then the two exercises (semantic search + odd-one-out). |
| 16 | Close | "Meaning is just a point in space." Tee up Day 18 (Chroma vector DB + retrieval + chat). |

## Teaching tips
- **Slides 4 & 7 are the whole lesson** — spend time there. If students get "close on the map =
  close in meaning," everything else follows.
- Demo live if you can: run `03-similar-vs-different/compare.py` right after slide 11 so they see the
  real ranking print out.
- Don't dwell on the formula (slide 9). The intuition (slide 8: "same direction = same meaning")
  matters more than the algebra for beginners.

➡ Back to [Day 17](../README.md).
