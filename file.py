
from file_handler_service import FileHandlerService

class File():

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handler_service = FileHandlerService()

    def open(self, descriptor='r'):
        try:
            self.file = self.file_handler_service.open_file(self.file_name, descriptor)
        except FileNotFoundError:
            self.file_handler_service.create_file(self.file_name)
            self.file = self.file_handler_service.open_file(self.file_name, descriptor)                        

    def write(self, contents):
        if contents:
            self.file_handler_service.write_to_file(self.file, contents)

    def write_line(self, contents):
        self.write(contents + '\n')

    def contents(self):
        contents = ''

        for line in self.file:
            contents += line

        return contents
