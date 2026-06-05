# Clinical Trial RAG Pipeline Agent

A retrieval-augmented generation (RAG) research agent for querying and synthesizing clinical trial literature. Built to answer complex questions over a private corpus of AML/oncology research papers and analyst reports — grounding every answer in primary source documents rather than model memory.

Supports two backends: **Groq-hosted LLM** (`groq_agent.py`) for higher reasoning quality, and **local Ollama LLM** (`ollama_agent.py`) for fully offline, API-free usage.

---

## What It Does

LLMs don't know your private documents. This agent solves that by:

- Ingesting PDFs, markdown, and plain text files into a local vector database
- Embedding each chunk using a HuggingFace sentence transformer model
- Retrieving the most semantically relevant chunks for any given query
- Calling tools (document search, calculator) via an agentic loop to reason over multiple steps
- Maintaining conversation memory so follow-up questions retain prior context
- Synthesizing a grounded natural language answer using either a Groq-hosted or local Ollama LLM

The result is a research assistant that can reason over 200+ pages of clinical trial data and return answers backed by actual source material.

---

## Architecture

```
Documents (PDF / .txt / .md)
        ↓
   PyMuPDF Loader
        ↓
  Text Chunking (LangChain RecursiveCharacterTextSplitter)
        ↓
  HuggingFace Embeddings (all-MiniLM-L6-v2)
        ↓
  ChromaDB Vector Store
        ↓
  LangChain Tool-Calling Agent
     ├── search_documents tool  →  Similarity Search (top-k chunks)
     └── calculate tool         →  numexpr expression evaluator
        ↓
  Conversation Memory (RunnableWithMessageHistory)
        ↓
  Groq LLM (groq_agent.py)  /  Ollama local LLM (ollama_agent.py)
        ↓
  Synthesized Answer
```

---

## Tech Stack

| Component | Tool |
|---|---|
| Document Loading | PyMuPDF, LangChain TextLoader |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |
| Agent Orchestration | LangChain AgentExecutor, create_tool_calling_agent |
| Conversation Memory | RunnableWithMessageHistory, ChatMessageHistory |
| Calculator | numexpr |
| LLM (cloud) | Groq — llama-3.1-8b-instant (`groq_agent.py`) |
| LLM (local) | Ollama — llama3.1:8b (`ollama_agent.py`) |

---

## Agent Tools

The agent decides which tools to call based on the query — it is not a fixed retrieval → answer pipeline.

**`search_documents(query)`** — Embeds the query and retrieves the top-k most semantically similar chunks from the ChromaDB vector store. Called whenever the agent needs to ground its answer in source documents.

**`calculate(expression)`** — Evaluates a mathematical expression using numexpr. Called when the agent needs to compute something (e.g. survival probabilities, hazard ratio arithmetic) rather than guess.

---

## Two Agent Backends

### `groq_agent.py` — Groq-hosted LLM
Uses the Groq API (free tier available). Higher reasoning quality, better tool-calling reliability, faster inference. Requires a `GROQ_API_KEY`.

### `ollama_agent.py` — Local Ollama LLM
Runs entirely on your machine — no API key, no internet required after model download. Useful for understanding the quality/speed tradeoff between local and hosted models. Requires [Ollama](https://ollama.com) installed locally.

---

## Setup

```bash
git clone https://github.com/tealplayer/RAG-Pipeline.git
cd RAG-Pipeline
pip install -r requirements.txt
```

**For Groq backend** — get a free API key at [console.groq.com](https://console.groq.com):

```bash
export GROQ_API_KEY="your-key-here"
```

**For Ollama backend** — install Ollama and pull the model:

```bash
ollama pull llama3.1:8b
```

Add your documents to the `data/` folder (PDF, `.txt`, or `.md` files), then run:

```bash
python ingest.py        # embed and store documents
python groq_agent.py    # start with Groq backend
# or
python ollama_agent.py  # start with local Ollama backend
```

---

## Example Queries

**Q: What are some predictions on the success of the REGAL trial?**

> Based on the provided research papers and clinical trial data, the key evidence includes: as of December 2025, 72 of 80 required events have occurred, with the IDMC recommending the trial continue without modification at both interim reviews. The event rate has decelerated from 2+ per month early in the trial to barely 1 per month. Sensitivity analysis sweeping BAT median OS from 8–20 months shows P(success) of 95–100% across all scenarios, with projected hazard ratios safely below the 0.636 threshold.

**Q: Is it plausible from this data to say there is a cure fraction?**

> Yes. The cure-fraction (mixture cure) model splits patients into two groups: cured patients whose risk drops to near zero, and uncured patients who follow a normal exponential decline. The predicted cure fraction of ~64% matches almost exactly with the Phase 2 immune response rate of 64% — a strong internal validation signal.

**Q: Could there be other explanations rather than a cure fraction?**

> A standard exponential model cannot explain the observed event deceleration pattern. Alternative explanations such as regression to the mean or selection bias do not fit the arithmetic: 72 events from 126 patients at 58 months of follow-up with implied mOS of ~48 months for the surviving cohort. The cure-fraction model is identified as the only one that simultaneously fits the curve and obeys the biological constraints of relapsed AML CR2.

---

## Data Sources

The corpus includes peer-reviewed clinical trial papers, published oncology research, and qualitative analyst reports covering:

- AML CR2 survival outcomes and treatment benchmarks
- Galinpepimut-S (GPS) Phase 1/2 trial data
- REGAL trial design and statistical methodology
- Cure fraction modeling in oncology

---

## Known Limitations & Future Work

**Table parsing** — Dense numerical tables in PDFs can be partially misread by the PDF loader. A vision-model based approach (converting pages to images) would improve extraction accuracy.

**Retrieval precision** — Specific numerical values buried in tables may not be retrieved if the surrounding text isn't semantically similar to the query. Increasing k or using hybrid search (keyword + semantic) would help.

**Multi-speaker attribution** — Documents sourced from comment threads (Reddit, Seeking Alpha) contain multiple authors per chunk. The agent can misattribute claims across speakers. Preprocessing to tag speakers before chunking would fix this.

**Tool-use hallucination** — Smaller models occasionally invoke the `calculate` tool with expressions they synthesized rather than ones directly stated in retrieved chunks. Prompt constraints and input validation would reduce this.

**Web UI** — Currently CLI only. A Streamlit or FastAPI frontend would make it more accessible.

**Live data ingestion** — Integrating NewsAPI or PubMed API to automatically pull new papers on a schedule would keep the corpus current.
