"""
Styling points, linestrings, polygons and TOC items.
"""

import os
from simplekml import Kml, ListItemType, Color

kml = Kml(name="Styling", open=1)

# Make all the items into radio buttons
kml.document.liststyle.listitemtype = ListItemType.radiofolder

# Change the icon of the document in the TOC
kml.document.liststyle.itemicon.href = "http://maps.google.com/mapfiles/kml/shapes/parks.png"

# A normal Point with both a LabelStyle and IconStyle
pnt = kml.newpoint(name="Kirstenbosch Normal", description="A style map.", coords=[(18.431486,-33.988)])
pnt.labelstyle.color = 'ff0000ff'
pnt.labelstyle.scale = 2  # Text twice as big
pnt.labelstyle.color = "ffff0000"
pnt.iconstyle.color = 'ffff0000'  # Blue
pnt.iconstyle.scale = 3  # Icon thrice as big
pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/info-i.png'  # Culry 'information i

# A Point with a styleMap. The Text changes from blue to red on mouse over.
pnt = kml.newpoint(name="Kirstenbosch StyleMap", coords=[(18.432314,-33.988862)])
pnt.stylemap.normalstyle.labelstyle.color = 'ffff0000'
pnt.stylemap.highlightstyle.labelstyle.color = 'ff0000ff'

# A red thick LineString
lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                        coords=[(18.43312,-33.98924), (18.43224,-33.98914), (18.43144,-33.98911), (18.43095,-33.98904)])
lin.linestyle.color = Color.red  # Red
lin.linestyle.width = 10  # 10 pixels

# A Polygon with a hole. Half invisible.
pol = kml.newpolygon(name="Atrium Garden",
                     outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004262216968), (18.43410,-33.98972), (18.43371,-33.98952), (18.43348,-33.98985)],
                     innerboundaryis=[(18.43360,-33.98982), (18.43386,-33.98995), (18.43401,-33.98974), (18.43376,-33.98962), (18.43360,-33.98982)])
pol.polystyle.color = '990000ff'  # Red
pol.polystyle.outline = 0



# A Point showing off a BalloonStyle
pnt = kml.newpoint(name="BallonStyle", coords=[(18.429191, -33.987286)])
pnt.balloonstyle.text = "These are trees and this text is blue with a green background."
pnt.balloonstyle.bgcolor = Color.lightgreen
pnt.balloonstyle.textcolor = Color.rgb(0, 0, 255)

# Saving
kml.save(os.path.splitext(__file__)[0] + ".kml")
