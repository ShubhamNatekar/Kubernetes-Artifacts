from flask import Flask, jsonify
from datetime import datetime
import socket
import json

app = Flask(__name__)

@app.route('/pucsd')
def myapi():

    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname) 
    now = datetime.now()
        
    data=[{
    	"Current Time in IST" : now.strftime("%H:%M:%S"),
	"IP Address" : ip,
	"Hostname" : hostname,
	"City" : "Pune",
	"Region" : "Maharashtra",
	"Country" : "India" 
    }]
    return jsonify(data)

if __name__ == '__main__':
    app.run()
