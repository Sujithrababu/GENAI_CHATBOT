from flask import Flask, render_template, request
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Initialize model once
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def AI_bot():
    reply = ""

    if request.method == "POST":
        user_msg = request.form.get("msg")
        reply = model.invoke(user_msg).content

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run()

