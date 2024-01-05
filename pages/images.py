import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

st.title('Image transformations')
st.markdown('''
It is also possible to make transformations directly on any given image URL without knowledge of the record it is attached to.

Performing client-side transformations can be useful for generating images conditionally based on media queries within a browser.
With this method, only a url for an existing Xata image is needed.
Here is an example of a simple image transformation:
''')

st.code(r"""
import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

img = xata.image_transform("https://us-east-1.storage.xata.sh/4u1fh2o6p10blbutjnphcste94", {
  "height": 100,
  "rotate": 180,
  "format": "webp"
})
""")

st.markdown('''
For more information on the available transformations, see the [Xata documentation](https://xata.io/docs/sdk/image-transformations).
''')
