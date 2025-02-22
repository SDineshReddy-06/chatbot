from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as ai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Configure API Key
API_KEY = 'AIzaSyC9vc4fgZ4oCFP1NltdU16lp-1ywatEz80'
ai.configure(api_key=API_KEY)

# Initialize AI Model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_ai():
    data = request.get_json()
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = chat.send_message(user_message)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run()
