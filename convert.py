from bs4 import BeautifulSoup
import requests
import json

class ConvertCurrency(object):

    def __init__(self):
        self.soup = ""

    def check_valid_currency(self, from_currency, to_currency):
        ''' To check from and to currency types '''

        with open('native_currencies.json', 'r') as json_file:
            currency_dict = json.load(json_file)
            if from_currency not in currency_dict.keys():
                return "Invalid : from currency"
            if to_currency not in currency_dict.keys():
                return "Invalid : to currency"

        ## when both keys are valid
        return None

    def convert_currency(self, amount, from_currency, to_currency):
        ''' To convert the given amount from currency to currency '''

        try:
            validate_currency = self.check_valid_currency(from_currency, to_currency)
            if validate_currency is None:
                url = "https://finance.google.com/finance/converter?a=" + amount + "&from=" + from_currency + "&to=" + to_currency
                response = requests.get(url, headers={"Accept": "application/json"})
                self.soup = BeautifulSoup(response.text, 'html.parser')
                return self.soup.find(id="currency_converter_result").text.strip()
            else:
                return validate_currency
        except Exception as e:
            print('Caught exception. ' + str(e))