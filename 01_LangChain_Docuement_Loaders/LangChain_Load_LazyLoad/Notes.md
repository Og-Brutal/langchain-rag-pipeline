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

## Pulling one document at a time with `next()`

Since `lazy_load()` returns a generator, use `next()` to pull **one** document without looping.

```python
docs = loader.lazy_load()      # generator, nothing loaded yet

first = next(docs)             # loads the 1st document
second = next(docs)            # loads the 2nd document
```

### Key points

- The generator **remembers its position**, so each `next()` continues from where it stopped.
- If no documents are left, `next()` raises `StopIteration`.
- `next()` and a `for` loop share the same generator: after taking one with `next()`, a `for` loop continues with the **remaining** documents.
- A generator can only be consumed **once**. To start over, call `loader.lazy_load()` again for a fresh generator.

### Handling `StopIteration`

**1. Default value** (shortest, good for a single pull):

```python
doc = next(docs, None)
if doc is None:
    print("No more documents")
```

**2. `try/except`** (clearest when you need to do more than check for `None`):

```python
try:
    doc = next(docs)
    print(doc.metadata)
except StopIteration:
    print("No more documents")
```

**3. Manual loop:**

```python
while True:
    try:
        doc = next(docs)
    except StopIteration:
        break
    print(doc.metadata)
```

> A plain `for doc in docs:` loop handles `StopIteration` automatically, which is why you only see the error when calling `next()` yourself.

## Summary

`next(generator)` pulls one document at a time; use a default value or `try/except StopIteration` to handle the end safely.