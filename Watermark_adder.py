import PyPDF2
import sys

input_pdf = sys.argv[1]
water_pdf = sys.argv[2]
wtr = open(water_pdf,'rb')
wtrPdf = PyPDF2.PdfFileReader(wtr)
wtrPage = wtrPdf.getPage(0)

file=open(input_pdf, 'rb')
InPdf = PyPDF2.PdfFileReader(file)
Output = PyPDF2.PdfFileWriter()
total_pages = InPdf.getNumPages()
for i in range(0,total_pages):
    InPdfPage = InPdf.getPage(i)
    InPdfPage.mergePage(wtrPage)
    Output.addPage(InPdfPage)

with open('waterMarkerPdf.pdf','wb') as outputFile:
    Output.write(outputFile)

file.close()
wtr.close()