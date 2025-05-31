from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("layout.html")

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

if __name__ == "__main__":
    app.run(debug=True)
