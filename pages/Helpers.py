import streamlit as st
from st_xatadb_connection import XataConnection

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection", page_icon="🦋")

xata =  st.connection('xata',type=XataConnection)

st.title('🛠️ Helpers')
st.divider()

st.markdown('''
If you want to ingest multiple records in Xata, using bulk is the most efficient way. The BulkProcessor, a helper of the Python SDK, aims to make the process even simpler by abstracting away any complexity of juggling concurrent workers or chunking data, or maintaining queues.

You can use the BulkProcessor to e.g. ingest a CSV file into Xata or read documents from a queue and delegate the ingestion to the processor.

Two methods are available to put data in the processing queue:

```python
- bp.put_records(":table", ":records") to add multiple records

- bp.put_record(":table", ":record") to add only one record
```

Using the option of multiples, `bp.add_records(":table", ":records")` is more efficient as it requires less locking of the internal data structures.
To call the BulkProcessor, you can do the following:

''')

st.code(r"""
import streamlit as st
from st_xatadb_connection import XataConnection

xata =  st.connection('xata',type=XataConnection)

bp = xata.bulk_processor()

# The dict keys match the columns in the destination table "Users"
data = [
   {"name": "Max Musterman", "email": "max@acme.co"},
   {"name": "Ida von Klammer", "email": "ida@acme.co"},
   # ... more records
   {"name": "Mia Diaz", "email": "mia@acme.co"},
]
# Add records to processor
bp.put_records("Users", data)
# Ensure the Processing queue is flushed before the script terminates.
# This command will halt the script until all records have been pushed.
bp.flush_queue()

""")

st.markdown('''
You can also use the Transaction helper to perform transactions using the BulkProcessor. The Transaction helper
is an additional abstraction for bulk requests that process' requests in parallel.
To use the Transaction helper, you can do the following:

''')

st.code(r"""
transaction = xata.bulk_transaction()
""")

xata.bulk_transaction()

st.markdown('''
For more information, see the [Xata documentation](https://xata.io/docs/sdk/python/bulk-processor).
''')
