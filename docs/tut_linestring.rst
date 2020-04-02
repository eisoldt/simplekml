Linestring Tutorial
-------------------

About
^^^^^

How to create a linestring. We will create different linestrings showing off the altitudemode and extrude properties.

Creating the Code
^^^^^^^^^^^^^^^^^

First import simplekml and create a KML object::

    import simplekml

Create the KML object::

    kml = simplekml.Kml(open=1) # the folder will be open in the table of contents

Next we create a simple linestring feature that lies on the ground::

    linestring = kml.newlinestring(name="A Line")
    linestring.coords = [(-122.364383,37.824664),(-122.364152,37.824322)]

Now to build on the previous linestring. Here we make a linestring that hovers 50m above the ground. To achieve this we give each "vertex" of the linestring (in this case the two coordinates representing the start and end of the linestring) a height value of 50m (the 50 in the two tuples). We also have to tell Google Earth that the height we gave each vertex is relative to the ground, we do this by assigning the value "relativetoground" to the atlitude property::

    linestring = kml.newlinestring(name="A Hovering Line")
    linestring.coords = [(-122.364167,37.824787,50), (-122.363917,37.824423,50)]
    linestring.altitudemode = simplekml.AltitudeMode.relativetoground

Let's make it more interesting and join the linestring to the ground. To this all we have to do is set the property extrude to 1 to tell Google Earth the extend the linestring all the way to the ground::

    linestring = kml.newlinestring(name="An Extended Line")
    linestring.coords = [(-122.363965,37.824844,100), (-122.363747,37.824501,100)]
    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
    linestring.extrude = 1

Let's go completely wild and make an extruded line climb out of the ground up to a height of 100m. To do this we simply change the first coordinates height value to zero::

    linestring = kml.newlinestring(name="A Sloped Line")
    linestring.coords = [(-122.363604,37.825009,0), (-122.363331,37.824604,100)]
    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
    linestring.extrude = 1

And finally we save the kml::

    kml.save("T00 LineString.kml")

Complete Code Example
^^^^^^^^^^^^^^^^^^^^^

Here is the complete code::

    import os
    import simplekml

    # Create an instance of Kml
    kml = simplekml.Kml(open=1)

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

