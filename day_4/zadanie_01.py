from flask import Flask
from flask import render_template


print(__name__)
app = Flask(__name__)



@app.route("/<value>")
def request_test_danej(value):
    # wykorzystaj moduł https://docs.python.org/3/library/ipaddress.html
    # sprawdź, czy user podał poprawny IP czy nie,
    # wyświetl odpowiednią informację, np.
    # "Podany IP = 192.168.10.3 - jest POPRAWNY"
    # ip = ...
    # user_value = ...
    return render_template("ip.html",
                           user_value=value)

if __name__ == "__main__":
    app.run(debug=True)
