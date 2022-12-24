# it takes current system time from {datetime} and returns the time to finish a particular pdf (later generalizable to all kinds) file, given the speed to read a page

import os
import datetime
from PyPDF2 import PdfReader
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
# print(f"Hour: {hour}")
# print(f"Minute: {minute}")
# print(f"Second: {second}")
def get_total_pdf_pages(directory, filename):				# my_function_1
  total_pages = 0
  with open(os.path.join(directory, filename), 'rb') as f:
        # Create a PdfFileReader object
        pdf_reader = PdfReader(f)
        # Get the number of pages in the PDF
        num_pages =  len(pdf_reader.pages)

  # Return the total number of pages
  return num_pages
def finishing_time(current_time, needed_hour, needed_min):	# my_function_2
	if ((current_time.minute + needed_min)>=60):
		needed_hour = needed_hour + int((current_time.minute + needed_min)/60)
		needed_min = int((current_time.minute + needed_min)%60)
		net_hour_needed = current_time.hour + needed_hour
		net_residual_minute_needed = needed_min
	else: 
		net_hour_needed = current_time.hour + needed_hour
		net_residual_minute_needed = current_time.minute + needed_min

	return net_hour_needed, net_residual_minute_needed
file_to_summon = input("\nName of the pdf file : ") 
desired_speed = float(input("\nDesired speed (in page per min) : "))
pageNum = int(get_total_pdf_pages(os.getcwd(), file_to_summon+'.pdf'))
total_time = pageNum*desired_speed  # (in Minutes) I am considering 1 min to finish reading a page
total_hour = int(total_time/60)
residual_min = int(total_time%60) 
needed_hour, needed_min = finishing_time(current_time, total_hour, residual_min)
print("\n")
print(f"Need to finish by {needed_hour}:{needed_min}")
print("\n")
