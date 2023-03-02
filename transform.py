import json

with open('chats.txt', 'r') as chats:
    lines = chats.readlines()

output = []
output.append({"role": "system", "content": "You are a woman responding to a man chatting with her. Use this examples to act as the Woman in a text chat:"})
for line in lines:
    if line.startswith('M: '):
        content = line.replace('M: ', '').strip()
        output.append({'role': 'user', 'content': content})
    elif line.startswith('W: '):
        content = line.replace('W: ', '').strip('?')
        output.append({'role': 'assistant', 'content': content})

with open('messages.json', 'w') as messages:
    messages.write(json.dumps(output, indent=4))
