<div align="center">



# 🔗 LangChain RAG Pipeline

### ✨ A step-by-step, hands-on journey through every stage of **Retrieval-Augmented Generation**
*From raw documents to intelligent retrievers — built with **LangChain** and **Google Gemini**.*

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Pipeline-Complete-00C853?style=for-the-badge)
![License](https://img.shields.io/badge/Made%20for-Learning-7E57C2?style=for-the-badge)

<br/>

🧭 **[Overview](#-overview)** ・
🧩 **[Pipeline](#-the-rag-pipeline)** ・
🗂️ **[Structure](#-folder-structure)** ・
📄 **[Loaders](#-1-document-loaders)** ・
✂️ **[Splitters](#-2-text-splitters)** ・
🗄️ **[Vector Stores](#-3-embeddings-and-vector-stores)** ・
🔍 **[Retrievers](#-4-retrievers)** ・
🚀 **[Quick Start](#-quick-start)**

<br/>

![divider](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=4&section=footer)

</div>

---

## 📖 Overview

This repository documents my learning of **RAG (Retrieval-Augmented Generation)**, one component at a time. Every stage of the pipeline has its own folder with **runnable demo scripts** and **concise revision notes**.

> 💡 **Why RAG?** LLMs only know what they were trained on. RAG lets a model answer from **your own documents** by retrieving the most relevant pieces first and handing them to the model as context.

<div align="center">

🟢 &nbsp;**The core pipeline is now complete** &nbsp;🟢

`Document Loaders` → `Text Splitters` → `Embeddings` → `Vector Stores` → `Retrievers`

</div>

---

## 🧭 The RAG Pipeline

<div align="center">

*Every folder in this repo maps to one stage of the pipeline below.*

</div>

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0FB295','primaryTextColor':'#0B2E26','primaryBorderColor':'#0FB295','lineColor':'#5C6B73','fontSize':'15px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    A(["📄 Document<br/><b>Loaders</b>"]) ==> B(["✂️ Text<br/><b>Splitters</b>"])
    B ==> C(["🧮 <b>Embeddings</b>"])
    C ==> D(["🗄️ Vector<br/><b>Stores</b>"])
    D ==> E(["🔍 <b>Retrievers</b>"])
    E -.-> F(["🤖 <b>LLM</b><br/>Gemini"])
    F -.-> G(["💬 <b>Answer</b>"])

    classDef covered fill:#B2F2E5,stroke:#0FB295,stroke-width:2px,color:#0B2E26
    classDef external fill:#EEF2F7,stroke:#94A3B8,stroke-width:1.5px,stroke-dasharray:4 3,color:#1E293B
    class A,B,C,D,E covered
    class F,G external
```

<div align="center">

🟩 **Covered in this repo** &nbsp;&nbsp;·&nbsp;&nbsp; ⬜ **Used inside the demos (Gemini LLM)**

</div>

---

## 🗂️ Folder Structure

> *Click any folder to jump straight to it.*

```text
📦 langchain-rag-pipeline/
 ┃
 ┣ 📄 01_LangChain_Docuement_Loaders/       # Stage 1 ─ loading data
 ┃  ┣ 📂 01_LangChain_TextLoader/
 ┃  ┣ 📂 02_LangChain_PDFLoader/
 ┃  ┣ 📂 03_LangChain_DIrectoryLoader/
 ┃  ┣ 📂 04_LangChain_Load_LazyLoad/
 ┃  ┣ 📂 05_LangChain_WebBasedLoader/
 ┃  ┗ 📂 06_LangChain_CSVLoader/
 ┃
 ┣ ✂️ 02_LangChain_Text_Splitters/          # Stage 2 ─ chunking
 ┃  ┣ 📂 01_LangChain_Length_Based_Text_Splitter/
 ┃  ┣ 📂 02_LangChain_Text_Structure_Based_Text_Splitter/
 ┃  ┣ 📂 03_LangChain_Document_Structure_Based_Text_Spliter/
 ┃  ┗ 📂 04_LangChain_Semantica_Text_SPlitter/
 ┃
 ┣ 🗄️ 03_LangChain_Vector_Store_DataBases/  # Stage 3 ─ embeddings + vector stores
 ┃
 ┣ 🔍 04_LangChain_Retrievers/              # Stage 4 ─ fetching relevant chunks
 ┃  ┣ 📂 01_LangChain_Wikipedia_Retriever/
 ┃  ┣ 📂 02_LangChain_Vector_Store_Retriever/
 ┃  ┣ 📂 03_LangChain_MMR_Retriever/
 ┃  ┣ 📂 04_LangChain_Multi_Query_Retriever/
 ┃  ┗ 📂 05_LangChain_Contextual_Compression_Retriever/
 ┃
 ┣ 📜 requirements.txt
 ┣ 🙈 .gitignore
 ┗ 📘 README.md
```

<div align="center">

| 🧱 Stage | 📂 Folder | 💡 What's inside |
|:---:|:---|:---|
| **1️⃣ &nbsp;Loading** | [`01_LangChain_Docuement_Loaders`](./01_LangChain_Docuement_Loaders) | Loaders for text, PDF, directory, CSV and web pages |
| **2️⃣ &nbsp;Splitting** | [`02_LangChain_Text_Splitters`](./02_LangChain_Text_Splitters) | Length-based, text-structure, document-structure and semantic splitters |
| **3️⃣ &nbsp;Embeddings + Vector stores** | [`03_LangChain_Vector_Store_DataBases`](./03_LangChain_Vector_Store_DataBases) | Vector store theory notes and a Qdrant notebook |
| **4️⃣ &nbsp;Retrievers** | [`04_LangChain_Retrievers`](./04_LangChain_Retrievers) | Five retriever types, each with a demo and notes |

</div>

**📎 Root files**

| 📄 File | 🎯 Purpose |
|---|---|
| [`requirements.txt`](./requirements.txt) | All Python dependencies |
| [`.gitignore`](./.gitignore) | Keeps `.venv/` and `.env` (API keys) out of Git |

---

## 📄 1. Document Loaders

📁 **Folder:** [`01_LangChain_Docuement_Loaders`](./01_LangChain_Docuement_Loaders)

A loader reads a source and returns a **list of `Document` objects**, each with `page_content` (the text) and `metadata` (source, page, etc.).

| 🔧 Loader | 📁 Demo folder | 📑 Documents returned |
|---|---|---|
| `TextLoader` | [`01_LangChain_TextLoader`](./01_LangChain_Docuement_Loaders/01_LangChain_TextLoader) | 1 per file |
| `PyPDFLoader` | [`02_LangChain_PDFLoader`](./01_LangChain_Docuement_Loaders/02_LangChain_PDFLoader) | 1 per **page** |
| `DirectoryLoader` | [`03_LangChain_DIrectoryLoader`](./01_LangChain_Docuement_Loaders/03_LangChain_DIrectoryLoader) | 1 per file / page, using a glob pattern |
| `WebBaseLoader` | [`05_LangChain_WebBasedLoader`](./01_LangChain_Docuement_Loaders/05_LangChain_WebBasedLoader) · [Notes](./01_LangChain_Docuement_Loaders/05_LangChain_WebBasedLoader/Notes.md) | 1 per URL |
| `CSVLoader` | [`06_LangChain_CSVLoader`](./01_LangChain_Docuement_Loaders/06_LangChain_CSVLoader) | 1 per **row** |

### ⚡ `load()` vs `lazy_load()`

📁 [`04_LangChain_Load_LazyLoad`](./01_LangChain_Docuement_Loaders/04_LangChain_Load_LazyLoad) · [Notes](./01_LangChain_Docuement_Loaders/04_LangChain_Load_LazyLoad/Notes.md)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#FFD166','primaryTextColor':'#1F2937','primaryBorderColor':'#EAB308','lineColor':'#64748B','fontSize':'15px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    L(["🧰 <b>Loader</b>"])
    L ==>|"<b>load()</b> — eager"| E(["📚 <b>List of Documents</b><br/><i>everything in memory</i>"])
    L ==>|"<b>lazy_load()</b> — lazy"| G(["🔁 <b>Generator</b><br/><i>one Document at a time</i>"])

    classDef eager fill:#FFE3E3,stroke:#E11D48,stroke-width:2px,color:#7F1D1D
    classDef lazy fill:#C8F7DC,stroke:#0FB295,stroke-width:2px,color:#064E3B
    classDef loader fill:#FEF3C7,stroke:#D97706,stroke-width:2px,color:#78350F
    class L loader
    class E eager
    class G lazy
```

| | `load()` | `lazy_load()` |
|---|---|---|
| **Style** | Eager | Lazy |
| **Returns** | `list` | `generator` |
| **Memory** | All documents at once | One at a time |
| **Best for** | Few documents | Many or large files |

### 🔎 Glob patterns for `DirectoryLoader`

| 🔣 Pattern | 📥 Loads |
|---|---|
| `**/*.txt` | All `.txt` files in all subfolders |
| `*.pdf` | All `.pdf` files in the root directory |
| `data/*.csv` | All `.csv` files in the `data/` folder |
| `**/*` | All files, all folders |

> `**` means recursive search through subfolders.

---

## ✂️ 2. Text Splitters

📁 **Folder:** [`02_LangChain_Text_Splitters`](./02_LangChain_Text_Splitters) · [Overview notes](./02_LangChain_Text_Splitters/Notes.md)

LLMs and embedding models have **input limits**, so large text is split into smaller **chunks** before embedding. Smaller chunks give more accurate vectors, cleaner search results, and lower memory use.

| 🧪 Type | ⚙️ Splitter | 📁 Demo + notes |
|---|---|---|
| Length based | `CharacterTextSplitter` | [`01_LangChain_Length_Based_Text_Splitter`](./02_LangChain_Text_Splitters/01_LangChain_Length_Based_Text_Splitter) |
| Text structure based | `RecursiveCharacterTextSplitter` | [`02_LangChain_Text_Structure_Based_Text_Splitter`](./02_LangChain_Text_Splitters/02_LangChain_Text_Structure_Based_Text_Splitter) |
| Document structure based | `RecursiveCharacterTextSplitter.from_language` | [`03_LangChain_Document_Structure_Based_Text_Spliter`](./02_LangChain_Text_Splitters/03_LangChain_Document_Structure_Based_Text_Spliter) |
| Semantic meaning based | `SemanticChunker` | [`04_LangChain_Semantica_Text_SPlitter`](./02_LangChain_Text_Splitters/04_LangChain_Semantica_Text_SPlitter) |

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#60A5FA','primaryTextColor':'#0B1E3F','primaryBorderColor':'#2563EB','lineColor':'#475569','fontSize':'15px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart TD
    A(["✂️ <b>Text Splitters</b>"])
    A ==> B(["📏 <b>Length Based</b><br/><i>fixed size cuts</i>"])
    A ==> C(["📝 <b>Text Structure</b><br/><i>paragraph → line → word</i>"])
    A ==> D(["📑 <b>Document Structure</b><br/><i>Markdown / code aware</i>"])
    A ==> E(["🧠 <b>Semantic Meaning</b><br/><i>cuts where meaning shifts</i>"])

    classDef root fill:#DBEAFE,stroke:#2563EB,stroke-width:2.5px,color:#0B1E3F
    classDef leaf fill:#FEF3C7,stroke:#D97706,stroke-width:2px,color:#78350F
    class A root
    class B,C,D,E leaf
```

### 📏 Length based: `CharacterTextSplitter`

Cuts text at a fixed size. **Fast and simple**, but it ignores grammar, so words and sentences can be cut in half.

### 📝 Text structure based: `RecursiveCharacterTextSplitter`

Tries natural boundaries first (paragraph, then line, then word, then character), splitting only what is too big and merging small pieces back up to `chunk_size`.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#A78BFA','primaryTextColor':'#1E1B4B','primaryBorderColor':'#7C3AED','lineColor':'#64748B','fontSize':'14px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart TD
    T(["📝 <b>Input Text</b>"]) --> S1{"Fits in<br/><b>chunk_size</b>?"}
    S1 -->|✅ Yes| OK(["✅ <b>Chunk ready</b>"])
    S1 -->|❌ No| P["🧱 Split on <b>paragraph</b>"]
    P --> S2{"Piece fits?"}
    S2 -->|✅| OK
    S2 -->|❌| LN["📏 Split on <b>line</b>"]
    LN --> S3{"Piece fits?"}
    S3 -->|✅| OK
    S3 -->|❌| W["🔤 Split on <b>word</b>"]
    W --> S4{"Piece fits?"}
    S4 -->|✅| OK
    S4 -->|❌| CH["🔡 Split on <b>character</b>"]
    CH --> OK

    classDef ok fill:#BBF7D0,stroke:#16A34A,stroke-width:2px,color:#14532D
    classDef step fill:#EDE9FE,stroke:#7C3AED,stroke-width:1.5px,color:#3B0764
    classDef decision fill:#FEF3C7,stroke:#D97706,stroke-width:1.5px,color:#78350F
    class OK ok
    class T,P,LN,W,CH step
    class S1,S2,S3,S4 decision
```

### 📑 Document structure based

The same recursive splitter, but with **format-specific separators** (Markdown headings, `class` / `def` in code) tried first, so a section or function stays together.

### 🧠 Semantic meaning based: `SemanticChunker`

Embeds every sentence and **cuts where the meaning changes** (a big jump in distance between neighbouring sentences). It lives in `langchain-experimental`.

### 🔁 Chunk overlap

Characters repeated between neighbouring chunks, so meaning isn't lost at a cut.

```text
Text: ABCDEFGHIJKLMNOPQRST   (chunk_size=10, chunk_overlap=3)

   Chunk 1 ▶ ABCDEFGHIJ
   Chunk 2 ▶        HIJKLMNOPQ   ← starts with HIJ (the overlap)
   Chunk 3 ▶               OPQRST
```

> ⚠️ **Trade-off:** more overlap means more chunks, which means more embeddings, storage and computation. Keep it around **10–20%** of `chunk_size`.

### 🧪 Visualize your chunks

> 👉 **[ChunkViz: chunk visualizer](https://chunkviz.up.railway.app/)** — paste text, adjust size and overlap, and watch the chunk boundaries move in real time.

### ⚙️ Two splitting functions

| Function | Input | Output |
|---|---|---|
| `split_text(text)` | A plain string | `list[str]` |
| `split_documents(docs)` | `list[Document]` from a loader | `list[Document]`, metadata kept on every chunk |

---

## 🗄️ 3. Embeddings and Vector Stores

📁 **Folder:** [`03_LangChain_Vector_Store_DataBases`](./03_LangChain_Vector_Store_DataBases)

| 📄 File | 💡 What it is |
|---|---|
| [`Notes.md`](./03_LangChain_Vector_Store_DataBases/Notes.md) | Vector store theory: indexing, in-memory vs on-disk, vector store vs vector database, the LangChain common interface |
| [`LangChain_Qdrant_Vector_Store_updated .ipynb`](./03_LangChain_Vector_Store_DataBases/LangChain_Qdrant_Vector_Store_updated%20.ipynb) | Hands-on Qdrant notebook (create a collection, add documents, search, scroll through stored points) |

**Embeddings:** text chunks become vectors using `GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")` in the demos.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#34D399','primaryTextColor':'#064E3B','primaryBorderColor':'#059669','lineColor':'#475569','fontSize':'15px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    C(["📑 <b>Chunks</b>"]) ==> E(["🧮 <b>Embedding Model</b><br/><i>gemini-embedding-001</i>"])
    E ==> V(["🔢 <b>Vectors + Metadata</b>"])
    V ==> S(["🗄️ <b>Vector Store</b><br/>FAISS · Chroma · Qdrant"])

    classDef data fill:#F1F5F9,stroke:#64748B,stroke-width:1.5px,color:#0F172A
    classDef engine fill:#FDE68A,stroke:#D97706,stroke-width:2px,color:#78350F
    classDef store fill:#A7F3D0,stroke:#059669,stroke-width:2.5px,color:#064E3B
    class C,V data
    class E engine
    class S store
```

| 🗄️ Store | 📍 Where it is used |
|---|---|
| **FAISS** | Retriever demos (in-memory) |
| **Chroma** | [Vector Store Retriever](./04_LangChain_Retrievers/02_LangChain_Vector_Store_Retriever) |
| **Qdrant** | [Qdrant notebook](./03_LangChain_Vector_Store_DataBases) (local, on-disk) |

---

## 🔍 4. Retrievers

📁 **Folder:** [`04_LangChain_Retrievers`](./04_LangChain_Retrievers)

A retriever takes a **query** and returns the most relevant **`Document`s**. Each folder has a runnable demo and revision notes.

| 🧲 Retriever | 💡 Idea in one line | 📁 Demo + notes |
|---|---|---|
| 🌐 **Wikipedia** | Queries the Wikipedia API (**keyword matching**, no semantic search) | [`01_LangChain_Wikipedia_Retriever`](./04_LangChain_Retrievers/01_LangChain_Wikipedia_Retriever) · [Notes](./04_LangChain_Retrievers/01_LangChain_Wikipedia_Retriever/Notes.md) |
| 🧭 **Vector Store** | Embeds the query and returns the **top-k** closest chunks | [`02_LangChain_Vector_Store_Retriever`](./04_LangChain_Retrievers/02_LangChain_Vector_Store_Retriever) · [Notes](./04_LangChain_Retrievers/02_LangChain_Vector_Store_Retriever/Notes.md) |
| 🎯 **MMR** | Relevant **and diverse**, reduces duplicate-like results | [`03_LangChain_MMR_Retriever`](./04_LangChain_Retrievers/03_LangChain_MMR_Retriever) · [Notes](./04_LangChain_Retrievers/03_LangChain_MMR_Retriever/Notes.md) |
| 🔀 **Multi-Query** | An LLM rewrites the query into several versions, then merges the results | [`04_LangChain_Multi_Query_Retriever`](./04_LangChain_Retrievers/04_LangChain_Multi_Query_Retriever) · [Notes](./04_LangChain_Retrievers/04_LangChain_Multi_Query_Retriever/Notes.md) |
| 🗜️ **Contextual Compression** | Retrieves first, then an LLM keeps **only the relevant part** of each chunk | [`05_LangChain_Contextual_Compression_Retriever`](./04_LangChain_Retrievers/05_LangChain_Contextual_Compression_Retriever) · [Notes](./04_LangChain_Retrievers/05_LangChain_Contextual_Compression_Retriever/Notes.md) |

### 🤔 Which one should I use?

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#F472B6','primaryTextColor':'#500724','primaryBorderColor':'#DB2777','lineColor':'#64748B','fontSize':'14px','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart TD
    Q{"🧭 <b>What problem<br/>do you have?</b>"}
    Q -->|"🌐 Need data from the web"| W(["<b>Wikipedia Retriever</b>"])
    Q -->|"🧭 Normal semantic search"| V(["<b>Vector Store Retriever</b>"])
    Q -->|"🎯 Results repeat the same info"| M(["<b>MMR</b>"])
    Q -->|"🔀 Queries are vague or re-phrased"| MQ(["<b>Multi-Query</b>"])
    Q -->|"🗜️ Chunks contain too much noise"| CC(["<b>Contextual Compression</b>"])

    classDef q fill:#FCE7F3,stroke:#DB2777,stroke-width:2.5px,color:#500724
    classDef sol fill:#C8F7DC,stroke:#0FB295,stroke-width:2px,color:#064E3B
    class Q q
    class W,V,M,MQ,CC sol
```

| | 🔎 Searches by | 🤖 Needs an LLM | 💸 Extra cost |
|---|---|---|---|
| **Wikipedia** | Keywords | ❌ No | 🌐 Network call |
| **Vector Store** | Meaning (embeddings) | ❌ No | — |
| **MMR** | Meaning + diversity | ❌ No | — |
| **Multi-Query** | Meaning, several phrasings | ✅ **Yes** | +1 LLM call per search |
| **Contextual Compression** | Meaning, then trimmed | ✅ **Yes** | +1 LLM call **per retrieved chunk** |

---

## 🚀 Quick Start

<details open>
<summary><b>⚙️ &nbsp;Set up in 5 steps</b></summary>

<br/>

**1️⃣ &nbsp;Clone the repo**

```bash
git clone https://github.com/Og-Brutal/langchain-rag-pipeline.git
cd langchain-rag-pipeline
```

**2️⃣ &nbsp;Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows
```

**3️⃣ &nbsp;Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ &nbsp;Add your Gemini API key**

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey). The `.env` file is already in `.gitignore`, so it won't be committed.

**5️⃣ &nbsp;Run any demo** *(from inside its own folder, because some demos use relative file paths)*

```bash
cd 04_LangChain_Retrievers/03_LangChain_MMR_Retriever
python3 LangChain_MMR_Retriever.py
```

> 💡 If your path contains spaces, wrap it in quotes: `cd "/path/with spaces/project"`.

</details>

### 🩺 Troubleshooting

| 🐛 You see | 🩹 Meaning / fix |
|---|---|
| `DeprecationWarning: langchain-community is being sunset` | Harmless warning, the code still runs |
| `503 UNAVAILABLE ... high demand` | Google's servers are busy. Wait and retry, or switch Gemini model |
| `np.float_ was removed in NumPy 2.0` (Chroma) | Old `chromadb`. Run `pip install -U chromadb langchain-chroma` |
| `JSONDecodeError` from the Wikipedia retriever | Set a custom user agent: `wikipedia.set_user_agent("YourApp/1.0 (you@example.com)")` |
| `ModuleNotFoundError: langchain_classic` | `pip install langchain-classic` |

---

## 🧰 Tech Stack

<div align="center">

| 🛠️ Tool | 🎯 Role |
|---|---|
| [**LangChain**](https://python.langchain.com/) | Framework for building LLM applications |
| [**Google Gemini**](https://ai.google.dev/) | LLM and embeddings, via `langchain-google-genai` |
| [**FAISS**](https://github.com/facebookresearch/faiss) | In-memory vector search |
| [**Chroma**](https://www.trychroma.com/) | Vector store (`langchain-chroma`) |
| [**Qdrant**](https://qdrant.tech/) | Vector database (`langchain-qdrant`, `qdrant-client`) |
| `pypdf` | PDF text extraction |
| `beautifulsoup4` + `requests` | Web page loading |
| `wikipedia` | Wikipedia retriever backend |
| `python-dotenv` | Loads API keys from `.env` |

</div>

---

## 🛣️ Roadmap

- [x] 📄 &nbsp;Document loaders (text, PDF, directory, CSV, web)
- [x] ⚡ &nbsp;`load()` vs `lazy_load()`
- [x] ✂️ &nbsp;Text splitters (length, text-structure, document-structure, semantic)
- [x] 🧮 &nbsp;Embeddings
- [x] 🗄️ &nbsp;Vector stores (FAISS, Chroma, Qdrant)
- [x] 🔍 &nbsp;Retrievers (Wikipedia, Vector Store, MMR, Multi-Query, Contextual Compression)
- [ ] 🚧 &nbsp;Next: end-to-end RAG chains in a separate repository

---

## 🤝 Notes

This is a learning project, so each folder is kept **small and focused**: one concept, one demo, one set of notes. Feedback and suggestions are welcome through [Issues](https://github.com/Og-Brutal/langchain-rag-pipeline/issues).

<br/>

<div align="center">

### ⭐ If this helped you learn, consider leaving a star!

**Built with ❤️ by [Abdul Wahab](https://github.com/Og-Brutal)**

[⬆ Back to top](#-langchain-rag-pipeline)

<br/>

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=80&section=footer)

</div>
