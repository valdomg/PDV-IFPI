from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('home.html')



if __name__ == "__main__":
  app.run()