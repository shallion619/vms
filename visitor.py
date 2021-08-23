
from file import File

class Visitor():

    VISITOR_STORE_FILENAME = 'visitor_data.txt'

    def __init__(self, gate_no, name, id, purpose, person_to_meet):
        self.gate_no = gate_no
        self.name = name
        self.id = id
        self.purpose = purpose
        self.person_to_meet = person_to_meet
        # self.visitor_id = visitor_id

    def save(self):
        visitor_store_file = File(self.VISITOR_STORE_FILENAME)
        visitor_store_file.open('a')
        visitor_store_file.write_line(
            f'{self.gate_no}, {self.name}, {self.id}, ' + 
            f'{self.purpose}, {self.person_to_meet}')

