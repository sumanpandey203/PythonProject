import PyPDF2

pdfFileObj = open(r'C:\Users\suman.pandey\Desktop\My_work\Drehmomentberechnung\2D_Interpolation_Ld.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())