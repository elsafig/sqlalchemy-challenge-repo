from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Set up the database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect database into new model
Base = automap_base()

#Reflect the tables from the database into the model
Base.prepare(autoload_with=engine)

#Save references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#Set up Flask
app = Flask(__name__)

# @app.route("/api/v1.0/json-list")
# def json_list():
#     session = Session(engine)
#     combined = 
#     return jsonify()
@app.route("/")
def home():
    return (
        f"SurfsUp Welcome Page</br></br>"
        f"Available routes are:</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end>")


@app.route("/api/v1.0/precipitation")
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value. Return JSON
def precipitaion():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-06-23').all()
    
    all_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
#Return a JSON list of stations from the dataset.
def stations():
    session = Session(engine)
    station_results= session.query(Measurement.station).distinct().all()
    f"Return the stations data as json"
    all_stations = list(np.ravel(station_results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
#Returns jsonified data for the most active station (USC00519281) (3 points)
#Only returns the jsonified data for the last year of data (3 points)
def tobs():
    session = Session(engine)
    results = session.query(Measurement.station, Measurement.tobs).\
    filter(Measurement.date>='2016-06-23').\
    filter(Measurement.station == 'USC00519281') 

    pop_tobs=[]
    for station, tobs in results:
        tobs_dict = {}
        tobs_dict["station"] = station
        tobs_dict["tobs"] = tobs
        pop_tobs.append(tobs_dict)
    return jsonify(pop_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    """Fetch min, max, and average temperatures calculated from the given start date to the end of the dataset, or a 404 if not."""
    input_date = start
    for 



    session = Session(engine)
    results = session.query(func.max(Measurement.tobs).label('max'),
      func.min(Measurement.tobs).label('min'),
      func.avg(Measurement.tobs).label('avg')).\
    filter(Measurement.date>='2016-06-23').\
    filter(Measurement.station == 'USC00519281')
    
    canonicalized = start.replace(" ", "").lower()
    for date in results:
        search_term = character["real_name"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404

@app.route("/api/v1.0/<start>/<end>")
def start(start, end):

if __name__ == "__main__":
    app.run(debug=True)


