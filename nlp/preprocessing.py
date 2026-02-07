import re

def preprocess(text):
    # lowercase (safe for sinhala + english mix)
    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # tokenize (simple)
    tokens = text.split()

    return tokens
