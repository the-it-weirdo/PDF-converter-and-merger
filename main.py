from InputHandler import *
from FileManager import *
from PDFHandler import *


def __handle_pdf__():
    all_pdfs = fileManager.list_files(base_path, '.pdf')
    print(f"Found {len(all_pdfs)} PDFs in directory: {base_path}.")
    if len(all_pdfs) > 0:
        selected = inputHandler.select_files(list(all_pdfs.keys()))
        selected = {key: all_pdfs.get(key) for key in selected}
        appender = pdfHandler.append_pdfs(sorted(list(selected.values())))
        print(f"Total pages after appending: {len(appender.pages)}")
        if len(appender.pages) > 0:
            outfilename = input('Enter output filename: ')
            with open(outfilename+'.pdf', 'wb') as fout:
                appender.write(fout)
                print(f"PDF Merge complete. Output: ./{outfilename}.pdf")
        else:
            print("No pages to append.")


def __handle_image__():
    all_images = {**fileManager.list_files(base_path, '.jpg'), **fileManager.list_files(base_path, '.jpeg'), **fileManager.list_files(base_path, '.png')}
    print(f"Found {len(all_images)} PDFs in directory: {base_path}.")
    if len(all_images) > 0:
        selected = inputHandler.select_files(list(all_images.keys()))
        selected = {key: all_images.get(key) for key in selected}
        try:
            pdf_images = pdfHandler.convert_to_pdf(sorted(list(selected.values())), 'image')
            outfilename = input('Enter output filename: ')
            with open(outfilename+'.pdf', 'wb') as fout:
                fout.write(pdf_images)
                print(f"Image conversion complete. Output: ./{outfilename}.pdf")
        except:
            return
        

def __handle_quit__():
    raise SystemExit('Quitting..')


base_path = ''
inputHandler = InputHandler()
fileManager = FileManager()
pdfHandler = PDFHandler()



while(True):
    switcher = {
        'Merge PDFs': __handle_pdf__,
        'Convert Image to PDF': __handle_image__,
        'Quit': __handle_quit__
    }
    name = {
        __handle_pdf__: 'PDFs',
        __handle_image__: 'Images'
    }
    options = list(switcher.keys())
    function = switcher.get(inputHandler.menu(options))
    if not function == __handle_quit__:
        while not base_path:
            base_path = input(f'Enter directory path for {name.get(function)}: ')
            if fileManager.is_path_exists(base_path) == False:
                base_path = ''
                print('Invalid path.')
    function()
    base_path = ''
