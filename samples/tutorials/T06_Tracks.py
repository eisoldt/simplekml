"""
This is a recreation of the example found in the KML Reference: http://code.google.com/apis/kml/documentation/kmlreference.html#gxtrack The unnecessary styling has not been implemented, but if you compare the KML References example in Google Earth to this example you should see no difference whatsoever (except for id values).
"""

import os
from simplekml import Kml, Snippet, Types

# Data for the track
when = ["2010-05-28T02:02:09Z",
    "2010-05-28T02:02:35Z",
    "2010-05-28T02:02:44Z",
    "2010-05-28T02:02:53Z",
    "2010-05-28T02:02:54Z",
    "2010-05-28T02:02:55Z",
    "2010-05-28T02:02:56Z"]

coord = [(-122.207881,37.371915,156.000000),
    (-122.205712,37.373288,152.000000),
    (-122.204678,37.373939,147.000000),
    (-122.203572,37.374630,142.199997),
    (-122.203451,37.374706,141.800003),
    (-122.203329,37.374780,141.199997),
    (-122.203207,37.374857,140.199997)]

cadence = [86, 103, 108, 113, 113, 113, 113]
heartrate = [181, 177, 175, 173, 173, 173, 173]
power = [327.0, 177.0, 179.0, 162.0, 166.0, 177.0, 183.0]

# Create the KML document
kml = Kml(name="Tracks", open=1)
doc = kml.newdocument(name='GPS device', snippet=Snippet('Created Wed Jun 2 15:33:39 2010'))
doc.lookat.gxtimespan.begin = '2010-05-28T02:02:09Z'
doc.lookat.gxtimespan.end = '2010-05-28T02:02:56Z'
doc.lookat.longitude = -122.205544
doc.lookat.latitude = 37.373386
doc.lookat.range = 1300.000000

# Create a folder
fol = doc.newfolder(name='Tracks')

# Create a schema for extended data: heart rate, cadence and power
schema = kml.newschema()
schema.newgxsimplearrayfield(name='heartrate', type=Types.int, displayname='Heart Rate')
schema.newgxsimplearrayfield(name='cadence', type=Types.int, displayname='Cadence')
schema.newgxsimplearrayfield(name='power', type=Types.float, displayname='Power')

# Create a new track in the folder
trk = fol.newgxtrack(name='2010-05-28T01:16:35.000Z')

# Apply the above schema to this track
trk.extendeddata.schemadata.schemaurl = schema.id

# Add all the information to the track
trk.newwhen(when) # Each item in the give nlist will become a new <when> tag
trk.newgxcoord(coord) # Ditto
trk.extendeddata.schemadata.newgxsimplearraydata('heartrate', heartrate) # Ditto
trk.extendeddata.schemadata.newgxsimplearraydata('cadence', cadence) # Ditto
trk.extendeddata.schemadata.newgxsimplearraydata('power', power) # Ditto

# Styling
trk.stylemap.normalstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
trk.stylemap.normalstyle.linestyle.color = '99ffac59'
trk.stylemap.normalstyle.linestyle.width = 6
trk.stylemap.highlightstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
trk.stylemap.highlightstyle.iconstyle.scale = 1.2
trk.stylemap.highlightstyle.linestyle.color = '99ffac59'
trk.stylemap.highlightstyle.linestyle.width = 8

# Save the kml to file
kml.save(os.path.splitext(__file__)[0] + ".kml")