
import sys
from Pubnub import Pubnub

#import RPi.GPIO as GPIO
import pingo
from time import sleep

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
	print(message)


def error(message):
	print("ERROR : " + str(message))


def connect(message):
	print("CONNECTED")


def reconnect(message):
	print("RECONNECTED")


def disconnect(message):
	print("DISCONNECTED")



def activate_relay():
	activate_relay(1000)

def activate_relay(time):
	pino_relay.high()
	sleep(time)
	pino_relay.low()


pubnub.subscribe(channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)