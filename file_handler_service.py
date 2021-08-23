
class FileHandlerService():

    def __init__(self):
        pass

    def open_file(self, filename, descriptor='r'):
        return open(filename, descriptor)

    def create_file(self, filename):
        self.open_file(filename, 'w')

    def write_to_file(self, file, contents):
        file.write(contents)
