from PyPDF2 import PdfFileMerger
import img2pdf
import os
from Utilities import *

output = TerminalOutput()

class PDFHandler:

    def append_pdfs(self, pdf_list):
        output.info(f"Given {len(pdf_list)} to append...")
        appender = PdfFileMerger()
        for pdf in pdf_list:
            output.info(f"Processing file: {pdf.split(os.path.sep)[-1]}..")
            try:
                appender.append(open(pdf, 'rb'))
                output.success(f"{pdf.split(os.path.sep)[-1]} processed.")
            except Exception as e:
                output.warn(f"Couldn't process {pdf}. Error: {e}")
        return appender

    def convert_to_pdf(self, files, type):
        types = {
            'image': self.__img_to_pdf__,
        }    
        function = types.get(type)
        if function is not None:
            return function(files)


    def __img_to_pdf__(self, files):
        # print(f"Given {len(files)} to convert...")
        try:
            return img2pdf.convert(files)
        except Exception as e:
            output.warn(f"Error occured: {e}")
            return None