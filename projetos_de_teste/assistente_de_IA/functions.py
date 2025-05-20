from openai import OpenAI # type: ignore

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
