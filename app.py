import os
from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

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
        response = openai.ChatCompletion.create(  # Correct API method
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful assistant for an engineering college."},
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
    app.run(debug=True)
