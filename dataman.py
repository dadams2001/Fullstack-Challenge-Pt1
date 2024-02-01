import json, re
import pandas as pd
class DataController(object):
    def __init__(self):
        self.accounts = pd.read_csv("./accounts.csv").to_dict()
        for key, value in self.accounts["phone"].items():
            self.accounts["phone"][key] = self.reformat_phone(value)

    def GET(self):
        output = {'result':'success'}
        try:
            output['accounts'] = self.accounts
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        
        return json.dumps(output)
    
    def reformat_phone(self, phone_number):
        digits_only = re.sub(r'\D', '', phone_number)

        if digits_only.startswith('+'):
            return digits_only
        else:
            default_country_code = '+1'
            return f'{default_country_code}{digits_only}'
