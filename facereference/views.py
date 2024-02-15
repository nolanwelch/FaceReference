from facereference import app
from facereference.util import queryUser, queryImage
from flask import request


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


@app.route("/search", methods=["GET"])
def search():
    if request.is_json:
        pass


@app.route("/image/<id>")
def image(id):
    img = queryImage(id)
    if img:
        html = f"<h1>Image #{img['id']}</h1>"
        html += f"<img src=\"{img['uri']}\">"
        html += f"<p>{img['alttext']}</p>"
        return html
    return f"Image #{id} not found."
