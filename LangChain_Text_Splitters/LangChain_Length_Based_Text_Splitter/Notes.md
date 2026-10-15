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

## Example

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="",       # split purely by length
    chunk_size=100,     # max characters per chunk
    chunk_overlap=0,    # characters shared between neighbouring chunks
)

chunks = splitter.split_text(text)
```

## Quick Summary

Length based = fixed-size cuts. Fast and simple, but it can break words and meaning, so embeddings quality suffers.