from gpiozero import Device,AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from Proceso_Solicitud import respuesta_texto

Device.pin_factory = PiGPIOFactory(host='172.25.204.251', port=8888)

servo1 = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(4, min_pulse_width=0.0006, max_pulse_width=0.0023)

servo1.angle=-90
servo2.angle=-90
respuesta_texto = respuesta_texto.lower()
print(respuesta_texto)
def activar_servo(servo):
    servo.angle = 90
    sleep(3)
    servo.angle = -90

if respuesta_texto == "orgánico":
    activar_servo(servo2)
elif respuesta_texto == "inorgánico":
    activar_servo(servo1)



