from flask import Flask, render_template, request
from model import predict_overthinking   # 🔥 import AI model

app = Flask(__name__)

# Questions
questions = [
    "Do you overthink small decisions?",
    "Do you worry about the future?",
    "Do you replay past events?",
    "Do you feel mentally tired?",
    "Do you fear making wrong choices?"
]

# 🔹 Home Module
@app.route('/')
def home():
    return render_template('home.html')


# 🔹 Test Module
@app.route('/test')
def test():
    return render_template('test.html', questions=questions)


# 🔹 Result Module (UPDATED WITH AI)
@app.route('/result', methods=['POST'])
def result():
    answers = request.form.getlist('answers')

    # Convert Yes/No → 1/0
    data = [1 if a == 'yes' else 0 for a in answers]

    # 🔥 Call AI model
    level, bert_output = predict_overthinking(data)

    return render_template(
        'result.html',
        level=level,
        bert=bert_output
    )


# 🔹 Progress Module
@app.route('/progress')
def progress():
    scores = [60, 70, 80, 75]
    avg = sum(scores) / len(scores)
    return render_template('progress.html', avg=avg)


# 🔹 Tools Module
@app.route('/tools')
def tools():
    return render_template('tools.html')


# 🔹 Motivation Module
@app.route('/motivation')
def motivation():
    quotes = [
        "You are not your thoughts.",
        "Stay calm and focused.",
        "Control your mind, control your life."
    ]
    return render_template('motivation.html', quotes=quotes)


# 🔹 Run App
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)