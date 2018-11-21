import requests
from time import sleep
import Adafruit_DHT as dht
from twilio.rest import Client
import collections

APIKey="R2GTGW0UJZJSIESJ"
URL='https://api.thingspeak.com/update?api_key=%s'%APIKey

account_sid = 'AC15f3074e44f564118a7df456a0e23ac9'
auth_token = '38b4ef4f6c6e8404a413ac7c3016b840'
client = Client(account_sid, auth_token)

while True:
	try:
		humidity,temperature=dht.read_retry(dht.DHT22,23)
		print(humidity,temperature)
		if temperature > 20.0 and humidity >= 10:
			message = client.messages \
				.create(
					body='Too hot in your greenhouse! Temperature = {temp:.2f}°C, Humidity = {hum:.2f}%'.format(temp=temperature, hum=humidity),
					from_='+4759446214',
					to='+33643269310'
				)	
		
		connection=requests.post(URL+'&field1=%.2f&field2=%.2f'%(temperature,humidity))
		
		sleep(20)
	except:
		print('Error occured')
		break
