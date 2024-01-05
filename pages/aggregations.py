import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection", page_icon="🦋")

xata = st.connection('xata',type=XataConnection)
st.title("Aggregations")
st.divider()
st.warning('This feature is Beta. It is still under active development. While we are avoiding breaking changes, we do not guarantee backwards compatibility until the functionality is GA.')

st.markdown("""
The aggregate API allows you to use the search/analytics engine to perform aggregations on your data.
Similar to the search API, it is important to understand that the Aggregation API is served from a different store,
which means: it is eventually consistent with the main store, and it cannot access the linked fields from a table.
If these limitations are not acceptable for your use case, you should use the Summarize API. The advantages of using
the Aggregation API, over the Summarize API, are:

- it generally offers better performance, because the underlying store is column oriented.

- it offers composable aggregations that can be combined into complex aggregations / visualizations.

Operations which are available both in the Aggregation and the Summarize API, such as sum, may present small
deviations due to differences in the order of reading data from storage and subsequent rounding, as well
as in case of in-flight data until consistency is achieved across the different stores.

An example of a relatively complex visualization that can be created with the Aggregation API could be: a multi-line chart,
where each line represents a movie genre, and the Y axis represents the average rating of the movies in that genre,
per year. This chart can be obtained with a single aggregation request, looking something like this:
""")

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)

results = xata.aggregate("titles", {
  "aggs": {
    "movieGenres": {
      "topValues": {
        "column": "genre",
        "size": 50,
        "aggs": {
          "byReleaseDate": {
            "dateHistogram": {
              "column": "releaseDate",
              "calendarInterval": "year"
            },
            "aggs": {
              "avgRating": {
                "average": {
                  "column": "rating"
                }
              }
            }
          }
        }
      }
    }
  }
})
""")

st.markdown("""
The code above combines three aggregations: topValues, dateHistogram and average. The topValues aggregations splits th
e data into buckets based on the genre column, and takes the top 50 genres by the number of movies in each.
The dateHistogram aggregation splits the data into buckets based on the releaseDate column,
and groups the data by calendaristic year. The average aggregation is a metric aggregation that is executed on the resulting buckets.

For more information on the Aggregation API, please refer to the [documentation](https://docs.xata.io/sdk/aggregate).
""")
