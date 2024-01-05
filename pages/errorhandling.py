import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

st.title('Error Handling')
st.divider()

st.markdown('''
When using the Xata Python SDK, you may encounter errors. This page will help you understand the errors you may encounter and how to handle them.
By default, the Xata Python SDK never raises exceptions. Instead, it returns a result object that contains the status of the operation and the result of the operation if successful.
This leads  you to verify if the operation was successful or not with the is_success() method.
So you end up with code like this:
''')

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

response = xata.query("Table_Name")

if response.is_success():
    st.write("Query successful")
else:
    st.write("error querying table")
""",language='python')

st.markdown('''
Doing this for every operation can be tedious. For this reason, the st_xatadb_connection package checks the status of the operation and raises an exception if the operation was not successful.
So now you can write code like this:
''')

st.code("""
try:
    response = xata.query("Table_Name")
except Exception as e:
    st.write("Error querying table",e.status_code,e.message)
""")

st.markdown('''
If the response is not successful, the exception will be raised and you can handle it in the except block.
You can check the status code and the message of the exception to understand what went wrong.
See more about the status codes in the [Xata documentation](https://xata.io/docs/rest-api#responses).

#### Calling the Xata client to debug

If you are still having trouble, you can call the Xata client directly to debug.

Use the `xata._call_client()` function to call the Xata client directly.Then you have access to the full Xata client and can call any method you want.
Remember that the Xata client instance is not persistent and you can't use in session state.
''')
