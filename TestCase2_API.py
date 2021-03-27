from prettytable import PrettyTable
import requests
response = requests.get("https://public-api.zipmex.net/api/v1.0/summary")
response_body = response.json()
result=[]
for instrument in response_body['data']:
    arr=response_body['data'][instrument]
    arr['instrument']=instrument
    result.append(arr)
t = PrettyTable(['instrument', 'last_price', 'lowest_24hr', 'highest_24hr'])

for i in result :
    t.add_row([i['instrument'], i["last_price"], i["lowest_24hr"], i["highest_24hr"]])
print(t)

