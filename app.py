from flask import Flask, render_template, request, jsonify
from replit import db

app = Flask(__name__)

@app.route("/")
def home():
  items = db.keys()
  return render_template('home.html', items=items)

@app.route("/new-task")
def new_task():
    return render_template('new.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)