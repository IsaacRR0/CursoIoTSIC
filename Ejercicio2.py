from gpiozero import LED
import time
led = LED(14)

while True:    
    print("Ingrese el tiempo que desee que permanezca encendido el LED ")
    encendido = int(input())
    led.on()
    time.sleep(encendido)
    led.off()