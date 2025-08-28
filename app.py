from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form.get("name")
    job_title = request.form.get("job_title")
    skills = request.form.get("skills")

    # Temporary placeholder (we'll wire real AI next)
    resume = (
        f"{name}\n\nTarget Role: {job_title}\n\nSkills: {skills}\n\n"
        "Experience:\n- Describe your recent role and achievements here.\n"
        "- Add metrics (e.g., increased sales by 20%, reduced costs by 15%).\n"
    )

    cover_letter = (
        f"Dear Hiring Manager,\n\nI’m excited to apply for the {job_title} role. "
        f"My background and skills in {skills} make me a strong fit. "
        "I’m eager to contribute measurable impact to your team.\n\n"
        "Sincerely,\n"
        f"{name}"
    )

    return render_template("result.html", resume=resume, cover_letter=cover_letter)

if __name__ == "__main__":
    app.run(debug=True)
