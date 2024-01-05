import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata', type=XataConnection)


st.title("Searching records")

st.markdown('''
As you insert data into Xata, it is automatically indexed for full-text search.
You can run a search by using the search endpoint. While the query endpoint exists only at the table level,
the search endpoint exists both at the database branch and the table level, because it is possible to search
across table.

The search index is updated asynchronously after each insert, update, meaning that the search
results are eventually consistent with the results that you get from the query endpoint.
Another fundamental difference to the query endpoint is that search doesn't support following links.
This means that for links records you can filter by the ID of the linked record, but not any of the other
columns. If you need filter or search by linked columns, other than the ID, it is recommended that you
denormalize the data.
''')

st.subheader("Search across tables")
st.markdown('''
The format of a search request at the branch level (across tables) is as follows:
''')

st.code("""
results = xata.search({
  "query": "<search phrase>",
  "tables": [{
    "table": "...",
    "filter": {...},
    "target": [...],
    "boosters": [...]
  }, {
    ...
  }],
  "fuzziness": 1,
  "prefix": "phrase",
  "highlight": {...}
})
""")

st.markdown('''
A simple example, which searches across all tables with default relevancy settings, looks like this:
''')

st.code("""
results = xata.search({'query': 'search phrase'})
""")

st.subheader("Searching in a single table")

st.markdown('''
If you want to search in a single table, it's easier to use the table-level search API. It looks like this:
''')

st.code("""
results = xata.search_on_table("Users", {
  "query": "<search phrase>",
  "filter": {...},
  "target": [...],
  "boosters": [...],
  "fuzziness": 1,
  "prefix": "phrase",
  "highlight": {...}
})""")


st.markdown('''
In other words, the table level settings from the branch-level search API (filter, target, boosters) are top level settings in the per-table search API.
For more information about the search API, see the [API reference](https://xata.io/docs/sdk/search).
''')

