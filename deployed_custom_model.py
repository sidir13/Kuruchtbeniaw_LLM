# Fine-tune the model, provide it with the ChatModel class that enables interaction through the interface, and deploy it to MLflow.

import mlflow
from wraper_custom import ChatModel

model_id = 'saved_model/gpt_neo_finetuned/checkpoint-140'

artifacts = {
    "model_id": model_id
}
print("Saving model...")
mlflow.set_tracking_uri("http://localhost:5000")

with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="chat_model",
        python_model=ChatModel(),
        artifacts=artifacts
    )

print("Done!")