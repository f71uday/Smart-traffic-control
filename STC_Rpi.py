import requests 
import json
API_ENDPOINT = "http://localhost:8080/Greeting"

r = requests.get(API_ENDPOINT)
data = r.json()
stopTime1 =0
stopTime2 =0
stopTime3 =0
stopTime4 =0
loaded_json = json.loads(r.text)
for x in range(4):
	print (loaded_json[x]['id'])
for x in range(1,4):
	stopTime1 = stopTime1+loaded_json[x]['id']
stopTime2= loaded_json[0]['id']+loaded_json[2]['id']+loaded_json[3]['id']
stopTime3= loaded_json[0]['id']+loaded_json[1]['id']+loaded_json[3]['id']
stopTime4= loaded_json[0]['id']+loaded_json[1]['id']+loaded_json[2]['id']
print stopTime1
print stopTime2
print stopTime3
print stopTime4