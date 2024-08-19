import PyPDF2

def pdf_to_text(pdf_file, txt_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(text)

# 示例用法
pdf_to_text('guide_1.pdf', 'guide_1.txt')
pdf_to_text('guide_2.pdf', 'guide_2.txt')
pdf_to_text('guide_3.pdf', 'guide_3.txt')