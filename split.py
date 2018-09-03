from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("rapport.pdf", "rb"))

with open('regcode.txt') as f:
    lines = [line.rstrip('\n') for line in open('regcode.txt')]
	
i = 0
while i < len(lines):
	output = PdfFileWriter()
	for j in range(inputpdf.numPages):
		output = PdfFileWriter()
		output.addPage(inputpdf.getPage(i))
		outputStream = file(lines[i] + ".pdf", "wb")
		output.write(outputStream)
	i += 1
