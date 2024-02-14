from facereference import app
from facereference.util import queryUser


@app.route("/")
def index():
    top = "<h1>FaceReference v0.1</h1>"
    redirect = "<p>Click <a href='user/nolan'>here</a> to see the user page!"
    return top + redirect


@app.route("/user/<username>")
def user(username):
    user = queryUser(username)
    if not user:
        return f'Sorry, but it doesn\'t look like user "{username}" exists.'

    fullname = f"<h2>{user['firstname']} {user['lastname']}</h2>"
    datecreated = f"<h3>Account created {user['datecreated']}</h3>"
    return fullname + datecreated
