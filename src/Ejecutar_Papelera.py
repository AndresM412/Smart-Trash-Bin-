import subprocess

#Ejecutá Ultrasonico_Solicitud.py
subprocess.run(['python','Ultrasonico_sensor.py'])

# Ejecuta Proceso_Solicitud.py
subprocess.run(['python', 'Proceso_Solicitud.py'])

subprocess.run(['python', 'Servos.py'])
