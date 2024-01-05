import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection",)

xata = st.connection('xata', type=XataConnection)

st.title("✒️ Inserting Records")
st.divider()

st.markdown('''
Once you've connected to your Xata.io database and queried your data, you can use st_xatadb_connection to insert new records into your database.
The general form of an insert request is:
''')


st.code("""
from st_xatadb_connection import XataConnection
import streamlit as st

xata = st.connection('xata', type=XataConnection)

response =xata.insert("table_name", {'column_name': 'value'})
""")

st.markdown('''
The  will insert a new record into the table with the specified column values with a generated record ID.
If you want to specify the record ID, you can do so by passing the record ID as the second argument to the `xata.insert()` function.
''')

st.code("""
response = xata.insert("table_name", {'column_name': 'value'}, "rec_id")
""")


st.subheader("Creating records in bulk")
st.markdown('''
If you have multiple records to insert, you can send them in a single request via the bulk endpoint. For example:
''')

st.code("""
users = xata.bulk_insert("Users",[
    {
      "email": "laurence@example.com",
      "name": "Laurence Fishburne",
      "team": "rec_cd8s4kbo8dsvsjilo1ug"
    },
    {
      "email": "hugo@example.com",
      "name": "Hugo Weaving",
      "team": "rec_cd8s4kbo8dsvsjilo1ug"
    },
    {
      "email": "joe@example.com",
      "name": "Joe Pantoliano",
      "team": "rec_cd8s4kbo8dsvsjilo1ug"
    }
  ])
""")

st.markdown('''
It is possible to provide IDs for each of the records. If records with the same IDs already exist, the bulk operation is cancelled and an error is returned.
file and file[] (file array) columns are not permitted in bulk requests.

For more information, see the [Xata API docs](https://xata.io/docs/sdk/insert).
''')

