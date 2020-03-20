import glob
import os

class Gatter:

    def get_lastest_fille(file_path):
        list_of_files = glob.glob('%a/*' file_path)
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file