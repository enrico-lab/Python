from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/article')
def article():
    return render_template("article.html")

@app.route('/journal')
def journal():
    return render_template("journal.html")

if __name__=="__main__":
    app.run(debug=True)
