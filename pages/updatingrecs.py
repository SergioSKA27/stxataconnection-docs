import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection")

xata = st.connection('xata', type=XataConnection)

st.title("📝 Updating Records")
st.divider()
st.markdown('''
In order to do a partial update to a record, you can use a request like this:
''')

st.code("""
from st_xatadb_connection import XataConnection
import streamlit as st

xata = st.connection('xata', type=XataConnection)

response = xata.update("table_name", "rec_id", {'column_name': 'value'})
""")

st.subheader("Replacing a record")
st.markdown('''
You can overwrite a full record with a request like this:
''')

st.code("""
response = xata.upsert("table_name", "rec_id", {'column_name': 'value'})
""")

st.markdown('''
For more information about the update and upsert endpoints, see the [API reference](https://xata.io/docs/sdk/update).
''')
