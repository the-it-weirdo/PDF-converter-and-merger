from PyPDF2 import PdfFileMerger
import os

path = input("Enter directory path: ")
all_pdf = {(idx+1): pdf for idx, pdf in enumerate(f for f in os.listdir(path) if f.endswith('.pdf'))}

print(f"Found {len(all_pdf)} pdf in directory: {path}\n")

# show pdf list
for key in all_pdf.keys():
    print(f"{key}: {all_pdf.get(key)}")

choosen_keys = input("\nChoose PDFs to merge: \nEnter corressponding numbers...\n(seperate by ,) (Enter 'A' to select all): ")
if choosen_keys.upper() == 'A':
    choosen_keys = all_pdf.keys()
else:
    try:
        choosen_keys = list(map(int, choosen_keys.split(',')))
    except:
        print("\nError occurred. Possible Invalid Input.")
        raise SystemExit("Terminating program.")

# show selected pdfs
print("\nSelected PDFs are: \n")
for key in choosen_keys:
    print(f"{key}: {all_pdf.get(key)}")

sure = True if input('\nAre you sure you want to merge them to single pdf? Enter Y if sure, anything otherwise. :').upper() == 'Y' else False

if sure:
    merger = PdfFileMerger()
    for key in choosen_keys:
        pdf = all_pdf.get(key)
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