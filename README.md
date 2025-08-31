# 📜 Contract Review & Compliance Automation  
Welcome to my **Multi-Agent Legal AI Project**! This repository demonstrates how to leverage **LLMs, LangChain, and Streamlit** to automatically review contracts for compliance risks, highlight problematic clauses, and provide summaries in real time.  

- 🤖 Multi-Agent workflow using **LangChain + Ollama**  
- 📑 Upload PDF contracts directly from the app  
- ⚖️ Clause extraction, risk detection, and compliance flagging  
- 🔍 Highlighted risk visualization with structured summaries  
- 🌐 Deployed with **Streamlit** for an interactive demo  

---

## ⚡ Tech Stack & Tools
[![LangChain](https://img.shields.io/badge/-LangChain-1E88E5?style=for-the-badge)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/-Ollama-000000?style=for-the-badge)](https://ollama.ai)
[![Hugging Face](https://img.shields.io/badge/-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![PyPDF2](https://img.shields.io/badge/-PyPDF2-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/pypdf2/)
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

---

## 🧩 Features
1. **Clause Identification Agent**  
   - **Model**: `llama3.2:1b` (lightweight, fast, efficient for extraction tasks).  
   - **Role**: Detects important contract clauses such as:  
     - Termination conditions  
     - Payment obligations  
     - Confidentiality terms  
     - Liability limits  

2. **Risk Assessment Agent**  
   - **Model**: `llama3:latest` (larger, better reasoning for legal context).  
   - **Role**: Evaluates flagged clauses and identifies compliance/legal risks.  
     - Highlights vague terms  
     - Flags high-risk obligations  
     - Maps risks to potential regulatory issues  

3. **Summarization Agent**  
   - **Model**: `llama3.2:1b`  
   - **Role**: Generates a concise, plain-language summary of the contract, focusing on:  
     - Key obligations  
     - Deadlines  
     - Risk hotspots   

---

## 🌐 Deployment
Deployed on **Streamlit Community Cloud** 👉 [Here](https://contract-compliance-fkfhbzh6z9mfaezw8uqmlg.streamlit.app/?embed_options=show_toolbar,show_padding,show_footer,light_theme,show_colored_line,disable_scrolling)  

---

## 📌 Future Improvements
- Integration with **domain-specific legal LLMs** from Hugging Face.  
- Support for **multilingual contracts** (Italian, Spanish, etc.).  
- Export risk reports as **PDF/Excel**.  
- Add a **compliance knowledge base** with regulatory citations.  
