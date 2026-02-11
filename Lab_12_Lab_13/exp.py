from PyPDF2 import PdfReader

# Function to extract headings based on font size and boldness
def extract_headings(pdf_reader):
    headings = []
    for page in pdf_reader.pages:
        content = page.extract_text()
        lines = content.split('\n')
        for line in lines:
            # Check for font size and boldness characteristics of headings
            # Adjust the conditions based on your PDF's actual font sizes and boldness
            if line.strip() and len(line.strip()) > 5:
                headings.append(line.strip())
    return headings

# Open PDF and extract headings
pdf_file = 'EE230_Analog_2024_Lab_12_Homework.pdf'
reader = PdfReader(pdf_file)
headings = extract_headings(reader)

# Print extracted headings
for heading in headings:
    print(heading)
