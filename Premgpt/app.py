from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# Secure your key using environment variables

API_KEY = os.getenv("API_KEY") 
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

        

        


    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("message")
    try:
        completion = client.chat.completions.create(
            model="provider-2/gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        raw_response = completion.choices[0].message.content 
        print(raw_response)
        return jsonify({"reply": raw_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
