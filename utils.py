import json

def get_user_input(msg='', accept_int=False):

        user_input = None

        valid_input = False

        while not valid_input:
            try:
                user_input = int(input(msg)) if accept_int else input(msg)
            except ValueError:
                print('please provide a integer value')
            else:
                valid_input = True
                break

        return user_input
        
def convert_para_into_list_of_lines(paragraph):
    return paragraph.split('\n')
    
def validate_json(json_string):
    try:
        json.loads(json_string)
    except ValueError:
        return False
    else:
        return True
