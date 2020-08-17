from PyPDF2 import PdfFileMerger
import os

path = input("Enter directory path: ")
all_pdf = [f for f in os.listdir(path) if f.endswith('.pdf')]

print(f"Found {len(all_pdf)} pdf in directory: {path}")
sure = True if input('Are you sure you want to merge them to single pdf? Enter Y if sure, anything otherwise. :').upper() == 'Y' else False

if sure:
    merger = PdfFileMerger()
    for pdf in all_pdf:
        print(f"Processing file: {pdf}...")
        pdf_path = os.path.join(path, pdf)
        merger.append(open(pdf_path, 'rb'))
    
    outfilename = input('Enter output filename: ')
    outfilename = os.path.join(path, outfilename)
    with open(outfilename+'.pdf', 'wb') as fout:
        merger.write(fout)
    
    print(f'Merge complete. Merged file is {outfilename}.pdf')
else:
    print('Merge operation cancelled.')