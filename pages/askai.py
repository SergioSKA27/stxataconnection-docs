import streamlit as st
from st_xatadb_connection import XataConnection



st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection")

xata = st.connection('xata',type=XataConnection)
client = xata._call_client()




st.title('✈️ Asking questions of your data with AI')
st.divider()

st.markdown('''
The ask endpoint helps you create interactive and engaging conversational interfaces, Q&A assistants, and chatbots.
It provides users with swift and direct access to the information they need, eliminating the need to navigate through
lengthy documentation or articles.

The endpoint leverages up-to-date information from your Xata database, such as documentation, knowledge bases, or any
source of data you've configured. The ask endpoint uses Xata's search capabilities to find relevant information from
your database, and uses this with OpenAI's ChatGPT API to interpret your question and generate natural language responses.

### How does it work?

At a high level, the ask endpoint works like this:


1. Run a text search against the database to find the records that are most relevant to the question asked by the user.

2. Take the most relevant results, and create a custom prompt for OpenAI.

3. Send the prompt to the ChatGPT API and let the model complete the answer.

The ask endpoint can use either keyword or vector search to find records that are most relevant to the user's query.
To learn more about keyword or vector searches, see our blog the compares the two approaches.

When you use the ask endpoint, you can choose to continue any conversation you've started.
Xata will remember the rules and context you've set, and allow you to continue to ask follow-up questions.
Check the examples below to see how to use it.
''')

st.code(r"""
result = xata.askai(
  "Tutorial",   # reference table
  "<question>", # question to ask
  [
    # array of strings with the rules for the model
  ],
  options={
    "searchType": "keyword|vector",
    "search": {
      "fuzziness": 0|1|2,
      "prefix": "phrase|disabled",
      "target": {
         # ...search target options...
      },
      "filter": {
        # ...search filter options...
      },
      "boosters": [
        # ...search boosters options...
      ]
    },
    "vectorSearch": {
      "column": "<embedding column>",
      "contentColumn": "<content column>",
      "filter": {
        # ...search filter options...
      }
    }
  }
)
""")

st.markdown('''
The response contains the generated answer and the record IDs that were used as context:
''')

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
### Asking follow-up questions

Xata supports the functionality of asking follow-up questions (as in a conversational model), which allows you to create
ChatGPT-style interfaces for your data. To achieve this, Xata introduces the concept of a session.

A session represents a single conversation between a user and the data in one of your Xata tables.
Each session contains relevant data from your tables, known as context.
The session preserves the rules you specified at its start, along with all the questions sent and answers received during the interaction.

When communicating with OpenAI, the ask endpoint ensures that your rules, your context,
and as many questions as possible are transmitted each time.
If the total amount of messages becomes too long for OpenAI to process,
Xata will trim messages from earlier in the conversation until the message size is manageable for OpenAI to handle effectively.

Each session maintains its own cached set of your context, so changes to the underlying data in your database will
not affect ongoing conversations. All cached information: your context, rules, and all conversations are automatically removed after 7 days.
''')

st.code(r"""
result = xata.askai_follow_up("Tutorial", "<your follow-up question>", "<session_id>")
""")

st.markdown('''
For more information on how to use the ask endpoint, see the [documentation](https://xata.io/docs/sdk/ask)
''')
