import requests
import json
from jsonschema import Draft7Validator as json_validator

def get_outbreak(offline=True):
    if offline:
        with open('outbreak.json', 'r') as outbreak:
            return json.load(outbreak)
    r = requests.get("https://raw.githubusercontent.com/SuLab/outbreak.info-resources/master/yaml/outbreak.json")
    return r.json()

class OutbreakValidator:
    def __init__(self):
        self.schema = get_outbreak()

    def find_outbreak_type(self, outbreak_type):
        possibilities = [item for item in self.schema['@graph'] if item['@id'] == outbreak_type]
        if len(possibilities) != 1:
            raise Exception(f"Found multiple possibilities for {outbreak_type}")
        return possibilities[0]

    def validate(self, value, outbreak_type):
        outbreak_schema = self.find_outbreak_type(outbreak_type)
        validator = json_validator(outbreak_schema['$validation'])
        if not validator.is_valid(value):
            self.errors = validator.iter_errors(value)
            self.print_errors()
            return False
        print('Instance is valid!')
        return True

    def print_errors(self):
        for error in self.errors:
            if "is valid" in error.message:
                #import pdb;pdb.set_trace()
                pass
            message = error.cause if error.cause else error.message

            path = ' -> '.join(error.path) if error.path else "root"
            print(f"Error with value \033[31m\"{error.instance}\"\033[m for field \033[34m\"{path}\"\033[m"
                    f"\n\t\033[90m{message}\033[m\n")

schema = OutbreakValidator()
schema.validate({'name': 'a', 'description': 'b', 'author': 'c'}, "outbreak:Dataset")
schema.validate({'name': 'a', 'description': 'b', 'author':[{'@type': 'Person', 'name': 'c'}]}, "outbreak:Dataset")
schema.validate({'description': 'b', 'author': 'c'}, "outbreak:Dataset")
