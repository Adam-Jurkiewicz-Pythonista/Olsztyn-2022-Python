from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import ipaddress
import requests as api_get

app = Flask(__name__)

def spr_geoip(ip: str) -> dict:
    base_url = f"http://api.ipstack.com/{ip}?access_key=e9e50_your_access_key"
    # for free access: https://ipstack.com/signup/free
    try:
        api_response = api_get.get(base_url)
    except Exception as e:
        return {'error': e}

    return {'ok': api_response.json()}


@app.route("/", defaults={'user_ip': ...})
@app.route('/<user_ip>')
def test_ip(user_ip):
    data = datetime.now().strftime("%c")
    remote_ip = request.remote_addr

    """
    {"ip": "134.201.250.155", 
    "type": "ipv4", 
    "continent_code": "NA", 
    "continent_name": "North America", 
    "country_code": "US", 
    "country_name": "United States", 
    "region_code": "CA", 
    "region_name": "California", 
    "city": "Los Angeles", 
    "zip": "90012", 
    "latitude": 34.0655517578125, 
    "longitude": -118.24053955078125, 
    "location": 
        {"geoname_id": 5368361, 
        "capital": "Washington D.C.", 
        "languages": 
            [
                {"code": "en", "name": "English", "native": "English"}], 
                "country_flag": "https://assets.ipstack.com/flags/us.svg", "country_flag_emoji": "\ud83c\uddfa\ud83c\uddf8", "country_flag_emoji_unicode": "U+1F1FA U+1F1F8", "calling_code": "1", "is_eu": false}}
    """
    if user_ip is Ellipsis:
        gateway_ip = api_get.get("https://api.ipify.org/")
        dane_geoip = spr_geoip(gateway_ip.text)
        return  render_template("spr_ok.html",
                                kiedy=data,
                                ip_to_check=remote_ip,
                                headers=request.headers,
                                dane_geo=dane_geoip,
                                )
    else:
        try:
            ip_ok = ipaddress.ip_address(user_ip)
            dane_geoip = spr_geoip(user_ip)
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
