# 🗑️ Papelera Inteligente con IA (OpenAI + Raspberry Pi)

Este proyecto utiliza una Raspberry Pi y la API de OpenAI para clasificar residuos mediante voz.

## 🚀 Funcionalidades
* **Detección de presencia:** Sensor ultrasónico HC-SR04.
* **Interacción por voz:** Whisper API para pasar de voz a texto.
* **Clasificación con LLM:** GPT-3.5 determina si el residuo es orgánico o inorgánico.
* **Hardware:** Servomotores para abrir la compuerta correspondiente.

## 🛠️ Instalación
1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv env`.
3. Activa el entorno y corre: `pip install -r requirements.txt`.
4. Configura tu `OPENAI_API_KEY` en un archivo `.env`.

## 🔌 Conexiones
* **Sensor Ultrasonico:** Trigger (GPIO 14), Echo (GPIO 15).
* **Servos:** Servo 1 (GPIO 17), Servo 2 (GPIO 4).