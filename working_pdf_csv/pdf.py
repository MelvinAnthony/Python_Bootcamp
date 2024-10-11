import PyPDF2

# PDF reader
# file_open = open("Some_new_file.pdf", "rb")

# # Updated for newer PyPDF2 versions
# pdf_reader = PyPDF2.PdfReader(file_open)

# # Printing the number of pages
# print(len(pdf_reader.pages))

# # Extracting text from the first page
# page_one = pdf_reader.pages[0]  # Use pages[] instead of getPage()
# page_one_text = page_one.extract_text()
# print(page_one_text)

# file_open.close()

# PDF writer
file_open = open("Some_new_file.pdf", "rb")
# Updated for newer PyPDF2 versions
pdf_reader = PyPDF2.PdfReader(file_open)

# Get the first page
first_page = pdf_reader.pages[0]

# Create a PdfWriter object
pdf_writer = PyPDF2.PdfWriter()

# Add the first page to the writer
pdf_writer.add_page(first_page)

# Write the new PDF to a file
with open("new_pdf_after_change.pdf", "wb") as pdf_output:
    pdf_writer.write(pdf_output)

file_open.close()
