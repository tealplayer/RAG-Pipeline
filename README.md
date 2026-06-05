# Clinical Trial RAG Pipeline Agent

A retrieval-augmented generation (RAG) research agent for querying and synthesizing clinical trial literature. Built to answer complex questions over a private corpus of AML/oncology research papers and analyst reports — grounding every answer in primary source documents rather than model memory.

## What It Does

LLMs don't know your private documents. This agent solves that by:

1. **Ingesting** PDFs, markdown, and plain text files into a local vector database
2. **Embedding** each chunk using a HuggingFace sentence transformer model
3. **Retrieving** the most semantically relevant chunks for any given query
4. **Synthesizing** a grounded natural language answer using a Groq-hosted LLM

The result is a research assistant that can reason over 200+ pages of clinical trial data and return answers backed by actual source material.

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
  Similarity Search (top-k chunks)
        ↓
  Groq LLM (llama-3.1-8b-instant)
        ↓
  Synthesized Answer
```

## Tech Stack

| Component | Tool |
|---|---|
| Document Loading | PyMuPDF, LangChain TextLoader |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Store | ChromaDB |
| LLM | Groq (llama-3.1-8b-instant) |
| Orchestration | LangChain |

## Setup

```bash
git clone https://github.com/tealplayer/RAG-Pipeline.git
cd RAG-Pipeline
pip install -r requirements.txt
```

Set your Groq API key (get one free at console.groq.com):
```bash
export GROQ_API_KEY="your-key-here"
```

Add your documents to the `data/` folder (PDF, .txt, or .md files), then run:
```bash
python ingest.py   # embed and store documents
python agent.py    # start the query interface
```

## Example Queries

**Q: What are some predictions on the success of the REGAL trial?**

> Based on the provided research papers and clinical trial data, the key evidence includes: as of December 2025, 72 of 80 required events have occurred, with the IDMC recommending the trial continue without modification at both interim reviews. The event rate has decelerated from 2+ per month early in the trial to barely 1 per month. Sensitivity analysis sweeping BAT median OS from 8–20 months shows P(success) of 95–100% across all scenarios, with projected hazard ratios safely below the 0.636 threshold.

---

**Q: Is it plausible from this data to say there is a cure fraction?**

> Yes. The cure-fraction (mixture cure) model splits patients into two groups: cured patients whose risk drops to near zero, and uncured patients who follow a normal exponential decline. The model is chosen because it has the fewest parameters, a direct biological rationale (GPS vaccine → immune memory → durable remission), and fits the observed survival curve. The predicted cure fraction of ~64% matches almost exactly with the Phase 2 immune response rate of 64% — a strong internal validation signal.

---

**Q: Could there be other explanations rather than a cure fraction?**

> The context raises several considerations. A standard exponential model cannot explain the observed event deceleration pattern. Alternative explanations such as regression to the mean or selection bias are discussed but do not fit the arithmetic: 72 events from 126 patients at 58 months of follow-up with implied mOS of ~48 months for the surviving cohort. The cure-fraction model is identified as the only one that simultaneously fits the curve and obeys the biological constraints of relapsed AML CR2.

## Data Sources

The corpus includes peer-reviewed clinical trial papers, published oncology research, and qualitative analyst reports covering:
- AML CR2 survival outcomes and treatment benchmarks
- Galinpepimut-S (GPS) Phase 1/2 trial data
- REGAL trial design and statistical methodology
- Cure fraction modeling in oncology

## Known Limitations & Future Work

- **Table parsing**: Dense numerical tables in PDFs can be partially misread by the PDF loader. A vision-model based approach (converting pages to images) would improve extraction accuracy.
- **Retrieval precision**: Specific numerical values buried in tables may not be retrieved if the surrounding text isn't semantically similar to the query. Increasing `k` or using hybrid search (keyword + semantic) would help.
- **Web UI**: Currently CLI only. A Streamlit or FastAPI frontend would make it more accessible.
- **Live data ingestion**: Integrating NewsAPI or PubMed API to automatically pull new papers and news on a schedule.
