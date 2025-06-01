from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        full_name = request.form['full_name']
        country = request.form['country']
        visa_type = request.form['visa_type']
        application_date = request.form['application_date']
        status = request.form['status']
        return f"Form submitted: {full_name}, {country}, {visa_type}, {application_date}, {status}"
    return render_template("submit.html")

@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('show_articles'))
    return render_template('add_article.html')

@app.route('/articles')
def show_articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
