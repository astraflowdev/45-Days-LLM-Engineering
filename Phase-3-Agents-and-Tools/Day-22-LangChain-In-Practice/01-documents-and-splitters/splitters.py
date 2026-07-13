"""
01 - Documents & splitters: the LangChain way to chunk text.

RAG step 1 is always the same: break big text into small, searchable CHUNKS.
Day 20 wrote a word-counter chunker by hand. LangChain gives you a smarter one
that respects the SHAPE of the text (paragraphs -> sentences -> words) so a
chunk rarely gets cut mid-sentence.

Two objects to meet:
    Document  -- LangChain's wrapper: .page_content (the text) + .metadata (a dict)
    RecursiveCharacterTextSplitter -- splits text/Documents into chunks with overlap

No API key needed -- splitting is pure text work.

Setup:
    pip install langchain-text-splitters langchain-core
Run:
    python splitters.py
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# A little "knowledge base" -- imagine this came from a PDF or a web page.
POLICY = """
Refund policy. Customers may request a refund within 30 days of purchase.
Refunds are processed to the original payment method within 5 business days.

Shipping. We ship across India. Standard delivery takes 4 to 7 working days.
Express delivery (extra charge) arrives in 1 to 2 days in metro cities.

Support. Reach us at help@example.in or call 1800-123-456, 9am-6pm, Mon-Sat.
Our office is in Pune, Maharashtra.
""".strip()


# --- 1. The splitter ------------------------------------------------------
# chunk_size    = target max characters per chunk.
# chunk_overlap = characters repeated between neighbours, so a fact split
#                 across a boundary still appears whole in at least one chunk.
# "Recursive" = it tries to split on big separators first (\n\n paragraphs),
# then smaller ones (\n, ". ", " "), only cutting mid-word as a last resort.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=160,
    chunk_overlap=30,
    separators=["\n\n", "\n", ". ", " ", ""],   # try these in order
)

# --- 2. Split raw text into string chunks ---------------------------------
chunks = splitter.split_text(POLICY)
print(f"Split {len(POLICY)} chars into {len(chunks)} chunks:\n")
for i, c in enumerate(chunks):
    print(f"--- chunk {i} ({len(c)} chars) ---")
    print(c)
    print()

# --- 3. The same thing, but as Document objects ---------------------------
# In RAG you usually carry METADATA (where did this text come from?) so you can
# cite sources later. create_documents makes a Document per chunk; you can
# attach metadata that every chunk inherits.
docs = splitter.create_documents(
    [POLICY],
    metadatas=[{"source": "policy.txt"}],
)
print(f"As Documents: {len(docs)} of them. First one:")
first = docs[0]
print("  .page_content:", repr(first.page_content[:60]), "...")
print("  .metadata    :", first.metadata)     # {'source': 'policy.txt'}
print()

# You can also build Documents by hand -- handy when each source is separate.
manual = Document(page_content="FAQ: yes, cash on delivery is available.",
                  metadata={"source": "faq", "topic": "payment"})
print("Hand-built Document:", manual.page_content, "|", manual.metadata)
print()

print("Takeaway: text -> Documents (content + metadata) -> chunks. That's RAG")
print("step 1. Next we embed these chunks and store them so we can search them.")
