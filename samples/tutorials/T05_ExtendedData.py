"""
This shows the use of the 3 different types of extended data: Data, Simple Data and Simple Array Data, as well as prettying up the data.
"""

import os
from simplekml import Kml, Types, Snippet, Color

# The KML
kml = Kml(name="ExtendedData", open=1)

# Data Example---------------------------------------------------------------------------------------------------------
# Create and style a point
pnt = kml.newpoint(name='1. World of Birds (Data)', coords =[(18.361960,-34.016543)])
pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/1.png'

# Add the Data to the point
pnt.extendeddata.newdata(name='birds', value=400, displayname="Bird Species")
pnt.extendeddata.newdata(name='aviaries', value=100, displayname="Aviaries")
pnt.extendeddata.newdata(name='visitors', value=10000, displayname="Annual Visitors")


# Simple Data Example -------------------------------------------------------------------------------------------------
# Create a schema
schema = kml.newschema(name='WOW')

schema.newsimplefield(name='birds', type='int', displayname='Bird Species')
schema.newsimplefield(name='aviaries', type='int', displayname='Aviaries')
schema.newsimplefield(name='visitors', type='int', displayname='Annual Visitors')

# Create and style a point
pnt = kml.newpoint(name='2. World of Birds (Simple Data)', coords =[(18.361960,-34.017224)])
pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/2.png'
# Uncomment the following line to display the data in a prettier format than the default table
#pnt.balloonstyle.text = """$[WOW/visitors] <b>$[WOW/visitors/displayName]</b> come to the World of Birds to walk through $[WOW/aviaries] <b>$[WOW/aviaries/displayName]</b> to see $[WOW/birds] <b>$[WOW/birds/displayName]</b>."""

# Add extended data to the point
pnt.extendeddata.schemadata.schemaurl = schema.id
pnt.extendeddata.schemadata.newsimpledata('birds', 400)
pnt.extendeddata.schemadata.newsimpledata('aviaries', 100)
pnt.extendeddata.schemadata.newsimpledata('visitors', 10000)


# Simple Array Data Example -------------------------------------------------------------------------------------------
# Create a new schema
schema = kml.newschema(name='Walk')
schema.newgxsimplearrayfield(name='birdseen', type=Types.int, displayname='Birds Seen')

# Create and style a point
coords = [(18.36271305597591,-34.01792707074279,0),
    (18.36249939144205,-34.01762728515967,0),
    (18.36247681257987,-34.01736644626698,0),
    (18.36237928017156,-34.01723665897296,0),
    (18.36223391902398,-34.0172544563783,0),
    (18.36203086107577,-34.01693989513787,0)]
when = ["2010-05-28T02:00:00Z",
        "2010-05-28T02:10:00Z",
        "2010-05-28T02:20:00Z",
        "2010-05-28T02:30:00Z",
        "2010-05-28T02:40:00Z",
        "2010-05-28T02:50:00Z"]

# Create the gx:Track and style it
trk = kml.newgxtrack(name='3. World of Birds (Simple Array Data)')
trk.snippet = Snippet('Click anywhere on the line or open the elevation profile to view the extended data.', 4)
trk.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/3.png'
trk.liststyle.itemicon.href = 'http://maps.google.com/mapfiles/kml/paddle/3.png'
trk.linestyle.width = 3
trk.linestyle.color = Color.red

# Add the coordinates
trk.newgxcoord(coords)
# Add the time
trk.newwhen(when)

# Add extended data to the point (view the elevation profile in Google Earth to see the data)
trk.extendeddata.schemadata.schemaurl = schema.id
trk.extendeddata.schemadata.newgxsimplearraydata('birdseen', [5,8,10,15,20,30])


# Finally save the KML to file
kml.save(os.path.splitext(__file__)[0] + ".kml")
