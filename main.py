import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Faz a requisição para o modelo GPT-4
resposta = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, sem considerar descrição."
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ]
)

# Imprime a resposta
print(resposta['choices'][0]['message']['content'])
