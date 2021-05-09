from flask import Flask, render_template, request, redirect
from scripts import database
import base64
import uuid

app = Flask(__name__, static_url_path="", static_folder="static", template_folder = "templates")

@app.route('/')
def index():
  return render_template('index.html')

#For Authentication
@app.route('/authenticate')
def authenticate():
  return render_template("authenticate1.html", isVerify=None)

@app.route('/verify_details', methods=['POST'])
def verify_details():
  pwd = database.getPassword(request.form['email'])
  for i in pwd:
    newpwd = i[0]
  if newpwd == request.form['password']:
    return redirect('/facecam')
  else:
    return render_template('authenticate1.html', isVerify=False)

@app.route("/facecam")
def facecam():
  return render_template('authenticate2.html')

#For Registration
@app.route('/register')
def register():
  return render_template("register.html")
  
@app.route('/save_data', methods=['POST'])
def save_data():
  uniqueId = str(uuid.uuid4())
  
  database.addData('user_table', "('" + uniqueId + "','" + request.form['fullname'] + "','" + request.form['number'] + "','" + request.form['email'] + "','" + request.form['dateofbirth'] + "','"+ request.form['address'] + "','" + request.form['password'] + "')")
  
  user = database.showData('user_table', uniqueId)

  return render_template('profile.html', data=user)

@app.route('/success_auth', methods=["POST"])
def successAuth():
  return render_template('successAuth.html')

@app.route('/success_reg', methods=["POST"])
def successReg():
  return render_template('successReg.html')

if __name__ == '__main__':
  app.run(debug=True)