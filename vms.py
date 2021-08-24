
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
            'Please provide command number : ',
            True
        )

    def process_user_command(self):
        if self.user_command == 1:
            self.add_new_visitor()
        elif self.user_command == 2:
            self.book_visitor()
        elif self.user_command == 3:
            self.check_entry()
        elif self.user_command == 4:
            self.print_summary()
            
    def add_new_visitor(self):
        gate_no = get_user_input('Please provide gate no : (1,2,3,4 available)', True)
        if not gate_no in range(1,5):
            print('Invalid gate number:')
            self.add_new_visitor()
            return

        name = get_user_input('Please provide name : ')
        id = get_user_input('Please provide id : ')
        purpose = get_user_input('Please provide purpose : ')
        person_to_meet = get_user_input('Please provide person to meet : ')

        visitor_service.add_new_visitor(gate_no, name, id, purpose, person_to_meet)


    def book_visitor(self):
        visitor_id = get_user_input('Please provide visitor id :')
        
        visitor = visitor_service.get_visitor_by_id(visitor_id)

        if visitor:
            visitor.book()
        else:
            print(f'No visitor found with id {visitor_id}')

    def check_entry(self):
        visitor_id = get_user_input('Please provide visitor id :')

        visitor = visitor_service.get_visitor_by_id(visitor_id)

        if not visitor:
            print(f'No visitor with id {visitor_id} found.')

            new_entry = input('Do you want to add new entry? (Yes/No) : ')

            if new_entry.lower() == 'yes':
                self.add_new_visitor()

            return
        
        if visitor.booked:
            print('Entry allowed!')

        else:
            print(f'Visitor with id {visitor_id} is not booked, Entry not allowed')

    def print_summary(self):
        visitor_service.print_summary()
