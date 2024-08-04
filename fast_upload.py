import sys
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    html = """
    <h1>Upload a file</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    """
    return html

@app.route("/", methods=["POST"])
def upload():
    file = flask.request.files["file"]
    filename = file.filename
    if file:
        file.save(filename)
        return "File uploaded successfully, stopping the server."
    else:
        return "No file uploaded"

if __name__ == "__main__":
    app.run()
