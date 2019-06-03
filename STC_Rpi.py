import requests 
import json
import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

S1G = 8
S1O = 10
S1R = 12
S2G = 22
S2O = 24
S2R =26
S3G =11
S3O = 13
S3R = 15
S4G = 36
S4O = 38
S4R = 40
GPIO.setup(S1G, GPIO.OUT,initial=0)
GPIO.setup(S1O, GPIO.OUT,initial=0)
GPIO.setup(S1R, GPIO.OUT,initial=0)
GPIO.setup(S2G, GPIO.OUT,initial=0)
GPIO.setup(S2O, GPIO.OUT,initial=0)
GPIO.setup(S2R, GPIO.OUT,initial=0)
GPIO.setup(S3G, GPIO.OUT,initial=0)
GPIO.setup(S3O, GPIO.OUT,initial=0)
GPIO.setup(S3R, GPIO.OUT,initial=0)
GPIO.setup(S4G, GPIO.OUT,initial=0)
GPIO.setup(S4O, GPIO.OUT,initial=0)
GPIO.setup(S4R, GPIO.OUT,initial=0)

API_ENDPOINT = "http://192.168.0.11:8080/Greeting"

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

# green signal1 for time  till loadedjson[0] rest red 
GPIO.output(S1G,GPIO.HIGH)
GPIO.output(S2R,GPIO.HIGH)
GPIO.output(S3R,GPIO.HIGH)
GPIO.output(S4R,GPIO.HIGH)
 # orange for 3 second signal one 
 #green signal2 for time loaded json[1] rest red 
 #orange for 3sec
 # green for  sigal3 json 2 rst red 
 #orange for 3sec 
 #green signal4 json 3 rest red 
 # orange for 3sec  
