from gpiozero import LED
import time

lista_LEDS = [LED(17),LED(2),LED(27),LED(4)]

'''
for i in range (0,4):
    print(lista_LEDS[i])
    time.sleep(2)

for i in range (3,-1,-1):   
    print(lista_LEDS[i])
    time.sleep(2)
'''


for i in range (0,4):
    lista_LEDS[i].on()
    time.sleep(2)
    
for i in range (3,-1,-1): 
    lista_LEDS[i].off()
    time.sleep(2)
    
