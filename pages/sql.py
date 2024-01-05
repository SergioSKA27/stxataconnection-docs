import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection",)

xata = st.connection('xata',type=XataConnection)
st.title('🐘 SQL Queries')
st.divider()

st.markdown('''
Xata uses PostgreSQL under the hood to store your data. You can use SQL to work with your data. The results come back in
a typical Xata JSON response mechanism over HTTP. If the Xata API doesn't cover the query you need,
you can use SQL directly to do queries, insert data, update information, and delete records.

Xata offers support for a subset of PostgreSQL functions. This includes functions such as subquery, comparison, aggregate,
window, range, json, string, datetime, and array functions. Functions beyond these are not permitted.
''')

st.subheader('Examples')
st.markdown('''
The following are instances of working with data, including retrieving, selecting, inserting, and deleting records, using SQL in the Xata platform.
''')

st.code(r"""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)

records = xata.sql_query("SELECT * FROM \"teams\"")
""")

st.write('The following response is returned:')

st.code("""
{
  "records": [
    {
      "id": "rec_c8hng2h26un90p8sr7k0",
      "name": "Matrix",
      "owner": {
        "id": "myid"
      },
      "xata": {
        "version": 0,
        "createdAt": "2023-05-15T08:21:31.96526+01:00",
        "updatedAt": "2023-05-15T21:58:54.072595+01:00"
      }
    }
  ]
}
""",language='json')

st.subheader('Insert a new record using a parameterized query')
st.code(r"""
records = xata.sql_query(
  "INSERT INTO \"Users\" (name, email) VALUES ($1, $2)",
  ["Keanu Reeves", "keanu@example.com"]
)
""")

st.subheader('Delete record using a parameterized query')
st.code(r"""
xata.sql_query(
  "DELETE FROM \"Users\" WHERE id=$1",
  ["my-record-id"]
)
""")

st.markdown('''
For more information about SQL in Xata, see the [Xata documentation](https://xata.io/docs/sdk/sql/overview).
''')
