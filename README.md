# LIET Bot 🤖

**LIET Bot** is a Generative AI-powered chatbot designed to bridge the gap between students and various college resources, including faculty information, academic materials, and more. It aims to assist students in navigating their college experience by providing quick and easy access to essential information.

This chatbot leverages **OpenAI's GPT-3.5 Turbo** to provide intelligent, conversational responses, making it easy for students to get information about their college, faculty, and other resources.

### 🚀 Features
- **Generative AI**: Powered by OpenAI's GPT-3.5 Turbo for dynamic and context-aware conversations.
- **Bridges Gap**: Provides students with access to faculty information, academic resources, and more.
- **User-Friendly Interface**: Simple and intuitive interface for seamless communication.
- **Responsive**: Optimized for both desktop and mobile devices.
- **MongoDB Integration**: Stores conversation context in MongoDB for personalized and continuous interactions.
- **Context Storage**: Maintains conversation history in the `system_content.txt` file to track previous interactions and provide relevant responses.
  
### 🧑‍💻 Technologies Used
- **HTML**: For the structure of the web pages.
- **CSS**: Styling for a responsive and modern design.
- **JavaScript**: Powers the chatbot's interactive elements.
- **Python (Flask)**: Backend API that handles user input and processes chatbot responses.
- **OpenAI GPT-3.5 Turbo**: The core AI model used for generating intelligent, dynamic responses based on user input.
- **MongoDB**: Used to store the context of the conversation, ensuring that the bot provides personalized experiences.
- **AI Integration**: Uses OpenAI's GPT-3.5 Turbo model to generate intelligent and contextually aware responses.

### 💻 Setup & Installation

#### 1. Clone the repository:
```bash
git clone https://github.com/your-username/liet-bot.git
```

#### 2. Navigate into the project directory:
```bash
cd liet-bot
```

#### 3. Install required dependencies:
For backend (Python):
```bash
pip install -r requirements.txt
```

For frontend:
```bash
npm install
```

#### 4. Set up MongoDB:
LIET Bot uses MongoDB to store conversation context. To set it up:
- **Install MongoDB**: Follow the [MongoDB installation guide](https://docs.mongodb.com/manual/installation/).
- **Run MongoDB**:
  ```bash
  mongod
  ```

#### 5. Set up environment variables:
Create a `.env` file in the root directory and add the following:
```env
MONGODB_URI=mongodb://localhost:27017/liet-bot
OPENAI_API_KEY=your-openai-api-key
```
- Replace `your-openai-api-key` with your own OpenAI GPT-3.5 Turbo API key. You can get it from the [OpenAI API](https://platform.openai.com/account/api-keys).

#### 6. Run the server:
Start the backend server by running:
```bash
python app.py
```

Access the bot at `localhost:5000` in your browser.

### 📝 `system_content.txt` File for Context Storage
The `LIET Bot` stores the conversation context in the `system_content.txt` file. This file helps maintain continuity in interactions by storing user inputs and the bot’s responses.

- **Location**: `/system_content.txt`
- **Purpose**: Tracks important data like previous queries, answers, and context for ongoing conversations.

### 🌐 Live Link
Check out the live version of the LIET Bot here (wait for atleast one minute update: OpenAI API expired): [LIET Bot Live](https://liet-bot.onrender.com)

### 📄 License
Distributed under the MIT License. See `LICENSE` for more details.

### 🤝 Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

### 📝 Acknowledgments
- Designed to bridge the gap between students and college resources.
- Uses **OpenAI GPT-3.5 Turbo** to provide intelligent conversational responses.
- Special thanks to **[MohdFaizanUrRahman](https://github.com/MohdFaizanUrRahman)** and **[Sohailsp101](https://github.com/Sohailsp101)** for being my team members on this project.
- Thanks to the open-source community for providing the tools that made this project possible.

###ScreenShots
1) ![Screenshot 2025-01-02 230523](https://github.com/user-attachments/assets/f0a15006-661f-4bf1-b8aa-c72289797eb4) .
2)![Screenshot 2025-01-04 142908](https://github.com/user-attachments/assets/d42c044f-f181-4e86-9f07-c8b1c0496f0c).
3) ![Screenshot 2025-01-04 143201](https://github.com/user-attachments/assets/10060666-052f-491b-b921-5420e356cea8).

### Key Updates:
1. **OpenAI GPT-3.5 Turbo Integration**: This section includes the mention of OpenAI GPT-3.5 Turbo as the core AI model for generating responses.
2. **Environment Variables**: The `.env` file now includes an `OPENAI_API_KEY` to authenticate requests with OpenAI's API.


