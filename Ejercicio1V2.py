import datetime
from gpiozero import Button

button_pin = 17
file_path = "/home/pi/Ejercicio1.txt"
button = Button(button_pin)

try:
    while True:
        button.wait_for_press()
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "a") as file:
            file.write(date_time + "\\n")
        print("Botón presionado. Fecha y hora escritas en el archivo.")

except KeyboardInterrupt:
    pass