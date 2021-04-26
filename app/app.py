from flask import Flask, jsonify
from datetime import datetime
import socket
import urllib.request
import json

app = Flask(__name__)

ip_add='14.140.42.210' # pune city ip address

@app.route('/pucsd')
def myapi():

    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname) 
    now = datetime.now()
        
    # Sending an API request
    response = urllib.request.urlopen("http://ipwhois.app/json/"+ip_add)
    ipgeolocation = json.load(response)

    data=[{
    	"Current Time in IST" : now.strftime("%H:%M:%S"),
	"IP Address" : ip,
	"Hostname" : hostname,
	"City" : ipgeolocation["city"],
	"Region" : ipgeolocation["region"],
	"Country" : ipgeolocation["country"] 
    }]
    return jsonify(data)

if __name__ == '__main__':
    app.run()
