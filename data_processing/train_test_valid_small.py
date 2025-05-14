import json
from save_jsonl import save_jsonl


with open('./data/processed/text.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


number_messages = len(data)
print(f"There is {number_messages} in total")

small_percentage = 0.001
number_max = number_messages * small_percentage

n_train = int(0.70 * number_max)

if (number_max - n_train) % 2 == 0:
    n_test = int((number_max - n_train)/2)
    n_val = n_test
else:
    n_test = int((number_max - n_train)/2)
    n_val = n_test + 1

print(f"Train has {n_train} messages, test has {n_test} and val has {n_val}")

train_data = data[:n_train]
val_data = data[n_train:n_train + n_val]
test_data = data[n_train + n_val:]


save_jsonl("./data/data_splits/train_small.jsonl", train_data)
save_jsonl("./data/data_splits/val_small.jsonl", val_data)
save_jsonl("./data/data_splits/test_small.jsonl", test_data)

print("All done")