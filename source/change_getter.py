import linecache

class Getter:
    
    def __init__(self, file_path):
        self.file_path = file_path

    def get_change(self):
        lastrow = sum(1 for i in open(self.file_path))
        target = linecache.getline(self.file_path, int(lastrow)).strip()
        linecache.clearcache()
        return target