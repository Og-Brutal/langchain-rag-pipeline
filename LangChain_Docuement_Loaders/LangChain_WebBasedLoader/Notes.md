# WebBaseLoader

`WebBaseLoader` is a document loader in LangChain used to load and extract text content from web pages (URLs).

It uses **BeautifulSoup** under the hood to parse HTML and extract visible text.

## When to Use

- For blogs, news articles, or public websites where the content is primarily text-based and static.

## Limitations

- Doesn't handle JavaScript-heavy pages well (use `SeleniumURLLoader` for that).
- Loads only static content (what's in the HTML, not what loads after the page renders).