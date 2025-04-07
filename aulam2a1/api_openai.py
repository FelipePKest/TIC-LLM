
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Voce é um expert sobre a historia dos LLMs."},
        {
            "role": "user",
            "content": "Conte a historia dos LLMs em uma frase."
        }
    ]
)

print(completion.choices[0].message.content)
