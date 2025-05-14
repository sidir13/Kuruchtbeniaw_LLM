# Class that enables interaction through the interface, and deploy it to MLflow.

import mlflow.pyfunc
from transformers import AutoTokenizer, AutoModelForCausalLM


class ChatModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        model_id = context.artifacts["model_id"]
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id)

    def predict(self, context, model_input):
        prompt = model_input["prompt"][0]  # si input est un DataFrame
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        output = self.model.generate(input_ids, max_new_tokens=50, do_sample=True, top_k=50)
        return [self.tokenizer.decode(output[0], skip_special_tokens=True)]
