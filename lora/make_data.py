import json

def format_text(obj):
    return f"""\
<|system|>
{obj['system']}
<|user|>
{obj['user']}
<|assistant|>
{obj['assistant']}<|endoftext|>\
"""

# for fn in ['data_puns/train_gen.jsonl', 'data_puns/test_gen.jsonl']:

#     # Load the JSON Lines file
#     with open(fn, 'r') as f:
#         data = [json.loads(line) for line in f]

#     # Add the "text" field with value "x" to each object
#     data_new = []
#     for obj in data:
#         data_new.append({'text': format_text(obj)})

#     # Save the modified objects back to the JSON Lines file
#     if "train" in fn:
#         n = len(data_new) // 10 * 8
#         with open(fn.replace("_gen", ""), 'w') as f:
#             for obj in data_new[:n]:
#                 f.write(json.dumps(obj) + '\n')
#         with open(fn.replace("_gen", "").replace("train", "valid"), 'w') as f:
#             for obj in data_new[n:]:
#                 f.write(json.dumps(obj) + '\n')
#     else:
#         with open(fn.replace("_gen", ""), 'w') as f:
#             for obj in data_new:
#                 f.write(json.dumps(obj) + '\n')

SYS_PROMPT = "You are Labrador, an AI language model developed by IBM DMF (Data Model Factory) Alignment Team. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior."

fn = "data_puns_shiv/puns.jsonl"

# Load the JSON Lines file
with open(fn, 'r') as f:
    data = [json.loads(line) for line in f]

# Add the "text" field with value "x" to each object
data_new = []
for obj in data:
    obj["system"] = SYS_PROMPT
    obj["user"] = obj["inputs"]
    obj["assistant"] = obj["targets"]
    data_new.append({'text': format_text(obj)})

# Save the modified objects back to the JSON Lines file
n = len(data_new) // 10 * 7
m = len(data_new) // 10 * 2 + n
with open(fn.replace("puns.jsonl", "train.jsonl"), 'w') as f:
    for obj in data_new[:n]:
        f.write(json.dumps(obj) + '\n')
with open(fn.replace("puns.jsonl", "valid.jsonl"), 'w') as f:
    for obj in data_new[n:m]:
        f.write(json.dumps(obj) + '\n')
with open(fn.replace("puns.jsonl", "test.jsonl"), 'w') as f:
    for obj in data_new[:m]:
        f.write(json.dumps(obj) + '\n')