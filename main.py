
from logger import Logger
from vms import VisitorManagementSystem

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
