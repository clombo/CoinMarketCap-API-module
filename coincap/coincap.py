import requests

API_URL = "https://api.coinmarketcap.com/v1/"

API_ENDPOINTS = {'ticker': "ticker/",'global': "global/"}

class Market(object):

    def __init__(self):
        #both the methods in the class can be called without inisializing the object since
        #no attributes are required at this point
        pass

    
    @staticmethod
    def Ticker(id="",**kwargs):

        """

            Can take a id of a specific cryptocurrency like bitcoin.

            Takes additional arguments list that is passed as the parameter list.
            Only two that currently exist on the API is:

            limit : specify the limit of how many results you want if no specific cryptocurrency is specified.
            convert : Convert the price totals to specific currency.

        """

        path = "{base}{endpoint}{ID}".format(base=API_URL,endpoint=API_ENDPOINTS['ticker'],ID=id)
        resp = requests.get(path,params=kwargs)
        return resp.json()
    
    @staticmethod
    def Global(**kwargs):

        """ 
        
            Returns global market cap data

            Takes additional arguments that is passed as parameter list.
            Only one currently exists on the API:

            convert: Convert the price totals to specific currency

        """

        path = "{base}{endpoint}".format(base=API_URL,endpoint=API_ENDPOINTS['global'])
        resp = requests.get(path,params=kwargs)
        return resp.json()