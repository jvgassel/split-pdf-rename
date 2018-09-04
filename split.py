from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("report.pdf", "rb"))

with open('regcode.txt') as f:
    lines = [line.rstrip('\n') for line in open('regcode.txt')]
	
output = PdfFileWriter()
for j in range(inputpdf.numPages):
	output = PdfFileWriter()
	output.addPage(inputpdf.getPage(j))
	outputStream = file(lines[j] + ".pdf", "wb")
	output.write(outputStream)
