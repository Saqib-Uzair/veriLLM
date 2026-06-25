from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    code = ""

    if request.method == "POST":

        code = request.form["code"]

        prompt = f"""
        You are an advanced static code analyzer.

        Analyze the following code and provide:

        1. Possible Bugs
        2. Security Issues
        3. Performance Problems
        4. Code Quality Suggestions
        5. Complexity Analysis
        6. Suggested Improvements

        Code:
        {code}
        """

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            result = response.text

        except Exception as e:
            result = f"Error: {e}"

    return render_template(
        "index.html",
        result=result,
        code=code
    )

if __name__ == "__main__":
    app.run(debug=True)