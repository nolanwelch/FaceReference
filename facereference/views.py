from facereference import app
from facereference.util import queryUser


@app.route("/")
def index():
    top = "<h1>FaceReference v0.1</h1>"
    redirect = "<p>Click <a href='user/nolan'>here</a> to see the user page!"
    return top + redirect


@app.route("/user/<name>")
def user(name):
    data = queryUser(name)
    if not data:
        return f"Sorry, but it doesn't look like user \"{name}\" exists."

    return f"<h2>Hello, {name}!"
