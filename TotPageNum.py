
# this is simply my laziness manifesting in everything that I do - huh! 

import os
from PyPDF2 import PdfReader

def get_total_pdf_pages(directory):
  total_pages = 0

  # Iterate through all the files in the directory
  for filename in os.listdir(directory):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
      # Open the PDF file
      with open(os.path.join(directory, filename), 'rb') as f:
        # Create a PdfFileReader object
        pdf_reader = PdfReader(f)
        # Get the number of pages in the PDF
        num_pages =  len(pdf_reader.pages)
        # Add the number of pages to the total
        total_pages += num_pages

  # Return the total number of pages
  return total_pages



current_directory = os.getcwd()
total_pages = int(get_total_pdf_pages(current_directory))

per_min = round(float(total_pages/(900)), 2)

print("\nTotal Number of pages you need to suck - "+str(total_pages)+"\n")
print("If I want to finish it by tonight, I need to read "+str(per_min)+" pages per minute, which is "+str(round((1/per_min),2))+" minutes per page\n")
