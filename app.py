from flask import Flask, render_template, request
from model import predict_overthinking  
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Questions
questions = [
    "Do you overthink small decisions?",
    "Do you worry about the future?",
    "Do you replay past events?",
    "Do you feel mentally tired often?",
    "Do you fear making wrong choices?",
    "Do you imagine worst-case scenarios frequently?",
    "Do you find it hard to relax your mind?",
    "Do you overanalyze conversations?",
    "Do you struggle to sleep due to thinking?",
    "Do you doubt your decisions often?",
    
    "Do you feel anxious without clear reason?",
    "Do you compare yourself with others a lot?",
    "Do you overthink what others think about you?",
    "Do you feel stuck in negative thoughts?",
    "Do you keep planning but not acting?",
    "Do you worry about things beyond your control?",
    "Do you replay embarrassing moments repeatedly?",
    "Do you feel overwhelmed by your thoughts?",
    "Do you hesitate to make decisions?",
    "Do you overthink your mistakes?",
    
    "Do you feel pressure to be perfect?",
    "Do you worry about things that haven’t happened yet?",
    "Do you feel mentally drained after thinking too much?",
    "Do you struggle to stay present in the moment?",
    "Do you question your choices repeatedly?",
    "Do you fear judgment from others?",
    "Do you feel restless due to thoughts?",
    "Do you get stuck analyzing situations repeatedly?",
    "Do you find it hard to stop worrying?",
    "Do you feel your thoughts are uncontrollable?"
]
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER['username'] and password == USER['password']:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')
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