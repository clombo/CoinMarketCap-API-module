from coincap import Market

""" 
Please note that this is example code and should not be run all at once.abs

 If you would like to test it I suggest running and printing the data back for each section separately otherwise
 you will be flooded with data.

"""

#Ticker example
ticker1 = Market.Ticker()

print ticker1

print '\n'

#Also takes additional arguments
ticker2 = Market.Ticker(limit=1,convert='EUR')

print ticker2

#For specific currency
litecoin = Market.Ticker(id='litecoin')
#or
litecoin = Market.Ticker(id='litecoin',convert='EUR')

print litecoin

#Global example
gbl = Market.Global()
#or
gbl = Market.Global(convert='EUR')