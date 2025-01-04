import os
from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
MONGO_URI = os.getenv('MONGO_URI') 

try:
    # Attempt to connect to MongoDB
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5-second timeout
    # Test the connection
    client.server_info()  # If the connection is successful, this will not raise an error
    print("Connected to MongoDB successfully!")
    
    # Proceed with accessing the database and collection
    db = client.get_database("lietContent")  # Replace with your database name
    collection = db.get_collection("liet-content")
    def get_system_content_from_db():
        try:
            # Fetch the system content document
            system_content_doc = collection.find_one({"key": "system_content"})  # Use your query filter
            if system_content_doc:
                return system_content_doc.get("content", "Default system content")
            return "System content not found in database."
        except Exception as e:
            return f"Error loading system content from MongoDB: {str(e)}"

except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")

def get_event_content():
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
        system_content = get_system_content_from_db()
        new_events = get_event_content()
        response = openai.ChatCompletion.create(  # Correct API method
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "system", "content": new_events},
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
