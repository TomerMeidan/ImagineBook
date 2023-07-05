import fitz
import os


def get_pdf_text(file_path):
    # Open the PDF file
    pdf_doc = fitz.open(file_path)

    # Initialize an empty string to store the extracted text
    extracted_text = ""

    # Iterate over the pages and append the text to the extracted_text string
    for page_num, page in enumerate(pdf_doc):
        text = page.get_text()
        extracted_text += text

    # Return the extracted text
    return extracted_text

def get_pdf_file_name(file_path):
    # Return the PDF file name without extension
    return os.path.splitext(os.path.basename(file_path))[0]
