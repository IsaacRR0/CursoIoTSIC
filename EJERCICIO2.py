import RPi.GPIO as GPIO
import time

# Configura los pines de los LEDs
led_pins = [17, 18, 27, 22]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in led_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def turn_on_led(led_num):
    GPIO.output(led_pins[led_num - 1], GPIO.HIGH)

def turn_off_led(led_num):
    GPIO.output(led_pins[led_num - 1], GPIO.LOW)

def main():
    setup()
    while True:
        with open("solicitud.txt", "r") as file:
            solicitud = file.read().strip()
        
        if solicitud:
            for i, status in enumerate(solicitud):
                if status == "1":
                    turn_on_led(i + 1)
                elif status == "0":
                    turn_off_led(i + 1)
                else:
                    print("Entrada inválida en solicitud.txt")
        
        time.sleep(1)  # Espera 1 segundo antes de volver a verificar el archivo

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
