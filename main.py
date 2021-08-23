
from utils import get_user_input
from visitor import Visitor

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
            
    def add_new_visitor(self):
        gate_no = get_user_input('Please provide gate no : ', True)
        name = get_user_input('Please provide name : ')
        id = get_user_input('Please provide id : ')
        purpose = get_user_input('Please provide purpose : ')
        person_to_meet = get_user_input('Please provide person to meet : ')
        visitor = Visitor(gate_no, name, id, purpose, person_to_meet)

        # Save visitor to the record.
        visitor.save()


if __name__ == '__main__':
    vms = VisitorManagementSystem()
    try:
        print('Visitor Management System')
        while True:

            vms.show_commands_to_user()
            vms.get_user_command()
            
            vms.process_user_command()

    
    except KeyboardInterrupt:
        print('Shutting down the visitor management system')

    vms.show_commands_to_user()
