class LastLowGetter:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_lastlow(self):
        lastrow = sum(1 for i in open(self.file_path))
        print(lastrow)
        return lastrow