import img2pdf
import os

path = input("Enter directory path: ")
all_img = [f for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

print(f"Found {len(all_img)} images in directory: {path}")
sure = True if input('Are you sure you want to convert all of them to pdf? Enter Y if sure, anything otherwise. :').upper() == 'Y' else False

if sure:
    same_pdf = True if input('Merge converted images into single pdf? Enter Y if yes, anything otherwise. :').upper() == 'Y' else False

    if same_pdf:
        all_img = [os.path.join(path, x) for x in all_img]
        outfilename = input('Enter output filename: ')
        with open(os.path.join(path, outfilename+'.pdf'), 'wb') as fout:
            fout.write(img2pdf.convert(all_img))
        
        print(f"Conversion complete. Output file: {os.path.join(path, outfilename+'.pdf')}.")
    else:
        for img in all_img:
            img_file_path = os.path.join(path, img)
            pdf_file_path = img_file_path.split('.')[0]+'.pdf'
            print(f"Converting: {img_file_path}")
            with open(img_file_path, 'rb') as input_file, open(pdf_file_path, 'wb') as output_file:
                output_file.write(img2pdf.convert(input_file))
            print(f"Converted. Ouptut: {pdf_file_path}")
        
        print("Converion Complete. All files converted.")