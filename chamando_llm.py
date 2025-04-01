from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "Voce é um expert sobre a historia dos LLMs."},
        {
            "role": "user",
            "content": "Descreva o que é um LLM em uma frase."
        }
    ]
)

print(completion.choices[0].message.content)
