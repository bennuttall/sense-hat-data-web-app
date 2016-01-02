from flask import Flask
import db

app = Flask(__name__)

@app.route('/')
def index():
    d, t, h = db.retreive_data()
    return "Temperature: %s<br>Humidity: %s" % (t, h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
