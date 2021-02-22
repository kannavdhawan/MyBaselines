#
import requests
res = requests.get('https://api.ratesapi.io/api/latest')
if res.status_code != 200:
    raise ApiError('ERROR')

for key, value in res.json().items():
    if key == 'rates':
        print(value['INR'])

