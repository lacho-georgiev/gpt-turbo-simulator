# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import json

openai.api_key = "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"

def send_message(message):

  with open('messages.json', 'r') as file:
    messages = json.load(file)

  with open('chats.txt', 'a') as chats:
    chats.write("W: {}\n".format(message))

  messages.append({"role": "user", "content": message})

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  response_text = response["choices"][0]["message"]["content"]
  # print(response_text)

  with open('chats.txt', 'a') as chats:
    chats.write("W: {}\n".format(response_text))

  messages.append({"role": "assistant", "content": response_text})

  with open('messages.json', 'w') as file:
    json.dump(messages, file)

  return response_text


print("assistant:", send_message("(new chat)"))

while True:
  message = input("user: ")
  if message.lower() == "exit":
    break
  print("assistant:", send_message(message))