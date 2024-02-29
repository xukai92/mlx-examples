import os
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = os.path.expanduser("~/artifacts/malachite-7b-0223-7.77")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

tokenizer.save_pretrained("malachite-7b")
model.save_pretrained("malachite-7b")