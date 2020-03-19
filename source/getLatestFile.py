import glob
import os

class 

list_of_files = glob.glob('/path/to/folder/*')
latest_file = max(list_of_files, key=os.path.getctime)