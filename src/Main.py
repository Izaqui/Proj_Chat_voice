import speech_recognition as sr
import pyttsx3
from random import choice
import os
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyC3P4e3SKNGB_RnpCt5IZUYp-BAsXrjU7Q'  # Gemini API key
genai.configure(api_key=GOOGLE_API_KEY)

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajustou a velocidade da fala para melhor clareza


#Configurações de temperatura
generation_config = {
    "candidate_count": 1,
    "temperature": 0.1,
}

#Configurações de segurança
safety_settings = {
    "HARASSMENT": "BLOCK_SOME",
    "SEXUAL": "BLOCK_SOME",
    "HATE": "BLOCK_SOME",
    "DANGEROUS": "BLOCK_SOME",
}
#Modelo utilizado
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])

# Voz definições
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
# definições de falar
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Metodo de inteção principal Escutar e comando de voz e responder via texto ou voz
def process_audio():
    recognizer = sr.Recognizer()
  
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("--------------Como esta se sentindo-------------------")
        print("--Uma Interface amigavel para parguntas e interação--")
        while True:
            try:
                print(f'Perguntas?')
                audio = recognizer.listen(source)
                # configuração de voz e linguagem 
                text = recognizer.recognize_google(audio, language='pt')
                print(f'> {text}')
                text = text.lower()
                response = chat.send_message(text)
                # Necessita configuração do projeto para linguagem e resposta sem um dialogo robotizado...
                #speak(response)
                print(f'______Resultado_______ \n\n{response.text}')
            except sr.UnknownValueError:
                print("...")
# Main
if __name__ == "__main__":
    process_audio()
