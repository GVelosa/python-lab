#Reading
from pypdf import PdfReader

#Initializing the PDF reader
report = PdfReader("src/pdfs/relatorio_de_vendas.pdf")
# print(len(report.pages))

#Passing one page
page_1 = report.pages[0]
text = page_1.extract_text()
print(text)

#A simple visualizer of the content
# for i in report.pages:
#     print(i.extract_text())

report.close() #This part is important to ensure no conflict.

#-------------------------------------------------------------#

