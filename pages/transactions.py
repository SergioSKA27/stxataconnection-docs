import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)

st.title('Transactions')
st.divider()

st.markdown('''
The transactions endpoint lets you execute multiple operations together as a single unit.
In this guide, we'll run through why transactions are important and run through Xata's transactions endpoint.
For this, you can use the `xata.transaction()` function. It takes a list of operations as an argument and returns a response object.

The Xata transactions API can be thought of as a way to wrap our existing insert, update, and delete operations into a
single operation. The options for each operation are almost identical to their non-transactional counterparts.

We'll start by taking a look at a full request-response, and then we'll step into each operation and its options.
''')

st.code("""

result = xata.transaction([
    { "insert": { "table": "titles", "record": { "originalTitle": "A new film" } } },
    { "insert": { "table": "titles", "record": { "id": "new-0", "originalTitle": "The squeel" }, "createOnly": True } },
    { "update": { "table": "titles", "id": "new-0", "fields": { "originalTitle": "The sequel" }, "ifVersion": 0 } },
    { "update": { "table": "titles", "id": "new-1", "fields": { "originalTitle": "The third" }, "upsert": True } },
    { "get": { "table": "titles", "id": "new-0", "columns": ["id", "originalTitle"] } },
    { "delete": { "table": "titles", "id": "new-0" } }
  ])

""")

st.markdown('''
Note that the `transaction()` function takes a list of operations as an argument. Each operation is a dictionary that contains
the type of operation and the operation-specific arguments. The supported operations are `insert`, `update`, `get`, and `delete`.

If successful, you can be certain that all operations have succeeded. You will receive a response like below:

''')

st.code("""
{
  "results": [
    { "operation": "insert", "rows": 1, "id": "rec-123456789" },
    { "operation": "insert", "rows": 1, "id": "new-0" },
    { "operation": "update", "rows": 1, "id": "new-0" },
    { "operation": "update", "rows": 1, "id": "new-1" },
    { "operation": "get", "columns": { "id": "new-0", "originalTitle": "The sequel" } },
    { "operation": "delete", "rows": 1 }
  ]
}""",language='json')

st.markdown('''
Or, in case of error, you know that all operations have been rolled back for you. You will receive a response like below:
''')

st.code("""
{
  "errors": [
    { "index": 0, "message": "table [invalid] not found" },
    { "index": 7, "message": "table [titles]: column [x]: column not found" }
  ]
}""",language='json')

st.markdown('''
for more information on transactions, please visit the API [documentation](https://xata.io/docs/sdk/transaction).
''')
