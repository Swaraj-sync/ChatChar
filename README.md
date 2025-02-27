# 🗨️ NLP Character Chatbot  

A Flask-based chatbot that allows users to chat with fictional or real-world characters using Google's Gemini API. The app features a simple web interface where users can enter a character's name once and then engage in continuous conversation.  

## 🚀 Features  
- 🌟 Chat with any character of your choice  
- 💬 Simple web-based interface  
- 📏 Limits response length for concise conversations  
- ☁️ Easily deployable to Render  

## 📂 Project Structure  
```
📁 nlp-character-chatbot
│── 📁 templates
│   └── index.html          # Web interface for the chatbot
│── app.py                  # Flask application
│── requirements.txt        # Dependencies
│── render.yaml (optional)  # Render deployment config
│── README.md               # Project documentation
```

## 🛠️ Installation & Setup  

### 🔹 Prerequisites  
Ensure you have **Python 3.8+** installed on your machine.  

### 🔹 Clone the Repository  
```sh
git clone https://github.com/Swaraj-sync/ChatChar.git
cd ChatChar
```

### 🔹 Install Dependencies  
```sh
pip install -r requirements.txt
```

### 🔹 Set Up API Key  
You need a valid **Google Gemini API Key** to run the chatbot. Set it as an environment variable:  
```sh
export GEMINI_API_KEY="your_gemini_api_key"
```
For Windows (Command Prompt):  
```sh
set GEMINI_API_KEY=your_gemini_api_key
```

### 🔹 Run the Flask App  
```sh
python app.py
```
The app will be available at **http://127.0.0.1:5000**.

## 🌍 Deploying to Render  

### 🔹 Steps  
1. Push your code to **GitHub/GitLab**.  
2. Log in to [Render](https://dashboard.render.com) and create a **new web service**.  
3. Connect your repository.  
4. Set up the environment variable `GEMINI_API_KEY`.  
5. Configure build and start commands:  
   - **Build Command:** `pip install -r requirements.txt`  
   - **Start Command:** `gunicorn app:app`  
6. Deploy and get a public URL!  

## 🔎 API Usage  

You can also test the chatbot via **cURL** or **Postman**:  
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"character_name":"Sherlock Holmes","user_input":"How do you solve a case?"}' \
     (https://chatchar-fuzu.onrender.com/)
```

## 🏗️ Future Improvements  
✅ Add chat history feature  
✅ Improve response formatting  
✅ Enhance UI with Bootstrap/Tailwind  

## 🤝 Contributing  
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!  
