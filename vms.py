
from utils import get_user_input
from visitor_service import visitor_service

class VisitorManagementSystem():

    def __init__(self):
        pass

    def show_commands_to_user(self):
        print('1. Accept a new visitor')
        print('2. Book Visitor')
        print('3. Check Visitor Appointment')
        print('4. Print Summary')

    def get_user_command(self):
        self.user_command = get_user_input(
            'Please provide command number',
            True
        )

    def process_user_command(self):
        if self.user_command == 1:
            self.add_new_visitor()
        elif self.user_command == 2:
            self.book_visitor()
            
    def add_new_visitor(self):
        gate_no = get_user_input('Please provide gate no : ', True)
        name = get_user_input('Please provide name : ')
        id = get_user_input('Please provide id : ')
        purpose = get_user_input('Please provide purpose : ')
        person_to_meet = get_user_input('Please provide person to meet : ')

        visitor_service.add_new_visitor(gate_no, name, id, purpose, person_to_meet)


    def book_visitor(self):
        visitor_id = get_user_input('Please provide visitor id :')
        
        visitor = visitor_service.get_visitor_by_id(visitor_id)

        if visitor:
            print(visitor.name)
            visitor.book()
        else:
            print(f'No visitor found with id {visitor_id}')

