import os, json, tempfile
import streamlit as st
import snowflake.snowpark as snowpark

st.set_page_config(
    page_title="Not Hotdog",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    body {
        background-color: #000;
    }
    .stApp {
        background-color: #000;
        color: white;
        text-align: center;
    }
    .result-hotdog {
        color: #00FF00;
        font-size: 4em;
        font-weight: bold;
    }
    .result-nothotdog {
        color: red;
        font-size: 4em;
        font-weight: bold;
    }
    .description {
        font-size: 1.5em;
        margin-top: 1.5em;
        color: #ccc;
    }
    [data-testid="stCameraInput"] video {
        width: 100% !important;
        height: auto !important;
    }
    unsafe_allow_html=True
    
    </style>
""", unsafe_allow_html=True)

with st.container():
    pic = st.camera_input("")
    if not pic: st.stop()


with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
    tmp.write(pic.getvalue())
    tmp.flush()
    path = tmp.name

session = snowpark.Session.builder.getOrCreate()
session.file.put(path, "@IMAGES", overwrite=False, auto_compress=False)

files = session.sql("LIST @IMAGES").collect()
name = os.path.basename(path)
stage_file = next((f.name for f in files if f.name.endswith(name)), None)
if not stage_file: st.stop()

# Ask two things: hotdog or not + what is in the image
prompt = """
1. Does this image contain a hot dog? Answer with JSON like: { "hotdog": true|false }
2. What is in the image? Respond with JSON key "description" and a short description.
Return only one combined JSON like:
{ "hotdog": true, "description": "a hot dog in a paper tray with mustard" }
"""

sql = f"""
SELECT SNOWFLAKE.CORTEX.COMPLETE(
  'claude-3-5-sonnet',
  $$ {prompt} $$,
  TO_FILE('@IMAGES', '{stage_file.split('/',1)[-1]}')
)
"""

try:
    result = json.loads(session.sql(sql).collect()[0][0])
    if result.get("hotdog"):
        st.markdown("<div class='result-hotdog'>🌭 HOT DOG</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-nothotdog'>🚫 NOT HOT DOG</div>", unsafe_allow_html=True)

    if "description" in result:
        st.markdown(f"<div class='description'>Detected: {result['description'].capitalize()}</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"❌ Unexpected response or error: {e}")
