from facereference import app


@app.route("/")
def index():
    return "# FaceReference v0.1"
