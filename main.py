#pip3 install PyMuPDF

import fitz  # this is pymupdf

with fitz.open("example.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)
