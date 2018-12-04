from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/newuser", methods=["POST"])
def newu():
    query = "INSERT INTO users (fname, lname, email) VALUES (%(f)s, %(l)s, %(m)s);"
    data = {
            'f': request.form['fname'],
            'l': request.form['lname'],
            'm': request.form['mail']
        }
    db = connectToMySQL('user_list')
    id = db.query_db(query, data)
    

    return redirect("/read")

@app.route("/goto")
def go():
    mysql = connectToMySQL('user_list')
    return render_template("newuser.html")

@app.route("/one/<id1>")
def oneuser(id1):
    mysql = connectToMySQL('user_list')
    oneuser = mysql.query_db('SELECT * FROM users WHERE id=%s', (id1))
    print(oneuser)

    return render_template("one.html", use = oneuser)
    

@app.route("/read")
def index():
    mysql = connectToMySQL('user_list')
    allusers = mysql.query_db('SELECT * FROM users;')
    print(allusers)
    
    return render_template("userlist.html", users = allusers)

if __name__ == "__main__":
    app.run(debug=True)
