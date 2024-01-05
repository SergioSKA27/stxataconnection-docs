import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata', type=XataConnection)

st.title('Similarity / vector search')
st.divider()
st.warning("This feature is Beta. It is still under active development. While we are avoiding breaking changes, we do not guarantee backwards compatibility until the functionality is GA.")

st.markdown('''
The Xata vector type can be combined with the vectorSearch API to perform similarity search on your data based on embeddings.

An embedding is a vector of floating point numbers that represents the original data (text, image, audio, etc.). Embeddings are typically produced by a machine learning model. You can store the embeddings in Xata in a column of type vector and use the vectorSearch API call to find the nearest neighbors of a given embedding. This is useful in a number of use cases related to machine learning, such as: semantic search, recommendations, clustering, classification, and others.

Vector search works at the table level and has the following format:
''')

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata', type=XataConnection)
results = xata.vector_search("Docs", {
  "queryVector": [0.1, 0.2],  # array of floats
  "column": "embeddings",     # column name,
  "similarityFunction": "l1", # space function
  "size": 5,                  # number of results to return
  "filter": {},               # filter expression
})
""")

st.markdown('''
For more information about the vector search API, see the [API reference](https://xata.io/docs/sdk/vector-search).
''')
