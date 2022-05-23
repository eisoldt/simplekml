"""
A collection of various features and stylings.
"""
import os

from simplekml import *

# Create an instance of Kml
kml = Kml(name="Various")

# Change the top level feature from a document to a folder
kml.document = Folder(name="Various", open=1)

#A NetworkLink
netlink = kml.newnetworklink(name="Broken NetworkLink")
netlink.link.href = "http://www.foobar.com/foo/bar.kml"

#A Document
doc = kml.newdocument()
doc.liststyle.listitemtype = ListItemType.radiofolder
doc.name = "Document"
doc.visibility = 1
doc.open = 1
doc.atomauthor = "Kyle Lancaster"
doc.atomlink = "http://code.google.com/p/simplekml/wiki/Document"
doc.address = "Cape Town, South Africa"
doc.phonenumber = "555-1234"
doc.snippet.content = "Snippet content that should be more than one line, hopefully"
doc.snippet.maxlines = 1
doc.description = "A document description."
doc.timestamp.when = "2011"

# A folder
fol = kml.newfolder(name="Geometry")
fol.open = 1

# A Point
pnt = fol.newpoint(name="Point", coords=[(1.0,1.0,0.0)])
pnt.extrude = 1
pnt.altitudemode = AltitudeMode.relativetoground
pnt.camera = Camera(longitude=1.0, latitude=1.0, altitude=20000, heading=45, tilt=10, altitudemode=AltitudeMode.relativetoground)
pnt.camera.gxtimestamp.when = "2010"
pnt.iconstyle.hotspot = HotSpot(x=0.5,y=0.5,xunits=Units.fraction,yunits=Units.fraction)

# A Linestring
lin = fol.newlinestring(name="LineString", coords=[(1.01,1.01,100),(1.12,1.12,100)])
lin.altitudemode = AltitudeMode.relativetoground
lin.lookat = LookAt(longitude=1.05,latitude=1.05,altitude=50000,tilt=5,altitudemode=AltitudeMode.relativetoground, range=50)
lin.tessellate = 1
lin.extrude = 1

# A Model
model = kml.newmodel(name="Model", description="Model placemark without a model!")
model.location.latitude = 1
model.location.longitude = 1

# Create a placemark with an address but no geometry
place = kml.newplacemark(name="Google Headquarters", address="1600 Amphitheatre Parkway, Mountain View, CA",
                         description="Located in Mountain View, California")

# Saving
kml.save(os.path.splitext(__file__)[0] + ".kml")