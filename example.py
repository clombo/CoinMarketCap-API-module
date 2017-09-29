from coincap import Market

#Ticker example
ticker1 = Market.Ticker()

#Also takes additional arguments
ticker2 = Market.Ticker(limit=1,convert='EUR')

#For specific currency
litecoin = Market.Ticker(id='litecoin')
#or
litecoin = Market.Ticker(id='litecoin',convert='EUR')

#Global example
gbl = Market.Global()
#or
gbl = Market.Global(convert='EUR')

g = Market.Global()

for key in g:
    print "{}:{}\n".format(key,g[key])