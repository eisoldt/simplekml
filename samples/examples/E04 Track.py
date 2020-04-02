"""
Example demonstrating how to use gx:Track with a model.
"""

import os
from simplekml import Kml, Model, AltitudeMode, Orientation, Scale

# Coordinates and timestamps to be used to locate the car model in time and space
car_info = {"coord" : [
                       (-1.205638094515976,52.86427051097027,0), 
                       (-1.205381150785744,52.86520449509131,0), 
                       (-1.205070556273065,52.8658866187436,0), 
                       (-1.20506114704183,52.86601843957955,0), 
                       (-1.20512625833175,52.86623139261676,0), 
                       (-1.205294145395112,52.86643197457281,0), 
                       (-1.205676706574317,52.86711097792102,0), 
                       (-1.205866919720511,52.86749802242012,0), 
                       (-1.205978077903859,52.86792708892633,0), 
                       (-1.2060237987725,52.86819270231999,0), 
                       (-1.205983883148774,52.86826739196837,0), 
                       (-1.205580187462454,52.86858138867128,0), 
                       (-1.204746927391411,52.8692086964254,0), 
                       (-1.204087156570155,52.86976390388508,0), 
                       (-1.20376709054747,52.87001624614373,0), 
                       (-1.203122645607228,52.87034182188007,0), 
                       (-1.202747641987371,52.8705296795463,0)
                    ] ,
                "when" :  [
                    "2008-07-14T00:00:00Z",
                    "2008-07-14T00:00:30Z",
                    "2008-07-14T00:01:00Z",
                    "2008-07-14T00:01:30Z",
                    "2008-07-14T00:02:00Z",
                    "2008-07-14T00:02:30Z",
                    "2008-07-14T00:03:00Z",
                    "2008-07-14T00:03:30Z",
                    "2008-07-14T00:04:00Z",
                    "2008-07-14T00:04:30Z",
                    "2008-07-14T00:05:00Z",
                    "2008-07-14T00:05:30Z",
                    "2008-07-14T00:06:00Z",
                    "2008-07-14T00:06:30Z",
                    "2008-07-14T00:07:00Z",
                    "2008-07-14T00:07:30Z",
                    "2008-07-14T00:08:00Z",
                    ]
} 

# The model path and scale variables
car_dae = r'http://simplekml.googlecode.com/hg/samples/resources/car-model.dae'
car_scale = 1.0

# Create the KML document
kml = Kml(name="Car", open=1)

# Create the model
model_car = Model(altitudemode=AltitudeMode.clamptoground,
                            orientation=Orientation(heading=75.0),
                            scale=Scale(x=car_scale, y=car_scale, z=car_scale))

# Create the track
trk = kml.newgxtrack(name="Car Track", altitudemode=AltitudeMode.clamptoground,
                     description="Model from: http://sketchup.google.com/3dwarehouse/details?mid=88a57c5396d3703dec0b522a48034ff2")

# Attach the model to the track
trk.model = model_car
trk.model.link.href = car_dae

# Add all the information to the track
trk.newwhen(car_info["when"])
trk.newgxcoord(car_info["coord"])

# Turn-off default icon and text and hide the linestring
trk.iconstyle.icon.href = ""
trk.labelstyle.scale = 0
trk.linestyle.width = 0

# Saving
kml.save(os.path.splitext(__file__)[0] + ".kml")
#kml.savekmz(os.path.splitext(__file__)[0] + ".kmz") # uncomment to save to kmz
#print kml.kml() # uncomment to see the kml printed to screen
