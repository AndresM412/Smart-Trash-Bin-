🗑️ Smart Bin: Clasificación de Residuos con GenAI
Proyecto de hardware e inteligencia artificial que utiliza una Raspberry Pi y los modelos de OpenAI para automatizar la separación de residuos (Orgánicos e Inorgánicos) mediante comandos de voz.

🧠 ¿Cómo funciona?
Detección: Un sensor ultrasónico detecta la presencia de un usuario a menos de 30 cm.

Interacción: El sistema saluda al usuario y graba un clip de voz con el residuo que desea depositar.

Procesamiento (IA):

Whisper API: Convierte el audio (.wav) a texto.

GPT-3.5 Turbo: Analiza el texto y clasifica el objeto como "orgánico" o "inorgánico".

Acción: Según la respuesta de la IA, se activa uno de los dos servomotores para abrir la compuerta correspondiente.

🛠️ Stack Tecnológico
Lenguaje: Python 3.x

Hardware: Raspberry Pi 4, Sensor HC-SR04, Servomotores SG90.

APIs: OpenAI (Whisper & Chat Completions).

Librerías principales: gpiozero, sounddevice, pydub, python-dotenv.

📂 Estructura del Proyecto
/src: Contiene la lógica del sensor, control de motores y conexión con la API.

/assets: Archivos de audio de bienvenida y muestras de peticiones.

/config: Gestión de variables de entorno (API Keys).