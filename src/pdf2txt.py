import PyPDF2
import os

def pdf_to_text(pdf_file, txt_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Convert PDF to text
pdf_to_text('guide_1.pdf', 'guide_1.txt')
pdf_to_text('guide_2.pdf', 'guide_2.txt')
pdf_to_text('guide_3.pdf', 'guide_3.txt')

def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"File {file_path} has been successfully generated.")
    else:
        print(f"Warning: File {file_path} not found.")

# Check if generated txt files exist
check_file_exists('guide_1.txt')
check_file_exists('guide_2.txt')
check_file_exists('guide_3.txt')
