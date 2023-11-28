import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

channel = 17

GPIO.setup(channel, GPIO.IN)

def mediHumedad():
    valor=GPIO.input(17)
    print(valor)

print("Sensado de humedad")

while(True):
    mediHumedad()
    time.sleep(2)