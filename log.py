import re
from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from werkzeug import generate_password_hash,check_password_hash,secure_filename

app=Flask(__name__)

mysql=MySQL()
#app.config[‘UPLOAD_FOLDER’]
#app.config[‘MAX_CONTENT_PATH’] For the max size of file that loading!
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='nezahat123'
app.config['MYSQL_DB']='login_data'
mysql.init_app(app)
#app= Flask(__name__)
#MySQLdb=MySQL()
#uploader will be succesfull when this part is finished.    
@app.route('/uploader', methods = ['GET', 'POST'])
def now_upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #return render_template("upload.html", title="You loaded the file succesfully")
      return 'file uploaded successfully'
#@app.route('/upload')
#def upload_file():
 #  return render_template('upload.html')

def is_email_address_valid(email):
    """Validate the email address using a regex."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True

@app.route("/")
def index():
    return render_template("index.html", title="Create User")
#conn= MySQLdb.connect(host="localhost",user="root",password="nezahat123",db="login_data")



@app.route("/signup",methods=["POST"])
def signup():
    
    email=str(request.form["email"])
    username= str(request.form["user"])	  
    password= str(request.form["password"])
    resultmail=is_email_address_valid(email)
    print("regex result ----- ")
    print(resultmail)
    hashpassword=generate_password_hash(password)

    if resultmail==True:

     cursor= mysql.connection.cursor()
     cursor.execute("INSERT INTO user (name,password,email) VALUES(%s,%s,%s)",(username,hashpassword,email))
     mysql.connection.commit()
    else:
     return render_template("index.html",title="parola hatali")

    return "signup is succesfull"

@app.route("/login")
def login():
    return render_template("login.html",title="data")

        
if __name__=="__main__":
   app.run(debug=True)



