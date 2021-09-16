"""
How to use simplekml.
"""

import os
from simplekml import Kml

kml = Kml(name="Usage", open=1) # open=1 just opens the document in the TOC (table of contents). Not a necessary step.

# A simple Point
kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])

# A simple Linestring showing off HTML markup
lin = kml.newlinestring(name="Pathway", description="A pathway in <b>Kirstenbosch</b>",
                        coords=[(18.43312,-33.98924), (18.43224,-33.98914), (18.43144,-33.98911), (18.43095,-33.98904)])

# A simple Polygon with a hole in it.
pol = kml.newpolygon(name="Atrium Garden",
                     outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004262216968), (18.43410,-33.98972), (18.43371,-33.98952), (18.43348,-33.98985)],
                     innerboundaryis=[[(18.43360,-33.98982), (18.43386,-33.98995), (18.43401,-33.98974), (18.43376,-33.98962), (18.43360,-33.98982)]])

# Saving
kml.save(os.path.splitext(__file__)[0] + ".kml")
#kml.savekmz(os.path.splitext(__file__)[0] + ".kmz") # uncomment to save to kmz
#print(kml.kml()) # uncomment to see the kml printed to screen
