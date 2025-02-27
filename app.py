import os
from flask import Flask, request, render_template, session
from google import genai
from google.genai import types

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24).hex())

# Configure Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Helper to convert session history to GenAI format
def to_genai_messages(history):
    return [
        types.Content(
            role=msg["role"],
            parts=[types.Part(text=part["text"]) for part in msg["parts"]]
        ) for msg in history
    ]

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        if "character" not in session:
            # Initialize character
            character = request.form["character_name"].strip()
            session["character"] = character
            session["history"] = [
                {
                    "role": "user",
                    "parts": [{
                        "text": f"You are {character}. Stay in character, "\
                                "maintain continuity, and never break character."
                    }]
                }
            ]
            
            # Generate initial response
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=to_genai_messages(session["history"]),
                    config=types.GenerateContentConfig(
                        temperature=0.9,
                        max_output_tokens=8192
                    )
                )
                session["history"].append({
                    "role": "model",
                    "parts": [{"text": response.text if hasattr(response, 'text') else 
                              f"Greetings! I am {character}. How may I assist you?"}]
                })
            except Exception as e:
                session["history"].append({
                    "role": "model",
                    "parts": [{"text": f"Error: {str(e)}"}]
                })
        else:
            # Handle ongoing conversation
            session["history"].append({
                "role": "user",
                "parts": [{"text": request.form["user_input"].strip()}]
            })
            
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=to_genai_messages(session["history"]),
                    config=types.GenerateContentConfig(
                        temperature=0.9,
                        max_output_tokens=8192
                    )
                )
                session["history"].append({
                    "role": "model",
                    "parts": [{"text": response.text if hasattr(response, 'text') else 
                              "I need to consult the stars... (response error)"}]
                })
            except Exception as e:
                session["history"].append({
                    "role": "model",
                    "parts": [{"text": f"Error: {str(e)}"}]
                })
            
            # Keep last 5 exchanges + system prompt
            if len(session["history"]) > 11:
                session["history"] = session["history"][:1] + session["history"][-10:]

    return render_template(
        "chat.html",
        character=session.get("character"),
        messages=session.get("history", [])[1:]  # Skip system prompt
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
