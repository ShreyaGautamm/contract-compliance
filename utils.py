from langchain.text_splitter import CharacterTextSplitter

# Example risk rules
RISK_KEYWORDS = [
    "penalty",
    "indemnity",
    "late fee",
    "termination",
    "liability",
]

def split_text(text, chunk_size=1000, overlap=100):
    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)

def check_risks(text_chunk):
    flagged = []
    for keyword in RISK_KEYWORDS:
        if keyword.lower() in text_chunk.lower():
            flagged.append(keyword)
    return flagged
