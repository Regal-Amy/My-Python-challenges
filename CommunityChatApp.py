#Building a Community chat app
from flask import Flask, request, redirect, session
import os
from replit import db
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

def message():
  entry = ""
  with open("template/messages.html", "r") as f:
    entry = f.read()
  keys = db.keys()
  keys = list(keys)
  content = ""
  count = 0
  for key in reversed(keys):
    count += 1
    newEntry = entry
    newEntry = newEntry.replace("{username}", db[key]["username"])
    newEntry = newEntry.replace("{user id}", db[key]["user id"])
    newEntry = newEntry.replace("{message}", db[key]["message"])
    content += newEntry
    if count == 5:
      break
  return content

@app.route('/')
def index():
  if session.get('user_id'):
    return redirect("/chatpage")
  if 'X-Replit-User-Id' in request.headers:
    user_id = request.headers['X-Replit-User-Id']
    session['user_id'] = user_id
    session['username'] = request.headers['X-Replit-User-Name']

  page = ""
  with open ("template/login.html", "r") as f:
    page += f.read()
  return page

@app.route('/chatpage')
def chatPage():
  if not request.headers["X-Replit-User-Id"]:
    return redirect("/")
  page = ""
  page += f"""<h1>Community Chat</h1>"""
  page += f"""You are logged in as {request.headers["X-Replit-User-Name"]}"""
  with open ("template/chat.html", "r") as f:
    page += f.read()

  page = page.replace("{content}", message())
  return page

@app.route("/add", methods=["POST"])
def add():
  form = request.form
  date = datetime.datetime.now().isoformat()
  entry = {
    "username": request.headers['X-Replit-User-Name'],
    "user id": request.headers["X-Replit-User-Id"], "message": form["message"],
    "date": date
  }
  db[date] = entry
  return redirect("/chatpage")

   
@app.route("/logout")
def logout():
  response = redirect('/')
  response.delete_cookie('user_id')
  response.delete_cookie('username')

  return response

@app.route('/admin')
def admin():
  if "X-Replit-User-Id" == 34597691: 
    return redirect('/')
  return "Admin Page - Only visible to you."

@app.route('/delete/<key>', methods=["POST"])
def delete(key):
  if "X-Replit-User-Id" == 34597691: 
    return redirect('/')

  if key in db:
    del db[key]
  return redirect('/chatpage')

  
app.run(host='0.0.0.0', port=81)
