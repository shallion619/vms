
from file_handler_service import FileHandlerService

import json

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

    def close(self):
        self.file.close()                  

    def write(self, contents):
        if contents:
            self.file_handler_service.write_to_file(self.file, contents)

    def write_line(self, contents):
        self.write(contents + '\n')

    def dump_json(self, json_data):
        self.open('w')
        json.dump(json_data, self.file, indent=4, sort_keys=True)
        self.close()

    def contents(self):
        self.open('r')

        contents = ''

        for line in self.file:
            contents += line

        self.close()

        return contents
