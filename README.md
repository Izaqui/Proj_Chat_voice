# Proj_Chat_voice

# Chat Voice com Gemini

## Projeto de interação de um chat bot por voz integrado com Gemini  

  


**Objetivo:** Cria um chat modo terminal para interação direta entre usuário e IA. A ideia principal é manter uma interação continua e natural entre IA e usuário sem utilizar promp escrito

**Descrição:** Um projeto simples construído em python com integração da <a href="https://gemini.google.com/app">**Gemini_API**</a>. 

## Projeto constituído de:
**Arquivo `Main.py`**
**`GOOGLE_API_KEY  =  'TOKEN' `**<a href="https://aistudio.google.com/app/apikey">Gemini API key</a>
**`genai.configure(api_key=GOOGLE_API_KEY)`**

**safety_settings**
`"HARASSMENT": "BLOCK_SOME",`
`"SEXUAL": "BLOCK_SOME",`
`"HATE": "BLOCK_SOME",`
`"DANGEROUS": "BLOCK_SOME",`

**Model**
`gemini-1.0-pro`

**Importações**
`import  speech_recognition  as  sr`
`import  pyttsx3`
`from  random  import  choice`
`import  os`
`import  google.generativeai  as  genai`