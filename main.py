from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'

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

@app.route('/', methods=['GET','POST'])
def feed():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        message = Feedback(email=email, text=text)
        db.session.add(message)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)