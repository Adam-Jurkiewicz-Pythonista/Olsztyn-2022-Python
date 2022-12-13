"""
Czytamy z JSON
http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-09-01/2022-12-01/?format=json
Wykorzystamy:
https://requests.readthedocs.io/en/latest/
"""

import requests
waluta = "usd"
data_od = "2022-09-01"
data_do = "2022-12-01"
api_link = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data_od}/{data_do}/?format=json"

r_api = requests.get(api_link)
print(r_api)
dane = r_api.json()
print(dane)