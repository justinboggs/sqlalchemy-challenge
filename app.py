import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-13<br/>"
        f"/api/v1.0/2017-08-13/2017-08-23"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    last_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    return jsonify(last_precip)    

@app.route("/api/v1.0/stations")
def station():

    session = Session(engine)

    station_list = session.query(Measurement.station).distinct().all()

    session.close()

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    new_df2 = session.query(Measurement.station, Measurement.tobs).filter(Measurement.date >= '2016-08-23').filter(Measurement.station == 'USC00519281').all()

    session.close()

    return jsonify(new_df2)



@app.route("/api/v1.0/2017-08-13")
def first():
    session = Session(engine)

    averages = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    start_date = session.query(*averages).filter(Measurement.date >= "2017-08-23").all()

    session.close()

    return jsonify(start_date)

@app.route("/api/v1.0/2017-08-13/2017-08-23")
def second():
    session = Session(engine)

    averages2 = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    start_end = session.query(*averages2).filter(Measurement.date >= "2017-08-23").all()

    session.close()

    return jsonify(start_end)

if __name__ == "__main__":
    app.run(debug=True)