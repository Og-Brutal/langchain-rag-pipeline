# Length Based Text Splitting

Splits text by a **fixed size** only, with no regard for the content. The size can be set in:

- **Characters** (e.g. split after every 100 characters)
- **Tokens**

## Advantages

- Very fast
- Easy to implement

## Disadvantages

- Ignores grammar and language structure.
- Words and sentences can be cut in the middle.
- Chunks carry incomplete meaning, so the embeddings made from them don't capture complete and accurate semantic meaning.

## Chunk Overlap

Characters **repeated** at the end of one chunk and the start of the next.

```
Text: ABCDEFGHIJKLMNOPQRST   (chunk_size=10, chunk_overlap=3)

Chunk 1: ABCDEFGHIJ
Chunk 2:        HIJKLMNOPQ   <- starts with HIJ (overlap)
Chunk 3:               OPQRST
```

**Why we want it:** a cut can land in the middle of a sentence. The overlap keeps some shared context between neighbouring chunks, so meaning isn't lost at the boundary.

**Trade-off:** a larger overlap means **more chunks**, which means more embeddings, more storage and more computation.

```
chunks ≈ text_length / (chunk_size - chunk_overlap)
```

Keep the overlap small, typically 10-20% of `chunk_size`.

## Example

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="",       # split purely by length
    chunk_size=100,     # max characters per chunk
    chunk_overlap=20,   # characters shared between neighbouring chunks
)
```

## Two Splitting Functions

| Function | Input | Output |
|---|---|---|
| `split_text(text)` | A plain **string** | List of **strings** |
| `split_documents(docs)` | List of **Document** objects (from a loader) | List of **Documents**, metadata kept on every chunk |

```python
chunks = splitter.split_text(text)          # list[str]
chunks = splitter.split_documents(docs)     # list[Document]
```

## Quick Summary

Length based = fixed-size cuts. Fast and simple, but it can break words and meaning. Overlap reduces that damage but increases the chunk count and computation.