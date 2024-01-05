import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection", page_icon="🦋")

xata = st.connection(
    "xata", type=XataConnection
)

st.title("Getting records")

st.markdown(
    """
---
In this tutorial, you'll learn how to use st_xatadb_connection to connect to your Xata.io database and query your data.

the general form of a query is:"""
)

st.code(
    """
from st_xatadb_connection import XataConnection
import streamlit as st

xata = st.connection('xata', type=XataConnection)

data = xata.query("{table_name}", {
  "columns": [...],
  "filter": {
    ...
  },
  "sort": {
    ...
  },
  "page": {
    ...
  }
})
""",
    language="python",
)

st.markdown('''
See more details about the query parameters in the [API reference](https://xata.io/docs/sdk/get).

''')

st.markdown(
    "All the parameters are optional, so the simplest query request looks like this:"
)
st.code(
    """
results = xata.query("Table_Name")
"""
)

st.markdown("The response looks like this:")

st.code(
    """
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
    ],
    "meta": {
        "page": {
            "cursor": "jMq7DcIwEIDhnjH-2sWRAsItAT2KkOU8bAgB3Zkqyu6IDei_",
            "more": false
        }
    }
}""",
    language="json",
)


st.subheader("Getting a single record by ID")

st.markdown(
    """
You can retrieve a record with a given ID using a request like this:
"""
)

st.code(
    """
record = xata.get("Table_Name", "my_id")
""",
    language="python",
)


st.subheader('Pagination')

st.markdown('''

You can paginate your results using the `page` parameter in your query request. With pagination,
you can retrieve a subset of your data, which is useful when working with large datasets.

Xata offers two types of pagination:

- cursor-based  is optimal for building next / prev navigation patterns.

- offset-based is optimal for building 1..2..10...19..20 navigation patterns.


st_xatadb_connection supports both types of pagination.
Use the function `xata.query` to retrieve a page of records from your database. Save your response to a variable,
then if you want to retrieve the next page of records, use the `next_page` function. Pass the response  to the `next_page` function,
similarly you can use the `prev_page` function to retrieve the previous page of records.

Here's an example of how to use the `next_page` function:

''')

st.code(
'''
if 'results' not in st.session_state or st.session_state.results is None:
    st.session_state.results = xata.query("Table_Name", {"page": {"size": 10}})

st.write(st.session_state.results['records'])

if st.button("Next Page"):
    st.session_state.results = xata.next_page("Table_Name", st.session_state.results, pagesize=10)
    st.rerun()

''')

st.markdown('''
And similarly, you can use the `prev_page` function to retrieve the previous page of records.
Below you can see an example of the code showing how to use the `next_page` function:
''')

if 'page' not in st.session_state or st.session_state.page is None:
    st.session_state.page = xata.query("Users", {"page": {"size": 1}})


st.write(st.session_state.page['records'])

if st.button("Next Page"):
    st.session_state.page  = xata.next_page("Users", st.session_state.page, pagesize=1)
    st.rerun()

if st.button("Prev Page"):
    st.session_state.page = xata.prev_page("Users", st.session_state.page, pagesize=1)
    st.rerun()
