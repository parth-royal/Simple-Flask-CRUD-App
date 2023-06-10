import uuid
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'admin123'

users = []

@app.route("/")
def index():
    return render_template("index.html", datas=users)

@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        user = {'uid': str(uuid.uuid4()), 'uname': uname, 'contact': contact}
        users.append(user)
        flash('User Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        for user in users:
            if user['uid'] == uid:
                user['uname'] = uname
                user['contact'] = contact
                flash('User Updated', 'success')
                return redirect(url_for("index"))
    else:
        for user in users:
            if user['uid'] == uid:
                return render_template("edit_user.html", datas=user)
    return redirect(url_for("index"))

@app.route("/delete_user/<string:uid>", methods=['GET'])
def delete_user(uid):
    for user in users:
        if user['uid'] == uid:
            users.remove(user)
            flash('User Deleted', 'warning')
            break
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
