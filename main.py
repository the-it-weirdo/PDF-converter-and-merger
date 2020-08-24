from InputHandler import *
from FileManager import *
from PDFHandler import *
from Utilities import *



def __handle_pdf__():
    all_pdfs = fileManager.list_files(base_path, '.pdf')
    output.info(f"Found {len(all_pdfs)} PDFs in directory: {base_path}.")
    if len(all_pdfs) > 0:
        selected = inputHandler.select_files(list(all_pdfs.keys()))
        selected = {key: all_pdfs.get(key) for key in selected}
        appender = pdfHandler.append_pdfs(sorted(list(selected.values())))
        output.info(f"Total pages after appending: {len(appender.pages)}")
        if len(appender.pages) > 0:
            outfilename = input('Enter output filename: ')
            with open(outfilename+'.pdf', 'wb') as fout:
                appender.write(fout)
                output.success(f"PDF Merge complete. Output: ./{outfilename}.pdf")
        else:
            output.error("No pages to append.")


def __handle_image__():
    all_images = {**fileManager.list_files(base_path, '.jpg'), **fileManager.list_files(base_path, '.jpeg'), **fileManager.list_files(base_path, '.png')}
    output.info(f"Found {len(all_images)} images in directory: {base_path}.")
    if len(all_images) > 0:
        selected = inputHandler.select_files(list(all_images.keys()))
        selected = {key: all_images.get(key) for key in selected}
        try:
            for item in selected:
                output.info(f"Converting {item}...")
                converted_image = pdfHandler.convert_to_pdf(selected.get(item), 'image')
                if converted_image is not None:
                    outfilename = item.split('.')[0]
                    with open(outfilename+'.pdf', 'wb') as fout:
                        fout.write(converted_image)
                    output.success(f"Image conversion complete. Output: ./{outfilename}.pdf")
                    # pdf_images = pdfHandler.convert_to_pdf(sorted(list(selected.values())), 'image') # for all images in a single pdf.
                else:
                    output.error(f"Failed to convert {item}.")
        except Exception as e:
            output.error(f"Some unexpected error occurred. Error: {e}")
            return
        

def __handle_quit__():
    raise SystemExit('Quitting..')


base_path = ''
inputHandler = InputHandler()
fileManager = FileManager()
pdfHandler = PDFHandler()
output = TerminalOutput()



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
                output.error('Invalid path.')
    function()
    base_path = ''
