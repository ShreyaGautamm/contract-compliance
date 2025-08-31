import streamlit as st
from parsers import parse_file
from utils import split_text, check_risks
from agents import process_contract
import pandas as pd

# Page config
st.set_page_config(
    page_title="Contract Compliance Dashboard",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Contract Review & Compliance Automation")
st.markdown("Upload contracts to analyze clauses, detect risks, and generate summaries in real time.")

# File upload
uploaded_file = st.file_uploader("Upload a contract (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("Parsing contract..."):
        text = parse_file(uploaded_file)
    st.success("✅ Contract parsed successfully!")

    # Split and process
    with st.spinner("Processing contract with multi-agent workflow..."):
        text_chunks = split_text(text)
        results = process_contract(text_chunks)
    st.success("✅ Contract analysis complete!")

    # Compute overall metrics
    total_flags = sum(len(r["risks"]) for r in results)
    total_chunks = len(results)

    st.metric("Total Chunks Processed", total_chunks)
    st.metric("Total Risk Flags Detected", total_flags)

    # Prepare data for download
    export_data = []
    for i, r in enumerate(results):
        export_data.append({
            "Chunk": i+1,
            "Summary": r["summary"],
            "Clauses": r["clauses"],
            "Risks": ", ".join(r["risks"])
        })
    df_export = pd.DataFrame(export_data)
    st.download_button("📥 Download Analysis CSV", df_export.to_csv(index=False), "contract_analysis.csv", "text/csv")

    # Tabs for viewing
    tabs = st.tabs(["Summary", "Clauses", "Risk Overview", "Full Text"])

    # --- SUMMARY TAB ---
    with tabs[0]:
        st.subheader("Contract Summaries")
        for i, r in enumerate(results):
            with st.expander(f"Chunk {i+1} Summary"):
                st.write(r["summary"])

    # --- CLAUSES TAB ---
    with tabs[1]:
        st.subheader("Identified Clauses")
        for i, r in enumerate(results):
            with st.expander(f"Chunk {i+1} Clauses"):
                st.write(r["clauses"])

    # --- RISK OVERVIEW TAB ---
    with tabs[2]:
        st.subheader("Risk Flags Overview")
        for i, r in enumerate(results):
            if r["risks"]:
                st.markdown(f"**Chunk {i+1}:**")
                # Highlight each risk inline
                highlighted = r["text"]
                for risk in r["risks"]:
                    highlighted = highlighted.replace(
                        risk,
                        f"<span style='color:red;font-weight:bold'>{risk}</span>"
                    )
                st.markdown(highlighted, unsafe_allow_html=True)
            else:
                st.markdown(f"**Chunk {i+1}:** No risks detected ✅")

    # --- FULL TEXT TAB ---
    with tabs[3]:
        st.subheader("Full Contract Text")
        st.text_area("Raw Contract Text", text, height=400)

    st.success("✅ Analysis complete! Expand sections to explore summaries, clauses, and risk highlights.")
