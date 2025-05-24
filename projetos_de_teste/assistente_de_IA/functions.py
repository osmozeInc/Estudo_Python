from openai import OpenAI # type: ignore
import pyttsx3

def ChatGPT():
    client = OpenAI(api_key="")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": "Olá, quem é você?"}
        ]
    )

    print(response.choices[0].message.content)


def Falar():
    engine = pyttsx3.init()
    texto = "Olá, esta é uma demonstração do pyttsx3."
    engine.say(texto)
    engine.runAndWait()




#Clima, Free WeatherAPI chave: 1aba4342ed1b4daba44190007252702