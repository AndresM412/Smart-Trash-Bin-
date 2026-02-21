🗑️ Smart Bin: Clasificación de Residuos con GenAI
Este proyecto integra hardware (Raspberry Pi) con servicios de Inteligencia Artificial (OpenAI) para crear una papelera inteligente capaz de clasificar residuos mediante comandos de voz.

🚀 Descripción del Proyecto
El sistema automatiza el proceso de reciclaje eliminando la duda del usuario sobre dónde depositar un residuo. Utiliza un sensor de proximidad para iniciar la interacción, captura audio, lo transcribe y utiliza un modelo de lenguaje para tomar la decisión de apertura de compuertas.

🧠 Flujo de Trabajo (Pipeline)
Detección de Presencia: El sensor ultrasónico HC-SR04 monitorea objetos a menos de 30 cm.

Captura de Voz: El sistema reproduce un saludo (Bienvenido.mp3) y graba la petición del usuario (peticion.wav).

Procesamiento de Lenguaje (NLP):

STT (Speech-to-Text): Se utiliza OpenAI Whisper para transcribir el audio a texto.

Razonamiento: Un prompt especializado en GPT-3.5 Turbo analiza la transcripción y clasifica el residuo estrictamente como "orgánico" o "inorgánico".

Ejecución Física: Dependiendo de la clasificación, se activa uno de los dos servomotores para abrir la tapa correspondiente.

🛠️ Stack Tecnológico
Lenguaje: Python 3.x.

Hardware: Raspberry Pi, Sensor Ultrasónico HC-SR04, Servomotores SG90.

IA & APIs: OpenAI API (Whisper-1 & GPT-3.5-Turbo).

Librerías: gpiozero, openai, sounddevice, pydub, python-dotenv.

📂 Estructura de Archivos
src/: Contiene los módulos de control de sensores, motores y lógica de IA.

assets/: Archivos multimedia (audio de bienvenida y muestras de voz).

config/: Configuración de entorno y seguridad (API Keys).

🔧 Configuración
Para replicar este proyecto:

Instala las dependencias: pip install -r requirements.txt.

Configura tus credenciales en un archivo .env:

Fragmento de código
OPENAI_API_KEY=tu_api_key_aqui
PIGPIO_HOST=tu_ip_raspberry
Ejecuta el orquestador: python src/Ejecutar_Papelera.py.

Nota: Este proyecto fue desarrollado con fines educativos y de investigación en la integración de IoT con modelos de lenguaje de gran escala (LLMs).
