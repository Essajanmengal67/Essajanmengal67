import requests
import csv

url = 'http://api.coincap.io/v2/assets'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request('GET', url, headers=headers)

myjson = response.json()

ourdata = []

csv_header = ['SYMBOL', 'NAME', 'PRICE(USD)']

for x in myjson['data']:
    listing = [x['symbol'], x['name'], x['priceUsd']]
    ourdata.append(listing)

with open('essajan.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csv_header)
    writer.writerows(ourdata)
print(myjson)
print('done')
