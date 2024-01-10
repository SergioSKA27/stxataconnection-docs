import streamlit as st

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection",)
st.markdown('''
<style>
    .bg-image {
        background-color: #f8f8f3;
        background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221000%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath fill=%22none%22 d=%22M0 0h2000v1000H0z%22%2F%3E%3Cpath d=%22M0 166h0c25.972-5.025 51.944-10.05 93-15 41.056-4.95 97.196-9.825 132-12 34.804-2.175 48.273-1.649 76 12 27.727 13.649 69.713 40.42 109 41 39.287.58 75.876-25.031 117-22 41.124 3.031 86.785 34.704 118 29 31.215-5.704 47.984-48.786 81-64 33.016-15.214 82.278-2.56 122 14 39.722 16.56 69.904 37.023 101 47 31.096 9.977 63.108 9.466 98-2s72.666-33.888 106-48c33.334-14.112 62.228-19.913 99-29s81.423-21.46 119 2 68.08 82.75 103 90 74.258-37.54 114-39c39.742-1.46 79.89 40.413 109 41 29.11.587 47.184-40.111 80-48 32.816-7.889 80.376 17.032 120 23 39.624 5.968 71.312-7.016 143-20%22 fill=%22none%22 stroke=%22%23d7d3fd%22 stroke-linecap=%22round%22%2F%3E%3Cpath d=%22M0 333h0c29.712 11.528 59.425 23.057 98 20 38.575-3.057 86.013-20.698 120-37 33.987-16.302 54.524-31.265 86-20s73.892 48.757 110 51c36.108 2.243 65.91-30.765 101-26 35.09 4.765 75.47 47.3 111 58 35.53 10.7 66.212-10.438 103-24s79.681-19.548 113-23c33.319-3.452 57.062-4.37 90 10 32.938 14.37 75.07 44.031 112 34 36.93-10.031 68.656-59.753 109-84 40.344-24.247 89.307-23.017 125-9s58.115 40.823 91 44c32.885 3.177 76.232-17.273 109-21 32.768-3.727 54.957 9.27 88 24s76.94 31.196 114 22c37.06-9.196 67.286-44.053 105-50 37.714-5.947 82.918 17.015 120 27 37.082 9.985 66.04 6.992 135 4%22 fill=%22none%22 stroke=%22%238b7ff9%22 stroke-linecap=%22round%22%2F%3E%3Cpath d=%22M0 500h0c36.245 7.895 72.49 15.789 104 12 31.51-3.789 58.286-19.262 92-30s74.365-16.742 115-14c40.635 2.742 81.255 14.231 114 31 32.745 16.769 57.614 38.817 94 34s84.289-36.498 120-51c35.711-14.502 59.23-11.825 96 1s86.788 35.8 119 40c32.212 4.2 46.618-10.374 79-10 32.382.374 82.74 15.694 122 4 39.26-11.694 67.42-50.404 100-55 32.58-4.596 69.582 24.923 106 36 36.418 11.077 72.253 3.712 109 14s74.408 38.228 111 35c36.592-3.228 72.117-37.625 105-53 32.883-15.375 63.123-11.73 100-13 36.877-1.27 80.39-7.457 115-7 34.61.457 60.317 7.56 92 13s69.341 9.22 147 13%22 fill=%22none%22 stroke=%22%238679f9%22 stroke-linecap=%22round%22%2F%3E%3Cpath d=%22M0 666h0c31.064-8.985 62.128-17.97 95-6 32.872 11.97 67.55 44.896 104 32s74.669-71.613 109-76c34.331-4.387 64.775 45.556 102 58 37.225 12.444 81.232-12.61 123-27s81.298-18.115 110-12c28.702 6.115 46.575 22.07 78 16 31.425-6.07 76.403-34.168 116-27 39.597 7.168 73.812 49.6 111 73s77.35 27.767 113 5c35.65-22.767 66.792-72.669 102-82 35.208-9.331 74.485 21.908 106 24 31.515 2.092 55.27-24.962 89-16s77.436 53.94 113 51c35.564-2.94 62.985-53.796 98-46 35.015 7.796 77.622 74.244 114 72 36.378-2.244 66.525-73.181 104-78 37.475-4.819 82.279 56.48 119 74 36.721 17.52 65.36-8.74 134-35%22 fill=%22none%22 stroke=%22%23ada5fb%22 stroke-linecap=%22round%22%2F%3E%3Cpath d=%22M0 833h0c38.354-2.62 76.708-5.24 115-2s76.523 12.34 110 8c33.477-4.34 62.201-22.123 90-16 27.799 6.123 54.672 36.151 93 30 38.328-6.151 88.111-48.482 127-42 38.889 6.482 66.884 61.775 101 63 34.116 1.225 74.353-51.618 108-51 33.647.618 60.703 54.698 95 51 34.297-3.698 75.835-65.173 109-73 33.165-7.827 57.957 37.995 92 51 34.043 13.005 77.337-6.808 114-12s66.696 4.238 101 4c34.304-.238 72.879-10.144 107-21 34.121-10.856 63.79-22.662 104-31 40.21-8.338 90.962-13.21 127 12s57.36 80.5 86 76 64.595-68.788 104-73c39.405-4.212 82.259 51.654 119 66 36.741 14.346 67.37-12.827 138-40%22 fill=%22none%22 stroke=%22%23c8c2fc%22 stroke-linecap=%22round%22%2F%3E%3Cpath d=%22M0 999h0c39.697 18.561 79.395 37.123 117 38 37.605.877 73.118-15.93 106-20 32.882-4.07 63.133 4.598 99-8 35.867-12.598 77.351-46.462 110-45 32.649 1.462 56.462 38.25 88 51 31.538 12.75 70.8 1.463 106-6s66.335-11.1 106-8c39.665 3.1 87.859 12.937 125 24 37.141 11.063 63.23 23.351 96 24 32.77.649 72.221-10.341 105-19 32.779-8.659 58.885-14.986 89-30 30.115-15.014 64.238-38.714 107-39 42.762-.286 94.163 22.84 128 24 33.837 1.16 50.112-19.65 83-31 32.888-11.35 82.39-13.243 117-2s54.328 35.622 91 50 90.296 18.756 126 18c35.704-.756 53.487-6.644 84-11 30.513-4.356 73.757-7.178 157-10%22 fill=%22none%22 stroke=%22%238477f9%22 stroke-linecap=%22round%22%2F%3E%3C%2Fsvg%3E");
        bottom:0;
        left:-50%;
        position:fixed;
        right:-50%;
        top:0;
        z-index:0;
        background-size: cover;
        background-position: center center;
        background-repeat: repeat;
        opacity: 0.2;
    }
</style>
<div class="bg-image"></div>
''', unsafe_allow_html=True)

st.title('🚀 Getting Started')

st.markdown('''
---
Welcome to the Streamlit Xata Connection tutorial! In this tutorial, we'll show you how to use the `st_xatadb_connection` package
for connecting your Streamlit app to your Xata database. We'll cover the basics of using `st_xatadb_connection` to query your Xata database,
insert, update, and delete data, work with files, perform transactions, and ask questions to the AI assistant.

:blue[So let's get started!]

## 1. Set up your Xata.io and Streamlit Environment


- Create a Xata account and database at https://xata.io.

- Generate an API key for your Xata database.

- Get your Xata database URL endpoint.

- Install Streamlit by running `pip install streamlit`.

- Install st_xata_connection by running `pip install st-xatadb-connection`.


## 2. Configure your Xata Credentials

To securely store your Xata API key and database URL, you can use Streamlit's secrets manager or environment variables.
''',unsafe_allow_html=True)

st.code("""
XATA_API_KEY = "YOUR_XATA_API_KEY"
XATA_DB_URL = "YOUR_XATA_DATABASE_URL"
""",language='toml')

st.markdown('''
## 3. Connect to your Xata.io Database

Import the `st_xatadb_connection` package and use the st.connection() function to connect to your Xata database.
You could also use the the `st.session_state` object to store the connection object and reuse it across your Streamlit app.
''')

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata', type=XataConnection)

""",language='python')

st.markdown('''
## 4. Query your Xata.io Database

Use the `xata.query()` function to query your Xata.io database.
''')

st.code("""
results = xata.query("Table_Name")
""",language='python')

st.markdown('''
## 5. Display your Query Results

Use Streamlit functions like `st.write()`, `st.table()`,`st.json()`, or `st.dataframe()` to display your query results in your Streamlit app.
''')

st.code("""
st.write(results)
""",language='python')

st.markdown('''
## 6. Insert, Update, and Delete Data

You can also use st_xatadb_connection to insert, update, and delete data in your Xata.io database.
''')

st.code("""
record = {
    "name": "John Doe",
    "age": 30,
    "email": "a@b.com"
}

response = xata.insert("Table_Name", record)
""",language='python')

st.markdown('''
The `xata.insert()` function returns a response object that contains the information about the inserted record.
It looks like this:''')

st.code("""
{
      "id": "rec_c8hnbch26un1nl0rthkg",
      "xata": {
        "version": 0,
        "createdAt": "2023-05-15T08:21:31.96526+01:00",
        "updatedAt": "2023-05-15T21:58:54.072595+01:00"
      }
}""",language='json')

st.markdown('''
where `id` is the unique identifier of the inserted record, and `xata` contains the metadata about the record.
Now we can use the `id` to update the record or delete it. And in the same way, this functions also return a response object
that contains the information about the updated or deleted record.''')

st.code("""

update_response = xata.update("Table_Name", "rec_c8hnbch26un1nl0rthkg", {"age": 31})
delete_response = xata.delete("Table_Name", "rec_c8hnbch26un1nl0rthkg")

""",language='python')

st.markdown('''
## 7. Working with files

Xata supports file uploads and downloads. You can use the `xata.upload_file()` function to upload a file to your Xata database
or the `xata.get_file()` function to download a file from your Xata database.

Suppose you have a file called `my_avatar.png` in your current working directory. You can upload it to your Xata database like this:
''')

st.code("""
upload_response = xata.upload_file("Table_Name", "rec_c8hnbch26un1nl0rthkg", "column_name", "my_avatar_bas64_encoded")
""",language='python')

st.markdown('''
Now you can download the file from your Xata database like this:
''')

st.code("""
download_response = xata.get_file("Table_Name", "rec_c8hnbch26un1nl0rthkg", "column_name")
""",language='python')

st.markdown('''
## 8. Transactions

If you want to perform multiple operations on your Xata database as a single unit of work, you can use transactions.
For this, you can use the `xata.transaction()` function. It takes a list of operations as an argument and returns a response object.

Suppose you want to insert a record and update another record in your Xata database as a single unit of work.
You can do it like this:
''')

st.code("""

transaction_response = xata.transaction([
{"insert": {"table": "Table_Name", "record": {"name": "Marie Doe", "age": 21, "email": "marie@mail.com"}}}
{"update": {"table": "Table_Name", "id": "rec_c8hnbch26un1nl0rthkg", "fields": {"age": 31}}}
{"get": {"table": "Table_Name", "id": "rec_c8hnbch26un1nl0rthkg","columns": ["name", "age"]}}
{"delete": {"table": "Table_Name", "id": "rec_c8hnbch26un1nl0rthkg"}}
])

""",language='python')

st.markdown('''

Note that the `transaction()` function takes a list of operations as an argument. Each operation is a dictionary that contains
the type of operation and the operation-specific arguments. The supported operations are `insert`, `update`, `get`, and `delete`.
''')

st.markdown('''
## 9. SQL Queries

If you feel more comfortable with SQL, you can use the `xata.sql_query()` function to query your Xata database using SQL.

The `xata.sql_query()` function takes a SQL query as an argument and returns a response object with the query results.
For example, suppose you want to query your Xata database using SQL. You can do it like this:
''')

st.code("""
    sql_response = xata.sql_query("SELECT * FROM Table_Name")
""",language='python')

st.markdown('''
## 10. Asking to the AI Assistant

Xata has an AI assistant that can help you with your queries. You can use the `xata.askai()` function to ask a question to the AI assistant,
taking a reference to the table you want to query and the question you want to ask as arguments.

Suppose you want to ask the AI assistant to find the people in your table whose age is greater than 30. You can do it like this:
''')

st.code("""
response = xata.askai("Table_Name", "Find the people whose age is greater than 30")
""",language='python')

st.markdown('The response  looks like this:')

st.code("""
{
  "answer": "< answer >",
  "sessionId": "cg52bk1eqh5rd5hndhq95jercs",
  "records": [
    "b70d541d114ff54ad15915636450663f",
    "8ae4837002e21f013aa85c30a126ea1c",
    "4b137344a3c53d5152c45ed514188cd2"
  ]
}""",language='json')

st.markdown('''
---
## Conclusion

The `st_xatadb_connection` package is a powerful tool that makes it easy to connect your Streamlit app to your Xata database.
In this article, we've covered the basics of using `st_xatadb_connection` to query your Xata database, insert, update, and delete data,
work with files, perform transactions, and ask questions to the AI assistant. But there's a lot more you can do with `st_xatadb_connection`.

We encourage you to explore the `st_xatadb_connection` documentation on this site to learn more about the package's capabilities and
also check out the Xata documentation to learn more about the Xata service and all the features it offers.
We also encourage you to check out the `st_xatadb_connection` GitHub repository to see the source code and contribute to the project.

- [Xata Documentation](https://xata.io/docs/)

- [GitHub Repository](https://github.com/SergioSKA27/st-xatadb-connection)

<div style="text-align:center;font-family:monospace;font-size:18px">
Thank you for reading this article!<br> We hope you found it useful and that it will help you build amazing data-driven web applications with Xata and Streamlit.
</div>
''',unsafe_allow_html=True)

st.divider()
