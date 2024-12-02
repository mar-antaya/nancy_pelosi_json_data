import csv, json, zipfile 
import requests, PyPDF2, fitz

zip_file_url = 'https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2024FD.zip'

#periodic transaction report 2024
pdf_file_url = 'https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2024/'

r = requests.get(zip_file_url)
zipfile_name = '2024.zip'

#opening the zip file 
with open(zipfile_name, 'wb') as f: 
    f.write(r.content)
    
#extracting what is inside of the zipfile
with zipfile.ZipFile(zipfile_name) as a:
    a.extractall('.')

#reading and opening the text with only Nancy hehe
with open('2024FD.txt') as f:
    for line in csv.reader(f, delimiter='\t'):
        print(line)
        if line[1] == 'Pelosi':
            dt = line[7]
            doc_id = line[8]

            r = requests.get(f"{pdf_file_url}{doc_id}.pdf")

            with open(f"{doc_id}.pdf", 'wb') as pdf_file:
                pdf_file.write(r.content)
                doc = fitz.open(f"{doc_id}.pdf")
                page = doc.load_page(page_id=0)
                json_data = page.get_text('json')

                print(json_data)

