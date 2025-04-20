import os, json, tempfile, streamlit as st
from snowflake.snowpark import Session

st.set_page_config(page_title="Not Hotdog", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>body,.stApp{background:#000;color:#fff;text-align:center}
.result-hotdog{color:#0F0;font-size:4em;font-weight:700}
.result-nothotdog{color:red;font-size:4em;font-weight:700}</style>""", unsafe_allow_html=True)

if not (pic := st.camera_input("")): st.stop()
with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f: f.write(pic.getvalue()); path = f.name

s = Session.builder.getOrCreate()
s.file.put(path, "@IMAGES", overwrite=False, auto_compress=False)
f = next((x.name for x in s.sql("list @IMAGES").collect() if x.name.endswith(os.path.basename(path))), None)
if not f: st.stop()

p = """1. Does this image contain a hot dog? Answer: { "hotdog": true|false }
2. What is in the image? Use key "description". Return one JSON like:
{ "hotdog": true, "description": "a hot dog with mustard on a plate" }"""

q = f"select snowflake.cortex.complete('claude-3-5-sonnet', $$ {p} $$, to_file('@IMAGES','{f.split('/',1)[-1]}'))"
try:
    r = json.loads(s.sql(q).collect()[0][0])
    c, t = ("result-hotdog", "🌭 HOT DOG") if r.get("hotdog") else ("result-nothotdog", "🚫 NOT HOT DOG")
    st.markdown(f"<div class='{c}'>{t}</div>", unsafe_allow_html=True)
    if d := r.get("description"): st.markdown(f"<div style='margin-top:1em;font-size:1.3em;color:#ccc'>Detected: {d.capitalize()}</div>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"❌ Error: {e}")
