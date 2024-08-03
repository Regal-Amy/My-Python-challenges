import os, time, datetime
from replit import db

print("My Diary")
time.sleep(2)
os.system("clear")

def add():
  time.sleep(2)
  os.system("clear")
  entry = input("Type in your entry: ").capitalize()
  now = datetime.datetime.now()
  now_str = now.strftime("%Y-%m-%d %H:%M:%S")
  timestamp = now_str.lstrip()
  db[timestamp] = entry
  

def view():
  time.sleep(2)
  os.system("clear")
  keys = list (db.keys())
  recent = keys.reverse()
  print(db[keys[1]])

  while keys[2:]:
    time.sleep(2)
    os.system("clear")
    viewPrevious = input("Do you want to view next previous entry? (y/n): ")
    if viewPrevious[0] == 'y':
       print(db[keys[2]])
       keys.pop(1)
    else:
      break
  else:
    print("Entries Exhausted")
  

def menu():
  time.sleep(2)
  os.system("clear")
  menu = input("Do you want to (Add) an entry, (View) entry or (Exit)? ").lower()
  if menu[0] == 'A'.lower():
    add()
  elif menu[0] == 'V'.lower():
    view()
  else:
    print ("Exiting Diary...")
    time.sleep(2)
    return
      
salt = 5467903

while True:
  if len(db) < 0:
    username = input("username: ")
    password = input("password: ")
    db[username] = f"{password}{salt}"
    menu()
  else:
    username = input("input username: ")
    password = input("input password: ")
    keys = list(db.keys())
    if username in keys and db[username] == f"{password}{salt}":
      menu()
      option = input ("Menu or Exit?: ").lower()
      if option[0] == 'm':
        menu()
      else:
        break
    else:
      print("Password Incorrect")