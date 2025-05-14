
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
model_id = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token  
model = AutoModelForCausalLM.from_pretrained(model_id) 




model.save_pretrained("./saved_model/gpt_neo")
tokenizer.save_pretrained("./saved_model/gpt_neo")

print("All clear")


