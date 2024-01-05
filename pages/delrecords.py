import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection", page_icon="🦋")

xata = st.connection('xata', type=XataConnection)

st.title("Deleting records")
st.divider()
st.markdown('''
To delete a record you can execute, for example:
''')

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata', type=XataConnection)

response = xata.delete("table_name", "rec_id")
""")

st.markdown('''
    In case the record with the given ID doesn't exist, the REST API returns a 404 and throws an exception.
    Transactions are used to delete multiple records.Transactions will not fail a delete operation if no record is found.
    All operations in a transaction must succeed otherwise it is rolled back.
    for more information about the delete endpoint, see the [API reference](https://xata.io/docs/sdk/delete).
''')

