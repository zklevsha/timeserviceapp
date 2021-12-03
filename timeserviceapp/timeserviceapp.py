import os
import datetime
import json
from flask import Flask

default_name = "app"
default_port = "5000"


service_name = os.environ.get('SERVICE_NAME', default_name)
port = os.environ.get('PORT', default_port)

app = Flask(__name__)

@app.route('/get-time')
def get_time():
    data = {'service_name': service_name, 
            'current_time_utc': str(datetime.datetime.now())}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)