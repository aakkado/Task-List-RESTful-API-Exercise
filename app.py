from flask import Flask, render_template, request, jsonify, redirect
from replit import db

app = Flask(__name__)

@app.route("/")
def home():
  items = db.keys()
  return render_template('home.html', items=items)

@app.route("/add-task", methods=['POST'])
def add_task():
  task = request.form.get("task")
  description = request.form.get("description")
  if task or description == '':
    return redirect("/")
  db[task] = description
  return redirect("/")

@app.route("/new-task")
def new_task():
    return render_template('new.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)