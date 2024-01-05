import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection")

xata =  st.connection('xata',type=XataConnection)

st.title('📋 Table Management')
st.divider()
st.markdown('''
With Xata, you can create, delete, and rename tables. You can also add and remove columns from tables.
''')

st.header('Create Table')
st.markdown('''
To create a table, you need to specify the table name and the columns and their data types.
You can do this by using the `create_table` method.
For example, to create a table named `movie` with two columns, `title` and `description`, you can do the following:
''')

st.code('''
import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

table_schema = {
  "columns": [
      {
          "name": "title",
          "type": "string",
      },
      {
          "name": "description",
          "type": "text",
          "notNull": True,
          "defaultValue": "Default text"
      }
  ]
}
result = xata.create_table('movie', table_schema)
''')

st.subheader('Delete Table')
st.markdown('''
To delete a table, you can use the `delete_table` method.
''')

st.code('''
result = xata.delete_table('users')
''')

st.subheader('Add Columns')
st.markdown('''
To add a column to a table, you can use the `create_column` method.
''')

st.code('''
result = xata.create_column('users', {'email': 'string'})
''')

st.subheader('Remove Columns')
st.markdown('''
To remove a column from a table, you can use the `delete_column` method.
''')

st.code('''
result = xata.delete_column('users', 'email')
''')

st.markdown('''
For more information, see the [Xata API reference](https://xata.io/docs/concepts/schema).
''')
