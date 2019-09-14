class OpenFile:

    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.f = open(self.file, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
