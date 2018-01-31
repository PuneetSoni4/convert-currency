from unittest import TestCase
import convert
import pytest

## using python pytest fixture to create and destroy class object
@pytest.yield_fixture(scope="class", autouse=True)
def ConvertCurrency(request):
    cc_object = convert.ConvertCurrency()
    if request.cls is not None:
        request.cls.cc_object = cc_object
    yield cc_object
    del cc_object

## implementing fixture to complete test class
@pytest.mark.usefixtures('ConvertCurrency')
class TestConvertCurrency(TestCase):

    ## TEST CASE : 1
    def test_convert_currency_1(self):
        result = self.cc_object.convert_currency('1', 'BTC', 'USD')
        assert (result == "1 BTC = 10114.9950 USD")

    ## TEST CASE : 2
    def test_convert_currency_2(self):
        result = self.cc_object.convert_currency('1.50', 'USD', 'BTC')
        assert (result == "1.5000 USD = 0.0002 BTC")

    ## TEST CASE : 3
    def test_convert_currency_3(self):
        result = self.cc_object.convert_currency('1', 'USD', 'USD')
        assert (result == "1 USD = 1 USD")

    ## TEST CASE : 4
    def test_convert_currency_4(self):
        result = self.cc_object.convert_currency('1', 'ABC', 'XYZ')
        assert (result == "Invalid : from currency")

    ## TEST CASE : 5
    def test_convert_currency_5(self):
        result = self.cc_object.convert_currency('1', 'ABC', 'USD')
        assert (result == "Invalid : from currency")

    ## TEST CASE : 6
    def test_convert_currency_6(self):
        result = self.cc_object.convert_currency('1', 'USD', 'XYZ')
        assert (result == "Invalid : to currency")