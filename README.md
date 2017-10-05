# CoinMarketCap-API-module


This might be overkill since this is a very small API. This was only for practice in building modules.
Practice makes perfect.

This module manipulates the [CoinMarketCap](https://coinmarketcap.com/) API available. For more information see their [API documentation](https://coinmarketcap.com/api/)

NOTES:
* Endpoints only update every 5 minutes
* All 'last_updated' fields are in [unix timestamps](https://en.wikipedia.org/wiki/Unix_time)

To manipulate the timestamp values using the datetime module available in python.

# Example Usage

Example code can be found in **example.py** as well

## import module

```python
from coincap import Market
```

The module has two static methods available:

* Ticker()
* Global()

## Ticker()

The Ticker() method returns a list of cryptocurrencies information in JSON format.

```python
t = Market.Ticker()

print t
```

The list can be limited by passing a limit as a argument when calling the method.

Additionally you can also set the currency you want price values to be returned in. For a full list of supported currencies see their [documentation page](https://coinmarketcap.com/api/). The default is USD.

Best practive would be to always set a limit when calling the Ticker() method otherwise it returns all the cryptocurrencies availbale on their platform.

```python
t = Market.Ticker(limit=10,convert='EUR')

print t
```

### Ticker for specific cryptocurrency

You can return information regarding a specific currency as well.

```python
litecoin = Market.Ticker(id='litecoin')
```

Optional argument includes the convert argument that you can pass to convert the output to the desired currency value.

```python
litecoin = Market.Ticker(id='litecoin',convert='EUR')
```

## Global()

The Global() method returns global data like the total market cap and active currencies.

```python
g = Market.Global()

print g
```

You can also pass a additional parameter to convert it to a currency value you want.

```python
g = Market.Global(convert='EUR')

print g
```
