import json
from file import File
from visitor import Visitor
from logger import logger
from utils import convert_para_into_list_of_lines, validate_json

class VisitorService():

    VISITOR_STORE_FILENAME = 'visitor_data.json'

    def __init__(self):
        pass

    def read_all_visitors_from_file(self):
        all_visitors = []
        visitor_store_file = File(self.VISITOR_STORE_FILENAME)

        file_contents = visitor_store_file.contents()

        if not file_contents:
            print('No visitors in the record')
        elif validate_json(file_contents):
            visitor_store_file.open('r')
            saved_dict = json.loads(visitor_store_file.contents())
            all_visitors = saved_dict['visitors']

        self.visitors = all_visitors
            

    def add_new_visitor(self, gate_no, name, id, purpose, person_to_meet):

        visitor = Visitor(gate_no, name, id, purpose, person_to_meet)

        # Save visitor to the record.
        visitor.save()

        # Show success message.
        logger.log(f'Visitor with id {visitor.id} added')

    def get_visitor_by_id(self, visitor_id):
        self.read_all_visitors_from_file()

        for visitor in self.visitors:
            if visitor['id'] == visitor_id:
                return self.get_visitor_instance_from_dict(visitor)
        
        return None

    def get_visitor_instance_from_dict(self, visitor_dict):
        return Visitor(**visitor_dict)

    def print_summary(self):
        visitor_store_file = File(self.VISITOR_STORE_FILENAME)

        file_contents = visitor_store_file.contents()
        print(file_contents)

visitor_service = VisitorService()
