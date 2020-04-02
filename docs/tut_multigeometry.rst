MultiGeometry Tutorial
----------------------

About
^^^^^

How to use the MultiGeometry features. We will create one KML with three MultiGeometry features. We will group :class:`simplekml.Polygon`, :class:`simplekml.LineString` and :class:`simplekml.Point` into the three MultiGeometry features. An additional folder will be created with normal points inside (not grouped with a MultiGeometry feature).

Background
^^^^^^^^^^
This tutorial is creating a reference for the South African coordinate system (Hartebeesthoek 94). The system divides South Africa into vertical bands of 3 degrees each with the odd longitude as the center of each band. Each of the bands is named Lo. 19, etc. based on the longitude that is represented. What this tutorial is going to do is create a polygon representing each of these bands. Between the bands will be a vertical line showing the separation. Each of the bands will have a label with its name. In addition, points will be created with the intersection of every odd number of latitude (just to show a MultiGeometry with points).

Creating the Code
^^^^^^^^^^^^^^^^^

First import simplekml and create a KML object::

    from simplekml import Kml, Color
    kml = Kml(open=1)

Next create a variable for each of the MultiGeometry elemnts and folder::

    multipnt = kml.newmultigeometry(name="MultiPoint") # SA (Hartebeeshoek94) Grid Intersections
    multilin = kml.newmultigeometry(name="MultiLine") # SA (Hartebeeshoek94) Lo. Lines
    multipolodd = kml.newmultigeometry(name="MultiPolyOdd") # SA (Hartebeeshoek94) Lo. Regions
    multipoleven = kml.newmultigeometry(name="MultiPolyEven") # SA (Hartebeeshoek94) Second Lo. Regions for styling
    lolabels = kml.newfolder(name="Lo. Regions") # The labels of the Lo. Regions (17-33)

A lot is happening in the next section. There are 2 for loops that are generating all the latitude and longitude values for the shapes. These coordinates are then used to create the various features. The code will be further highlighted below, where necessary::

    for x in range(16, 36, 2):
        linecoords = []
        if x < 34: # Label region
            lo = lolabels.newpoint(name=str(x+1), coords=[(x+1, -29)])
            lo.style.iconstyle.icon.href = "" # Remove the icons
        for y in range(-35, -19, 2):
            multipnt.newpoint(coords=[(x, y)])
            linecoords.append((x,y))
        multilin.newlinestring(coords=linecoords)
        polycoordsodd.append(linecoords)
        if len(polycoordsodd) == 2:
            end = polycoordsodd[1][:]
            end.reverse()
            multipolodd.newpolygon(outerboundaryis=polycoordsodd[0]+end)
            polycoordsodd = []
        if firstrun:
            firstrun = False
        else:
            polycoordseven.append(linecoords)
            if len(polycoordseven) == 2:
                end = polycoordseven[1][:]
                end.reverse()
                multipoleven.newpolygon(outerboundaryis=polycoordseven[0]+end)
                polycoordseven = []

This following section creates the points that are being used as labels for the regions. The points are added to the folder we created above (lolabels). You might be wondering why a MultiGeometry feature is not created to contain all the labels, this is because in KML all points in a MultiGeometry inherit the !MultiGeometries name for the name of the label. So, all the labels would end up being called "Lo. Regions", which is not what is wanted. The icon style's href of the points is also being made to equal "". This removes the icon completely and allows the name of the label to be centered on the origin of the point::

    if x < 34: # Label region
        lo = lolabels.newpoint(name=str(x+1), coords=[(x+1, -29)])
        lo.style.iconstyle.icon.href = "" # Remove the icons


Here the longitude coordinates are generated. Now each of the intersections of the longitudes and latitudes can be drawn as a point in a MultiGeometry (multipnt). This is done by calling `newpoint` on the multipnt variable, and supplying the coordinates. After the loop finishes a new LineString is created from all the coordinates generated. this is done by calling `newlinestring` on the multilin variable::

    for y in range(-35, -19, 2):
        multipnt.newpoint(coords=[(x, y)])
        linecoords.append((x,y))
    multilin.newlinestring(coords=linecoords)

What the next step does is basically creates a polygon in multipolodd and multipoleven alternatively. Once all the coordinates are generated for either of the MultiGeometry collections `newpolygon` is called on the relative collection::

    if len(polycoordsodd) == 2:
        end = polycoordsodd[1][:]
        end.reverse()
        multipolodd.newpolygon(outerboundaryis=polycoordsodd[0]+end)
        polycoordsodd = []
    if firstrun:
        firstrun = False
    else:
        polycoordseven.append(linecoords)
        if len(polycoordseven) == 2:
            end = polycoordseven[1][:]
            end.reverse()


Finally all the MultiGeometry features get styled. There a few things to note here.

  * The labels' scale of the point collection is set to `0.0`. This is done to make all the labels disappear.
  * The icon of the points is changed from the default pin to a circle by setting the icon styles href to the path of the circle image.
  * Color is applied to the LineString (thick black).
  * Color is applied to the MultiGeometry Polgon feature. Here we see the :class:`simplekml.Color` class being utilized. The :class:`simplekml.Color` class contains a list of named colors (from CSS and HTML). Here the orange and lightblue colors are used. The problem that occurs is that these colors are completely opaque, and makes the reference grid we are creating completely pointless, because we cannot see South Africa below the polygons. To remedy this, :func:`simplekml.Color.changealpha` of the :class:`simplekml.Color` class is used. What this does is accept a Google Earth HEX string and an alpha value and returns the HEX string with the alpha value modified. It is a quick and convenient way of assigning any alpha value to the standard colors

::

    multipnt.style.labelstyle.scale = 0.0 # Hide the labels of the points
    multipnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
    multilin.style.linestyle.color = Color.black
    multilin.style.linestyle.width = 5
    multipoleven.style.polystyle.color = Color.changealpha("77", Color.orange)
    multipoleven.style.linestyle.color = Color.changealpha("77", Color.orange)
    multipolodd.style.polystyle.color = Color.changealpha("77", Color.lightblue)
    multipolodd.style.linestyle.color = Color.changealpha("77", Color.lightblue)


Complete Code Example
^^^^^^^^^^^^^^^^^^^^^

Here is the complete code::

    from simplekml import Kml, Color
    kml = Kml(open=1)

    kml = simplekml.Kml(open=1)

    # Creating MultiGeometry
    multipnt = kml.newmultigeometry(name="MultiPoint") # SA (Hartebeeshoek94) Grid Intersections
    multilin = kml.newmultigeometry(name="MultiLine") # SA (Hartebeeshoek94) Lo. Lines
    multipolodd = kml.newmultigeometry(name="MultiPolyOdd") # SA (Hartebeeshoek94) Lo. Regions
    multipoleven = kml.newmultigeometry(name="MultiPolyEven") # SA (Hartebeeshoek94) Second Lo. Regions for styling
    lolabels = kml.newfolder(name="Lo. Regions") # The labels of the Lo. Regions (17-33)

    # Create all the coordinates to populate the South African Coordinate System
    polycoordsodd = []
    polycoordseven = []
    firstrun = True
    for x in range(16, 36, 2):
        linecoords = []
        if x < 34: # Label region
            lo = lolabels.newpoint(name=str(x+1), coords=[(x+1, -29)])
            lo.style.iconstyle.icon.href = "" # Remove the icons
        for y in range(-35, -19, 2):
            multipnt.newpoint(coords=[(x, y)])
            linecoords.append((x,y))
        multilin.newlinestring(coords=linecoords)
        polycoordsodd.append(linecoords)
        if len(polycoordsodd) == 2:
            end = polycoordsodd[1][:]
            end.reverse()
            multipolodd.newpolygon(outerboundaryis=polycoordsodd[0]+end)
            polycoordsodd = []
        if firstrun:
            firstrun = False
        else:
            polycoordseven.append(linecoords)
            if len(polycoordseven) == 2:
                end = polycoordseven[1][:]
                end.reverse()
                multipoleven.newpolygon(outerboundaryis=polycoordseven[0]+end)
                polycoordseven = []

    # Style everything
    multipnt.style.labelstyle.scale = 0.0 # Hide the labels of the points
    multipnt.style.iconstyle.icon.href = "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
    multilin.style.linestyle.color = Color.black
    multilin.style.linestyle.width = 5
    multipoleven.style.polystyle.color = Color.changealpha("77", Color.orange)
    multipoleven.style.linestyle.color = Color.changealpha("77", Color.orange)
    multipolodd.style.polystyle.color = Color.changealpha("77", Color.lightblue)
    multipolodd.style.linestyle.color = Color.changealpha("77", Color.lightblue)

    kml.save("Tut_MultiGeometry.kml")
