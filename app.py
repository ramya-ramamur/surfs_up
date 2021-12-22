# Import Python dependencies
import datetime as dt
#import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependency
from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create the classes variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#set up flask
app = Flask(__name__)
@app.route('/')

#add the precipitation, stations, tobs, and temp routes
def welcome():
    return(
    f"Welcome to the Climate Analysis API!<br/>"
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/temp/start/end<br/>"
    )

#Precipitation Route
@app.route('/api/v1.0/precipitation')    
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)