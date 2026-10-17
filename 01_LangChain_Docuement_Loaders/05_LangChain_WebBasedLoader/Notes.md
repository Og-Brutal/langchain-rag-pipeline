# WebBaseLoader

`WebBaseLoader` is a document loader in LangChain used to load and extract text content from web pages (URLs).

It uses **BeautifulSoup** under the hood to parse HTML and extract visible text.

## When to Use

- For blogs, news articles, or public websites where the content is primarily text-based and static.

## Limitations

- Doesn't handle JavaScript-heavy pages well (use `SeleniumURLLoader` for that).
- Loads only static content (what's in the HTML, not what loads after the page renders).

## Loading Multiple Pages

For multiple pages, make a **list of URLs** and pass the list to the loader.

```python
from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://www.paulgraham.com/greatwork.html",
]

loader = WebBaseLoader(urls)
docs = loader.load()

print(len(docs))   # 2 (one Document per URL)
```

- You get **one `Document` per URL**, returned in a single flat list.
- Each Document's `metadata["source"]` holds its URL, so you can tell which page a Document came from.
- For many URLs, use `loader.lazy_load()` to process one page at a time instead of holding everything in memory.