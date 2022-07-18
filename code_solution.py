#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "individual assignment 2"
name = "Florence"
np_email = "s10242888@connect.np.edu.sg"
student_id = "10242888D"
class_number = "WA22"

# The following modules are imported to kickstart your assignment:

# import Path function from pathlib
from pathlib import Path
# import re and csv module
import re, csv

### Tips for the assignment ###

# 1. Set file paths to pfb_ind_assign2 folder for reading and writing files.
# 2. Create search pattern for rental, address, flat type and date
# 3. Iterate over tenancy documents 
     # For each file open as read mode:
          ## 3.1 search and return rental, address flat type and dates
          ## 3.2 clean up the extracted data 
          ## 3.3 for each matched item, append to tenancy.csv

# create a path object in the current working directory
file_path = Path.cwd()/"pfb_ind_assign2"
# create a new file in pfb_ind_assign2 folder
file_path2 = Path.cwd()/"pfb_ind_assign2"/"tenancy.csv"
file_path2.touch()

# create a list for the headers of extracted datas
headers = ["ADDRESS", "FLAT TYPE", "START DATE", "END DATE", "RENTAL RATE"]

# open file using 'with' and 'open' keywords in 'write' mode
# include another parameter (newline="") to prevent an extra line being added in the csv file
with file_path2.open(mode="w", encoding="UTF-8", newline="") as file:
     # create a writer object and named it as 'writer' variable, use 'csv.writer(file)'
     writer = csv.writer(file)
     # use '.writerow()' to write headers
     writer.writerow(headers)

# iterate over the path object using a for loop
# glob("*.txt") method is used to search any files with txt extension
for file in file_path.glob("*.txt"):
     # open each txt file in read mode
     with file.open(mode="r", encoding="UTF-8") as file:
          # create a text object using read() method from csv module
          text = file.read()
          # use re.findall() as a search function from re module 
          # use basic regex to create search pattern for rental, address, flat type and date in string
          address = re.findall(pattern=r"Block [0-9]+ Unit [0-9][0-9]-[0-9][0-9].+", string=text)
          flat = re.findall(pattern=r"[0-9] ROOM FLAT", string=text)
          rental = re.findall(pattern=r"[A-Z][A-Z][A-Z]+[0-9][0-9][0-9][0-9]", string=text)
          dates = re.findall(pattern=r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", string=text)  
     # use mode="a" to append the datas to csv file
     with file_path2.open(mode="a", encoding="UTF-8", newline="") as file:
          writer = csv.writer(file)
          datas = address+flat+dates+rental
          datas_list = list(datas)
          # user '.writerow()' to write single line and iterate over a for loop
          writer.writerow(datas_list)
