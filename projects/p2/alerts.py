import os
import csv
import json
import time
import sys
import requests
from datetime import datetime

local_currency = 'INR'
local_symbol = '₹'

api_key = ''
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("ALERTS TRACKING...")
print()

already_hit_symbols = []

while True:
    with open("my_alerts.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if '\ufeff' in line[0]:
                symbol = line[0][1:].upper()
            else:
                symbol = line[0].upper()
            amount = line[1]

            quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol 

            request = requests.get(quote_url, headers=headers)
            results = request.json()

            currency = results['data'][symbol]

            name = currency['name']
            price = currency['quote'][local_currency]['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                os.system("say ALERT. ALERT. ALERT. ")
                os.system('say '+ str(name) + ' hit ' + amount)
                sys.stdout.flush()

                now = datetime.now()
                current_time = now.strftime("%I:%M%p")
                print(name + ' hit ' + amount + ' at ' + current_time + '!')
                already_hit_symbols.append(symbol)

    print('...')
    time.sleep(10)
