
from file import File
from utils import validate_json

import json



class Visitor():

    VISITOR_STORE_FILENAME = 'visitor_data.json'

    JSON_SCHEMA = {
        'visitors': []
    }

    def __init__(self, gate_no, name, id, purpose, person_to_meet, booked=False):

        self.gate_no = gate_no
        self.name = name
        self.id = id
        self.purpose = purpose
        self.person_to_meet = person_to_meet
        self.booked = booked
        # self.visitor_id = visitor_id


    def save(self):
        visitor_store_file = File(self.VISITOR_STORE_FILENAME)

        file_contents = visitor_store_file.contents()

        if not file_contents:
            # If file is empty, no data is stored there.
            visitor_store_file.dump_json(self.JSON_SCHEMA)

        file_contents = visitor_store_file.contents()

        if validate_json(file_contents):
                visitor_store_file.open('r')
                saved_dict = json.loads(visitor_store_file.contents())
                
                # Add new visitor to dict.
                visitor_dict = {
                    'gate_no': self.gate_no,
                    'name': self.name,
                    'id': self.id,
                    'purpose': self.purpose,
                    'person_to_meet': self.person_to_meet,
                    'booked': self.booked
                }

                updated_dict = False

                for index, visitor in enumerate(saved_dict['visitors']):
                    if visitor['id'] == visitor_dict['id']:
                        saved_dict['visitors'][index].update(visitor_dict)
                        updated_dict = True

                if not updated_dict:
                    saved_dict['visitors'].append(visitor_dict)

                visitor_store_file.dump_json(saved_dict)

        else:
            raise Exception('Invalid file schema: visitor_data.json')
            

    def book(self):
        if self.booked == True:
            print('Visitor is already booked.')
            return

        self.booked = True
        self.save()
