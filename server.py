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
    oneuser = mysql.query_db('SELECT * FROM users WHERE id= %s' % id1)
    # SELECT MAX(id) FROM users
    #oneuser = mysql.query_db('SELECT * FROM users WHERE id=2')
    print(oneuser)

    return render_template("one.html", use = oneuser)

@app.route("/edit")
def goto():
    mysql = connectToMySQL('user_list')
    return render_template("updateuser.html")

@app.route("/edituser/<id2>", methods=["POST"])
def edit(id2):
    mysql = connectToMySQL('user_list')
    #edituser = mysql.query_db('SELECT * FROM users WHERE id = %s' % id2)
    edituser = mysql.query_db('SELECT * FROM users WHERE id = 2')
    print(edituser)

    return redirect('userlist.html', us = edituser)
    

@app.route("/read")
def index():
    mysql = connectToMySQL('user_list')
    allusers = mysql.query_db('SELECT * FROM users;')
    print(allusers)
    
    return render_template("userlist.html", users = allusers)

if __name__ == "__main__":
    app.run(debug=True)
