import os
from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_system_content():
    try:
        with open("system_content.txt", "r") as file:
            return file.read().strip()  # Read content and remove leading/trailing whitespace
    except Exception as e:
        return f"Error loading system content: {str(e)}"


app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    try:
        system_content = get_system_content()
        response = openai.ChatCompletion.create(  # Correct API method
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        bot_message = response['choices'][0]['message']['content'].strip()
        return jsonify({'reply': bot_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
