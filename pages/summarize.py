import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)
st.title("Summarize")
st.divider()

st.markdown("""
The summarize endpoint is used to run calculations on your data.
Summarizing or performing calculations on your data can reveal information to you or the users of your product.
You could request the total number of sales in January, the profit on a basketball, or to find the store in your city with the best sales numbers.

""")

st.subheader("What's the average price of a basketball?")

st.markdown("""
Here, the column is product. The summary - in it's two parts - will be average as the function, and sale_price as the column.
In plain language, you might ask "give me the average sale price for each product". The request would look like:
""")

st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

xata = st.connection('xata',type=XataConnection)

records = xata.summarize("sales", {
  "filter": { "product": "basketball" },
  "columns": ["product"],
  "summaries": {
    "average_sale_price": { "average": "sale_price" }
  }
})
""")

st.markdown("""
Since we specified product in columns, we get one row for each unique product in our table. In the request above,
we have a key average_sale_price. This is the name of your summary; you will see this appear in the result.
""")
st.code("""
{
  "summaries": [{ "product": "basketball", "average_sale_price": 16.6 }]
}
""", language="json")

st.markdown("""
For more information on the summarize endpoint, check out the [documentation](https://xata.io/docs/sdk/summarize).
""")
