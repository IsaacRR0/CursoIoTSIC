from gpiozero import LED
import psutil

# Definir los pines GPIO para los LEDs 
led_red = LED(4)
led_amber = LED(17)
led_green = LED(27)
led_blue = LED(22)

# Archivo de registro
log_file = "uso_memoria.txt"

#Función para mostrar mensajes y encender los LEDs según la cantidad de memoria
def show_memory(memory):
    with open(log_file, "a") as file:

        if memory <= 25:  # Menos de 25%
            file.write("Memoria menor a 25%\n")
            led_red.off()
            led_amber.off()
            led_green.on()
            led_blue.off()
            print(str(memory))
        elif memory > 25 and memory <= 50:  # Mayor de 25% pero menor a 50%
            file.write("Memoria menor a 50%\n")
            led_red.off()
            led_amber.off()
            led_green.on()
            led_blue.on()
            print(str(memory))
        elif memory > 50 and memory <= 75:  # Entre 10 cm y 30 cm
            file.write("Memoria menor a 75%\n")
            led_red.off()
            led_amber.on()
            led_green.on()
            led_blue.on()
            print(str(memory))
        else:
            file.write("Memoria menor al 90%\n")
            led_red.on()
            led_amber.on()
            led_green.on()
            led_blue.on()
            print(str(memory))


# Bucle principal para medir la distancia continuamente
try:
    while True:
        #Obtener uso de la memoria en porcentaje
        memory = psutil.cpu_percent(interval=1)
        #memory = psutil.virtual_memory().available*100/psutil.virtual_memory().total
        show_memory(memory)
except KeyboardInterrupt:
    led_red.off()
    led_amber.off()
    led_green.off()
    led_blue.off()