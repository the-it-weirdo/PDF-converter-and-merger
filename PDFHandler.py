from PyPDF2 import PdfFileMerger
import img2pdf

class PDFHandler:

    def append_pdfs(self, pdf_list):
        print(f"Given {len(pdf_list)} to append...")
        appender = PdfFileMerger()
        for idx, pdf in enumerate(pdf_list):
            print(f"Processing file: {idx+1}..")
            try:
                appender.append(open(pdf, 'rb'))
            except Exception as e:
                print(f"Couldn't process {pdf}. Error: {e}")
        print("Processing complete.")
        return appender

    def convert_to_pdf(self, files, type):
        types = {
            'image': self.__img_to_pdf__,
        }
        function = types.get(type)
        return function(files)


    def __img_to_pdf__(self, files):
        print(f"Given {len(files)} to convert...")
        try:
            print("Converting...")
            return img2pdf.convert(files)
        except Exception as e:
            print(f"Error occured: {e}")