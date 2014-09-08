
import sys
from Pubnub import Pubnub

#import RPi.GPIO as GPIO
#import pingo
from time import sleep
import json


DEFAULT_RELAY_TIMER = 1000


placa = pingo.rpi.RaspberryPi()  # *
pino_relay = placa.pins[7]
pino_relay.mode = pingo.OUT
pino_relay.low()



publish_key = "pub-c-aa5394de-a478-450e-9130-358036369684"
subscribe_key = "sub-c-4e9507d2-3793-11e4-afa1-02ee2ddab7fe"
secret_key = "sec-c-MDZlZTRlZGItODIxNS00OTk0LTk2NjgtZDYyOWU4NTJjNjQ4"
cipher_key = ''
ssl_on = False


## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

channel = 'dispensadora'


# Asynchronous usage
def callback(message, channel):
	if message['action'] == "release":
		print("RELEASING...")
		if 'release_time' in message:
			activate_relay(message['release_time'])
		else:
			activate_relay(DEFAULT_RELAY_TIMER)
	else:
		print(message)


#		"action": "release",
#		"timestamp": new Date(),
#		"id": "glass"


def error(message):
	print("ERROR : " + str(message))


def connect(message):
	print("CONNECTED")


def reconnect(message):
	print("RECONNECTED")


def disconnect(message):
	print("DISCONNECTED")



def activate_relay():
	activate_relay(DEFAULT_RELAY_TIMER)

def activate_relay(release_time):
	print "activating relay for %s ms" % release_time
	pino_relay.high()
	sleep(release_time)
	pino_relay.low()


pubnub.subscribe(channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)