import openai
import os
from dotenv import load_dotenv

load_dotenv()
mi_api_key = os.getenv("OPENAI_API_KEY")

modelo_whisper = 'whisper-1'

media_file_path = os.path.join(os.getcwd(), 'Peticiones', 'peticion.wav')

with open(media_file_path, 'rb') as media_file:
    residuo = openai.Audio.transcribe(
        api_key=mi_api_key,
        model=modelo_whisper,
        file=media_file)

residuo = residuo['text']
#print(residuo)
# --------------------------------------------------------------------

modelo = 'gpt-3.5-turbo'

mensajes = [
    {'role': 'system', 'content': 'Responde solo con una palabra'},
    {'role': 'user', 'content': '¿Respondeme lo siguiente SOLO usando la palabra orgánico o inorgánico: El residuo al que se hace referencia en el siguiente texto: (' + residuo + '), es orgánico o inorgánico?'},
    {'role': 'assistant', 'content': 'Respuesta del modelo'}
]

# Luego, realizas la solicitud a la API
respuesta = openai.ChatCompletion.create(
    api_key=mi_api_key,
    model=modelo,
    messages=mensajes,
    max_tokens=10
)
respuesta_texto=respuesta["choices"][0]["message"]["content"]
print(respuesta_texto)