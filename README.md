# LLM Fine-Tuned Model Deployment


![Interface of the LLM](images/interface.PNG)

This project involves deploying a fine-tuned Large Language Model (LLM) on a website. The model is fine-tuned using personal data and is deployed using MLflow. The website frontend is built with JavaScript, HTML, and CSS, while the backend API is powered by Flask, allowing communication through API calls.

**Note**: The personal data used to fine-tune the model will **not be provided** as part of this project, as they are private and confidential.

## Limitations

Due to limited computational power on my local machine, I was only able to use a lighter model, **GPT-Neo 125M**. Additionally, the fine-tuning was performed with **very few data points**, which has resulted in **mediocre** performance in terms of the model's responses.

However, this setup serves as a starting point. To improve the model's performance, you can:
- **Use a more powerful model** with more resources (e.g., a larger version of GPT-Neo or another LLM).
- **Provide a larger dataset** for fine-tuning, which would significantly enhance the model's quality and accuracy in responses.


## Project Structure

- **Frontend**: 
  - JavaScript, HTML, and CSS are used to build the website interface.
  
- **Backend**: 
  - The LLM is fine-tuned using Python.
  - The model is deployed with **MLflow** for efficient management of machine learning models.
  - API calls to interact with the model are handled using **Flask**.

## Steps to Run the Project

### 1. **Frontend Setup**

The website is built using HTML, CSS, and JavaScript. To run the frontend:

1. Clone the repository.
2. Navigate to the `website/` directory.
3. Open `index.html` in a browser to see the website in action.

### 2. **Backend Setup (Flask API)**

The model is fine-tuned using Python and Flask API handles the communication between the frontend and the deployed model.

#### Requirements:

- Python 3.x
- Flask
- MLflow
- Other dependencies (listed in `requirements.txt`)

#### Installation:

1. Clone the repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
