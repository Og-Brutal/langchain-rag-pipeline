# load() vs lazy_load()

## `load()`: Eager Loading (loads everything at once)

- **Returns:** a list of `Document` objects
- Loads all documents immediately into memory
- **Best when:**
  - The number of documents is small
  - You want everything loaded upfront

## `lazy_load()`: Lazy Loading (loads on demand)

- **Returns:** a generator of `Document` objects
- Documents are not all loaded at once; they are fetched one at a time as needed
- **Best when:**
  - You're dealing with large documents or lots of files
  - You want to stream processing (e.g., chunking, embedding) without using lots of memory

## Example (500 PDFs)

`lazy_load()` gives a generator of docs, so you process one document at a time instead of holding all 500 PDFs in memory.

```python
docs = loader.load()             # list, everything in memory

for doc in loader.lazy_load():   # generator, one at a time
    print(doc.metadata)
```

## Quick comparison

| | `load()` | `lazy_load()` |
|---|---|---|
| Loading style | Eager | Lazy |
| Returns | list | generator |
| Memory use | All documents at once | One document at a time |
| Best for | Few documents | Many or large files |