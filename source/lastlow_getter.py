class LastLowGetter:

    def __init__(self, file):
        self.file = file

    def get_lastlow(self):
        lastrow = sum(1 for i in open(self.file))
        print(lastrow)
        return lastrow