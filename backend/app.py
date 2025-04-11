from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

# Preloaded motivational quotes
quotes = [
    "Push harder than yesterday if you want a different tomorrow.",
    "Success is not for the lazy.",
    "Your only limit is your mind.",
    "Stay focused and never give up!",
    "Dream. Believe. Do. Repeat.",
]

@app.route("/generate", methods=["POST"])
def generate():
    class_name = request.form.get("className", "Student")
    quote = request.form.get("quote")

    # If no custom quote, use AI/preloaded quote
    if not quote:
        quote = random.choice(quotes)

    template_type = request.form.get("templateType", "image")

    # Save uploaded logo (optional)
    if "logo" in request.files:
        logo = request.files["logo"]
        logo_path = os.path.join("..", "assets", logo.filename)
        logo.save(logo_path)
    else:
        logo_path = None

    # Simulate generation
    result = {
        "class_name": class_name,
        "quote_used": quote,
        "type": template_type,
        "logo_path": logo_path,
        "message": f"{template_type.capitalize()} generated successfully for {class_name}!",
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
