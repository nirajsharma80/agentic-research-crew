import os
import streamlit as st
from crew import run_research

st.set_page_config(page_title="Signal Crew | Research studio",page_icon="✳",layout="wide")
st.title("✳ Signal Crew")
st.caption("A small, role-based research crew that searches, compares, and briefs a topic.")
with st.sidebar:
    st.subheader("Connections")
    st.write("Google AI key: " + ("ready" if os.getenv("GOOGLE_API_KEY") else "missing"))
    st.write("Serper search key: " + ("ready" if os.getenv("SERPER_API_KEY") else "missing"))
    st.caption("Keys are read from the process environment and are never stored by the app.")
topic=st.text_area("Research question",placeholder="How are smaller retailers using computer vision for inventory management?",height=100)
angle=st.text_input("Audience or angle",value="A product manager evaluating practical opportunities")
if st.button("Run the crew",type="primary"):
    if not topic.strip(): st.warning("Enter a research question first.")
    elif not os.getenv("GOOGLE_API_KEY") or not os.getenv("SERPER_API_KEY"): st.error("Set GOOGLE_API_KEY and SERPER_API_KEY before running the crew.")
    else:
        with st.spinner("The researcher and analyst are working..."):
            try: result=run_research(topic.strip(),angle.strip())
            except Exception as exc: st.error(f"Research run failed: {exc}"); st.stop()
        st.markdown(result)
        st.download_button("Download brief",result,file_name="research-brief.md",mime="text/markdown")
