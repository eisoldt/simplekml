"""
Demonstrates how to create a linestring focusing on the extrude and altitudemode properties.
"""
import os
import simplekml

# Create an instance of Kml
kml = simplekml.Kml(name="LineString", open=1)

# Create a linestring with two points (ie. a line)
linestring = kml.newlinestring(name="A Line")
linestring.coords = [(-122.364383,37.824664),(-122.364152,37.824322)]

# Create a linestring that will hover 50m above the ground
linestring = kml.newlinestring(name="A Hovering Line")
linestring.coords = [(-122.364167,37.824787,50), (-122.363917,37.824423,50)]
linestring.altitudemode = simplekml.AltitudeMode.relativetoground

# Create a linestring that will hover 100m above the ground that is extended to the ground
linestring = kml.newlinestring(name="An Extended Line")
linestring.coords = [(-122.363965,37.824844,100), (-122.363747,37.824501,100)]
linestring.altitudemode = simplekml.AltitudeMode.relativetoground
linestring.extrude = 1

# Create a linestring that will be extended to the ground but sloped from the ground up to 100m
linestring = kml.newlinestring(name="A Sloped Line")
linestring.coords = [(-122.363604,37.825009,0), (-122.363331,37.824604,100)]
linestring.altitudemode = simplekml.AltitudeMode.relativetoground
linestring.extrude = 1

# Save the KML
kml.save(os.path.splitext(__file__)[0] + ".kml")