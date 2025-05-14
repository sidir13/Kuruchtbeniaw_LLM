import json

def save_jsonl(filename, dataset):
    with open(filename, "w", encoding="utf-8") as f:
        for item in dataset:
            json.dump(item, f)
            f.write("\n")