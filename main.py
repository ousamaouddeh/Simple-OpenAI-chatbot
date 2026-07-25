from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI()
MODEL='gpt-5.4-mini'
TEMPERATURE = 2
#MAX_TOKENS = 100       Not working with this model because its a free model
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions"

messages = [{"role":"system","content": SYSTEM_PROMPT}]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        stream=True
    )

    full_reply = ""
    print("Assistant: ", end="", flush=True)
    for chunk in response:
        piece = chunk.choices[0].delta.content
        if piece:
            print(piece, end="", flush=True)
            full_reply += piece
    print()

    messages.append({"role": "assistant", "content": full_reply})
    return full_reply
while True:
    user_input = input("You : ")
    if user_input.strip().lower() in {'exit','quit'}:
        break
    answer = chat(user_input)
