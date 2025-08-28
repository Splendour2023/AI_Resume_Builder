from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads OPENAI_API_KEY from .env

app = Flask(__name__)

# Create OpenAI client (will read api_key from env if not passed)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        role = request.form.get("role", "").strip()
        skills = request.form.get("skills", "").strip()
        experience = request.form.get("experience", "").strip()  # optional

        # Build prompts
        resume_prompt = (
            f"Create a professional resume for {name} applying for a {role} role. "
            f"Highlight these skills: {skills}. Include a short experience section: {experience}."
        )

        cover_prompt = (
            f"Write a concise, professional cover letter for {name} for a {role} role. "
            f"Mention skills: {skills} and briefly reference this experience: {experience}."
        )

        # Use the new chat completions API
        resume_resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": resume_prompt}],
            max_tokens=700,
            temperature=0.2,
        )

        cover_resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": cover_prompt}],
            max_tokens=450,
            temperature=0.2,
        )

        # Extract the text out of responses
        resume = resume_resp.choices[0].message.content.strip()
        cover_letter = cover_resp.choices[0].message.content.strip()

        return render_template("result.html", name=name, role=role, resume=resume, cover_letter=cover_letter)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
