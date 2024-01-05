import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)


st.title('Working with files')
st.divider()
st.markdown('''
All Xata record APIs can be used to create, read, update, delete and query files.
''')

st.subheader('Upload a file through inserting a new record')

st.code(r"""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)

record = xata.insert("Users", {
  "name": "Keanu",
  "photo": {
    "name": "file.png",
    "mediaType": "image/png",
    "base64Content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEklEQVR42mNk+M9QzwAEjDAGACCDAv8cI7IoAAAAAElFTkSuQmCC",
  }
})
""")


st.subheader('Upload a file through updating a record')
st.code(r"""
record = xata.update("Users", "record_id", {
  "photo": {
    "base64Content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEklEQVR42mNk+M9QzwAEjDAGACCDAv8cI7IoAAAAAElFTkSuQmCC"
  }
})""")

st.subheader('Append a file to an array through updating a record')
st.markdown('''
In the following example the photos column is of type file[] (file array). The existing file ids from the array must be present in the update.
''')
st.code(r"""
record = xata.update("Users", "record_id", {
  "photos": [
    {
      "id": "existing_file_id"
    },
    {
      "id": "new_id",
      "base64Content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEklEQVR42mNk+M9QzwAEjDAGACCDAv8cI7IoAAAAAElFTkSuQmCC"
    }
  ]
})""")

st.subheader('Download a file through reading a record')
st.markdown('''
The base64Content must be requested explicitly, it is not returned when selecting columns using wildcard.
''')
st.code(r"""
user = xata.get("Users", "record_id", columns=["photo.name", "photo.base64Content"])
""")

st.write('Response:')
st.code("""
{
  "id": "record_id",
  "photo": {
    "name": "file.png",
    "base64Content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAEklEQVR42mNk+M9QzwAEjDAGACCDAv8cI7IoAAAAAElFTkSuQmCC"
  }
}""",language='json')

st.subheader('Delete a file through updating a record')

st.code(r"""
record = xata.update("Users", "record_id", {"photo": None})
""")

st.subheader('Delete a file from an array through updating a record')
st.markdown('''
A file array item is deleted by setting the array to the set of ids that need to be kept.
''')
st.code(r"""
record = xata.update("Users", "record_id", {
  "photos": [
    {"id": "id_to_keep_1"},
    {"id": "id_to_keep_2"}
  ]
})
""")


st.subheader('File (binary) APIs')
st.markdown('''
Since all record APIs use JSON for both request and response body, the file content needs to be encoded.
For reasons like performance or data size on the wire, encoding the content might not be desired.
To work directly with binary file content, Xata introduces new file APIs. Similar to the other Xata APIs,
the file APIs require the Authorization header and a valid API key.
''')

st.subheader('Upload a file using the file API')
st.write('file column type:')
st.code(r"""
# file_content = bytes
response = xata.upload_file("table_name", "record_id", "column_name", file_content)
""")

st.subheader('Append a file to an array using file API')
st.write('Column type is file[] (file array). The fileId is optional and a unique id will be automatically generated if not provided.')
st.code(r"""
# file_content = bytes
response = xata.append_file_to_array("table_name", "record_id", "column_name", "file_id", file_content)
""")

st.subheader('Download a file using the file API')
st.write('file column type:')
st.code(r"""
file = xata.get_file("table_name", "record_id", "column_name")
""")
st.write('file[] (file array) column type:')

st.code(r"""
file = xata.get_file_from_array("table_name", "record_id", "column_name", "file_id")
""")

st.subheader('Delete a file using file API')
st.write('file column type:')
st.code(r"""
response = xata.delete_file("table_name", "record_id", "column_name")
""")

st.subheader('Delete a file from an array using file API')
st.write('Column type is file[] (file array). fileId is required to identify the array item to be deleted.')
st.code(r"""
response = xata.delete_file_from_array("table_name", "record_id", "column_name", "file_id")
""")

st.markdown('''
For more information on the File API, please refer to the [documentation](https://xata.io/docs/sdk/file-attachments).
''')
