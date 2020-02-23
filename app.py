#app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page."

@app.route("/api/v1.0/precipitation")
def precip():
    print("Server received request for 'Precip' page...")
    return "Welcome to my 'Precip' page."

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    return "Welcome to my 'Stations' page."

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'TOBS' page...")
    return "Welcome to my 'TOBS' page."



if __name__ == "__main__":
    app.run(debug=True)
    