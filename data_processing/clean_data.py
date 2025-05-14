import json

with open('./data/raw/kuru.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

messages, authors, timestamps, text = [], [], [], []
for i in range(len(data["messages"])-1):
    message_prompt = data["messages"][i]
    message_completion = data["messages"][i+1]

    content_prompt = message_prompt["content"]
    content_completion = message_completion["content"]

    timestamp_prompt = message_prompt["timestamp"]
    timestamp_completion = message_prompt["timestamp"]

    author_prompt = message_prompt["author"]["name"]
    author_completion = message_completion["author"]["name"]

    messages.append({"prompt":content_prompt + "\n", "completion" : content_completion })
    authors.append({"prompt":author_prompt, "completion" : author_completion })
    timestamps.append({"prompt":timestamp_prompt, "completion" : timestamp_completion })
    text.append({"text" : content_prompt})

with open('./data/processed/messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)

with open('./data/processed/timestamps.json', 'w', encoding='utf-8') as f:
    json.dump(timestamps, f, ensure_ascii=False, indent=2)


with open('./data/processed/authors.json', 'w', encoding='utf-8') as f:
    json.dump(authors, f, ensure_ascii=False, indent=2)

with open('./data/processed/text.json', 'w', encoding='utf-8') as f:
    json.dump(text, f, ensure_ascii=False, indent=2)

print("All clear")