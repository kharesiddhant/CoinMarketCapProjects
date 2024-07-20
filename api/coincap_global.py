import requests
import json

api_key = ''

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest'

request = requests.get(global_url, headers=headers)
results = request.json()

data = results["data"]

print(json.dumps(results, sort_keys=True, indent=4))