"""
Day 18 - Step 5: Why Chroma and RAG chat matter.

Offline recap. No model call required.
"""

print("=" * 72)
print("DAY 18 RECAP: CHROMA, RETRIEVAL, AND AI CHAT")
print("=" * 72)

print("\n1) What you built")
print("- Embedded notes with a local model")
print("- Stored those vectors inside a persistent Chroma collection")
print("- Re-opened the database from disk")
print("- Retrieved the nearest notes for a new question")
print("- Sent the retrieved notes into an LLM chat prompt")

print("\n2) Why the database matters")
print("- Your vectors survive after the script exits")
print("- You can keep adding notes later")
print("- Retrieval becomes a clean database call")
print("- Metadata stays attached to each note")

print("\n3) Why this is already RAG")
print("RAG = Retrieval-Augmented Generation")
print("Retrieve relevant notes first, then let the model answer from them.")

print("\n4) The pipeline")
print("notes -> embeddings -> Chroma -> top-k matches -> chat model -> answer")

print("\n5) What comes next")
print("- Better chunking")
print("- Larger document collections")
print("- Cloud vector storage with pgvector")
print("- Better ranking and citations")

print("\n6) Mental model")
print("Day 16: chat memory")
print("Day 17: embeddings")
print("Day 18: persistent retrieval + AI chat")
print("Day 19: move the same idea to Postgres with pgvector")
