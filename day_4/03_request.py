from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

print(__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/czas")
def czas():
    return render_template("data.html", czas=datetime.now())


@app.route("/demo2")
def hello_world2():
    return "<p>Hej - Tu ADAM <hr> W Wersji 2!</p>"

@app.route("/test_req")
def request_test():
    return render_template("req.html",
                           czas=datetime.now(),
                           headers=request.headers,
                           address=request.remote_addr,
                           user=request.remote_user)


if __name__ == "__main__":
    app.run(debug=True)
