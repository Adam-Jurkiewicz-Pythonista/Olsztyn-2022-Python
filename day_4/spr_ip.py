from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import ipaddress

app = Flask(__name__)


@app.route("/", defaults={'user_ip': ...})
@app.route('/<user_ip>')
def test_ip(user_ip):
    data = datetime.now().strftime("%c")
    remote_ip = request.remote_addr
    if user_ip is Ellipsis:
        return  render_template("spr_remote.html",
                                kiedy=data,
                                ip_to_check=remote_ip,
                                headers=request.headers,
                                )
    else:
        try:
            ip_ok = ipaddress.ip_address(user_ip)
            dane_geoip = {}
            return render_template("spr_ok.html",
                                   kiedy=data,
                                   ip_to_check=user_ip,
                                   headers=request.headers,
                                   dane_geo=dane_geoip,
                                   )
        except Exception as e:
            return render_template("spr_error.html",
                                   kiedy=data,
                                   ip_to_check=user_ip,
                                   headers=request.headers,
                                   error=e,
                                   )


if __name__ == "__main__":
    app.run(debug=True)
