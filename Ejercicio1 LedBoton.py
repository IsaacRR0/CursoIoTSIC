from gpiozero import LED,Button

led = LED(17) 
boton = Button(2)
while True: 
    if boton.is_pressed:
        led.on()
    else:
        led.off()