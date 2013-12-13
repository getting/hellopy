from urllib.request import urlopen


url = 'http://blockchain.info/charts/market-price?format=json'
response = urlopen(url)

print(response.read().decode())
