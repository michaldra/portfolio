from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)

@app.route('/', methods=['POST'])
def feed():
    email = request.form['email']
    text = request.form['text']
    with open('feedback.txt', 'a', encoding='utf-8') as f:
        f.write("Email: ", email + '\n' + "Wiadomość: ",text + '\n')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)