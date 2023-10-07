from gpiozero import LED
import time

# Crear objetos LED para los LEDs rojo, verde y amarillo
led_rojo = LED(17)
led_verde = LED(2)
led_amarillo = LED(3)

try:
    while True:
        # Leer la señal desde la consola
        senal = input("Escribe 'alto', 'siga' o 'precaucion': ").lower()

        if senal == 'alto':
            led_rojo.on()
            led_verde.off()
            led_amarillo.off()
        elif senal == 'siga':
            led_rojo.off()
            led_verde.on()
            led_amarillo.off()
        elif senal == 'precaucion':
            led_rojo.off()
            led_verde.off()
            led_amarillo.on()
        else:
            print("Entrada no válida. Usa 'alto', 'siga' o 'precaucion'.")

except KeyboardInterrupt:
    print("Programa detenido")
finally:
    # Apagar todos los LEDs
    led_rojo.off()
    led_verde.off()
    led_amarillo.off()
