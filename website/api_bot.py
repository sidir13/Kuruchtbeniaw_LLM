import sys
sys.path.append('./')
from wraper_custom import ChatModel

import mlflow.pyfunc
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

print("Initialization api flask")
app = Flask(__name__)
CORS(app)


model_uri = "chat_model" 
model = mlflow.pyfunc.load_model(model_uri)
print("Model loaded successfully")
# Api route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Recuperation of prompt ...")
        input_data = request.get_json()

        # "Make sure the request contains a prompt
        if 'prompt' not in input_data:
            return jsonify({'error': 'Missing prompt'}), 400

        prompt = input_data['prompt']

        # Conversion to DataFrame for passing to MLflow.
        input_df = pd.DataFrame({'prompt': [prompt]})

        # Using the model to make a prediction.
        prediction = model.predict(input_df)

        # Return the response in JSON format.
        return jsonify({'response': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

print("Starting api...")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
    print("Api ended !")