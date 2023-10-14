import RPi.GPIO as GPIO
import time

# Configurar el pin GPIO
led_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Definir el diccionario de caracteres en código Morse
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': ' '}

# Función para parpadear el LED según el código Morse
def blink_morse_code(message):
    for char in message:
        if char == ' ':
            time.sleep(2)  # Espacio entre palabras
        else:
            morse_char = morse_code.get(char.upper())
            if morse_char:
                for symbol in morse_char:
                    if symbol == '.':
                        GPIO.output(led_pin, GPIO.HIGH)
                        time.sleep(0.2)  # Punto
                    elif symbol == '-':
                        GPIO.output(led_pin, GPIO.HIGH)
                        time.sleep(0.6)  # Rayo
                    GPIO.output(led_pin, GPIO.LOW)
                    time.sleep(0.2)  # Espacio entre símbolos
            time.sleep(0.4)  # Espacio entre letras

try:
    while True:
        message = "SOS"
        for _ in range(360):  # Parpadear durante 30 minutos (30 minutos * 12 ciclos por minuto)
            blink_morse_code(message)
            time.sleep(2)  # Espacio entre mensajes

except KeyboardInterrupt:
    GPIO.cleanup()