from coincap import Market

#ticker = Market.Global()

#print ticker

g = Market.Global()

for key in g:
    print "{}:{}\n".format(key,g[key])