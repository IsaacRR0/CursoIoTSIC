from gpiozero import LED
import time
LED = LED(17)
print("Ingrese el tiempo que desee que permanezca encendido el LED ")
encendido = input()
LED.on()
time.sleep(encendido)
LED.off()