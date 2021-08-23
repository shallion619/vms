from file import File
from visitor import Visitor
from logger import logger
from utils import convert_para_into_list_of_lines

class VisitorService():

    VISITOR_STORE_FILENAME = 'visitor_data.txt'

    def __init__(self):
        pass

    def read_all_visitors_from_file(self):
        visitor_store_file = File(self.VISITOR_STORE_FILENAME)

        visitor_store_file.open()

        list_of_visitors_data = convert_para_into_list_of_lines(
            visitor_store_file.contents())

        list_of_visitors_in_object_form = self.data_line_list_to_visitor_object_list(
            list_of_visitors_data)

        self.visitors = list_of_visitors_in_object_form
        
    def data_line_list_to_visitor_object_list(self, list_of_data_lines):
        list_of_objects = []
        for line in list_of_data_lines:
            data_units = line.split(', ')
            list_of_objects.append(Visitor(
                int(data_units[0]), data_units[1], data_units[2],
                data_units[3], data_units[4]))     

        return list_of_objects       

    def add_new_visitor(self, gate_no, name, purpose, person_to_meet):

        visitor = Visitor(gate_no, name, id, purpose, person_to_meet)

        # Save visitor to the record.
        visitor.save()

        # Show success message.
        logger.log(f'Visitor with id {visitor.id} added')

    def get_visitor_by_id(self, visitor_id):
        self.read_all_visitors_from_file()

        for visitor in self.visitors:
            if visitor.id == visitor_id:
                return visitor
        
        return None


visitor_service = VisitorService()
