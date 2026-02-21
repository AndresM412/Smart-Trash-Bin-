import os

import RPi.GPIO as GPIO
import time
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play
import sys

def setup_gpio(trigger_pin, echo_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def distance_measurement(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    pulse_start_time = time.time()
    pulse_end_time = time.time()

    while GPIO.input(echo_pin) == 0:
        pulse_start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

def play_audio(file_path):
    sound = AudioSegment.from_file(file_path)
    play(sound)

def record_audio(file_path, duration=5):
    fs = 44100  # Frecuencia de muestreo
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()

    write(file_path, fs, recording)

def main():
    trigger_pin = 14
    echo_pin = 15

    base_path = os.getcwd()
    audio_file_path = os.path.join(base_path, "Bienvenido.mp3")
    recording_path = os.path.join(base_path, "Peticiones", "peticion.wav")

    setup_gpio(trigger_pin, echo_pin)

    try:
        audio_played = False  # Variable para rastrear si ya se reprodujo el audio
        while True:
            # Esperar hasta que se detecte algo a menos de 30 cm
            while distance_measurement(trigger_pin, echo_pin) >= 30:
                time.sleep(0.1)
                audio_played = False  # Restablecer el estado cuando la persona está fuera de rango

            # Reproducir el audio solo una vez
            if not audio_played:
                play_audio(audio_file_path)
                audio_played = True

                # Grabar audio y guardarlo como "peticion.wav"
                record_audio(recording_path)
                print("Grabación completada. Archivo guardado como 'peticion.wav'")
                
                sys.exit()  # Salir del programa después de completar la grabación

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()