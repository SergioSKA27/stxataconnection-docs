import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide",
initial_sidebar_state="collapsed", page_title="Streamlit Xata Connection", page_icon="🦋")

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


st.markdown('''
<h1 style="font-family:Courier; text-align:center;">Streamlit Xata Data Base Connection
</h1>
''',unsafe_allow_html=True)
#<img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" width="100" height="50" align-items="center"/>

st.caption('By: Sergio Demis Lopez Martinez')
st.divider()

st.markdown('''
<h1 style="font-family:Courier; text-align:center;padding-bottom:0px;">Xata and Streamlit </h1>
<h2 style="font-family:Courier; text-align:center;">A Dynamic Duo for Building Powerful Web Applications</h2>
''', unsafe_allow_html=True)

st.markdown('''
<div style="text-align:center;padding-top:1rem">
In the realm of web development, the combination of Xata and Streamlit is nothing short of a dream team. Xata,
with its schemaless relational SQL database and simple REST API, provides a flexible and scalable foundation for storing
and managing data. Streamlit, on the other hand, is an open-source framework that empowers developers to create
interactive web applications with minimal effort. Together, they form a synergistic partnership that unlocks a world of
possibilities for building sophisticated web applications.
</div>


---

''' ,unsafe_allow_html=True)


st.markdown('''
### Xata: The Flexible and Scalable Data Storage Solution

<div style="text-align:justify">
Imagine a database that can effortlessly adapt to your evolving needs, without the constraints of a rigid schema.
Xata.io brings this vision to life, allowing you to add, remove, and modify columns on the fly. This flexibility makes
it an ideal choice for applications that require frequent changes or those that deal with diverse data types.
</div>

<div style="text-align:justify;padding-bottom:10px">
Furthermore, Xata's scalability ensures that your application can handle even the most demanding workloads.
Its cloud-based architecture can seamlessly scale up or down as your data grows or shrinks, ensuring optimal performance at all times.
<br>
</div>

''',unsafe_allow_html=True)


st.markdown('''

### The <b>st_xatadb_connection</b> Package: Simplifying the Integration Process

<div style="text-align:justify">
To further enhance the synergy between Xata and Streamlit, I've created the <b>st_xatadb_connection</b> package.
This package provides a seamless bridge between the two tools, making it incredibly easy to connect your Streamlit
application to your Xata database.
</div>

<div style="text-align:justify;padding-bottom:10px">
With just a few lines of code, you can perform CRUD operations (create, retrieve, update, delete) on your Xata data,
generate reports and visualizations, and even interact with your data in real time.
The <b>st_xatadb_connection</b> package takes care of all the heavy lifting, allowing you to focus on building your application's functionality.
</div>

##### The Simplicity of <b>st_xatadb_connection</b>: Building Apps with Xata and Streamlit

<div style="text-align:justify">
<b>st_xatadb_connection</b> is the ultimate game-changer for developers looking to build data-driven web applications with
Xata and Streamlit. Its intuitive API and powerful features make it a breeze to connect to your Xata database and
start working with your data.
</div>

With <b>st_xatadb_connection</b>, you can:

- Set your Xata credentials securely in Streamlit's secrets manager or environment variables.

- Connect to your Xata database with a single line of code.

- Query your Xata.io tables with ease using a familiar SQL-like syntax.

- Display your query results in Streamlit with just a few clicks.

Here's a sneak peek into how incredibly simple it is to use <b>st_xatadb_connection</b>:

</div>''' ,unsafe_allow_html=True)


st.code("""
import streamlit as st
from st_xatadb_connection import XataConnection

# Connect to your Xata.io database
xata = st.connection('xata', type=XataConnection)

# Query your 'Table' table
results = xata.query("Table")

# Display the query results in your Streamlit app
st.write(results)
""",language='python')


st.markdown('''
That's it! With just a few lines of code, you've created a fully functional web application that displays data from your Xatadatabase.

Benefits of using <b>st_xatadb_connection</b>:

- Effortless Setup: <b>st_xatadb_connection</b>'s intuitive API makes it incredibly easy to set up and configure.
You can connect to your Xata.io database and start querying your data in minutes.

- Seamless Integration: <b>st_xatadb_connection</b> integrates seamlessly with Streamlit, allowing you to effortlessly display
your query results in interactive visualizations and dashboards.

- Accelerated Development: <b>st_xatadb_connection</b>'s streamlined API and pre-built functions enable rapid development,
saving you valuable time and effort.

<div style="text-align:justify">
<b>st_xatadb_connection</b> is the key to unlocking the full potential of Xata and Streamlit. With its user-friendly
interface and robust capabilities, it's the perfect tool for building data-driven web applications that are both
powerful and easy to use.
</div>

<div style="text-align:center;font-family: Courier">
Experience the simplicity and efficiency of <b>st_xatadb_connection</b> firsthand. Try it out today and see how effortlessly
you can build amazing web applications with Xata and Streamlit!
</div>
''' ,unsafe_allow_html=True)



st.markdown('''
---

<h1 style="text-align:center;font-family: Courier">
Xata Free is a Free Cloud Database!
</h1>

This cloud-based database offers an impressive array of features, all available for free:

 **10 Database Branches**: Xata allows you to create and maintain up to 10 database branches, enabling you to experiment
with different schemas and data structures without affecting your production data.

- **15 GB of Free Storage**: Xata provides a generous 15 GB of storage space for your data, allowing you to store a
substantial amount of in-formation without worrying about exceeding limits.

- **15 GB of Search Engine Storage**: Xata also offers 15 GB of dedicated storage for its powerful search engine.
This ensures that your data is indexed and easily searchable, making it a breeze to find the information you need.

- **2GB File Attachments**: Xata allows you to attach files of up to 2GB in size to your database records.
This makes it easy to store images, documents, and other binary data alongside your structured data.

- **250 AI Queries Per Month**: Xata provides a generous quota of 250 AI queries per month,
enabling you to leverage artificial intelligence to extract insights from your data.


With all these features available for free, Xata is the perfect choice for startups, individual developers,
and anyone looking for a powerful and cost-effective database solution.

For more information about Xata Free and its features, visit the [Xata](https://xata.io/pricing/) page
<div style="text-align:center;font-family: Courier">
Join the growing community of developers who have chosen Xata as their trusted database partner.
Unleash your creativity and build amazing things with Xata!
</div>
''',unsafe_allow_html=True)



st.markdown('''
### Unleashing Your Creativity with Xata and Streamlit
<div style="text-align:justify">
The possibilities are endless when you combine the power of Xata and Streamlit, amplified by the <b>st_xatadb_connection</b>
package. Whether you're building a customer relationship management (CRM) system, a data visualization dashboard, or a
real-time monitoring application, this dynamic duo has you covered.

So, let your creativity soar and embark on your next web development project with confidence, knowing that Xata
and Streamlit will be your trusty companions every step of the way.
''',unsafe_allow_html=True)

cols = st.columns([0.3,0.4,0.3])

if cols[1].button('🚀 Get Started with Xata and Streamlit',use_container_width=True):
    switch_page("Getting_Started")

st.markdown('''
### Check Out the Demo Apps Below to See <b>st_xatadb_connection</b> in Action!

- [Simple Gallery App](https://st-gallery-xata-demo.streamlit.app/)

- [Personal Cloud Storage App](https://st-xata-personal-cloud-demo.streamlit.app/)
''',unsafe_allow_html=True)


st.divider()
