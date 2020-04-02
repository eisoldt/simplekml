Styling
=======

A style tells Google Earth how to render a feature. For more information on styling please see `KML Reference <http://code.google.com/apis/kml/documentation/kmlreference.html>`_.

Concept
-------

Every feature can have a :class:`simplekml.Style` that tells Google Earth how to render it. A :class:`simplekml.Style` can have different 'substyles':  :class:`simplekml.IconStyle`, :class:`simplekml.IconStyle`, :class:`simplekml.LineStyle`, :class:`simplekml.PolyStyle`, :class:`simplekml.BalloonStyle` and :class:`simplekml.ListStyle`.

In simplekml a feature, by default, has no style, but as soon as you assign a value to one of the feature's :class:`simplekml.Style`'s properties the style is automatically created. In the generated KML the style becomes a child of the containing element (:class:`simplekml.Document`, :class:`simplekml.Folder`, etc). Here is an example::

    from simplekml import Kml

    kml = Kml()
    fol = kml.newfolder("A Folder")
    pnt = fol.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
    pnt.style.labelstyle.color = 'ff0000ff'  # Red
    kml.save("singlestyle.kml")

With the resulting generated KML:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
        <Document id="feat_1">
            <Folder id="feat_2">
                <Style id="stylesel_0">
                    <LabelStyle>
                        <color>ff0000ff</color>
                        <colorMode>normal</colorMode>
                        <scale>1</scale>
                    </LabelStyle>
                </Style>
                <name>A Folder</name>
                <Placemark id="feat_3">
                    <name>Kirstenbosch</name>
                    <styleUrl>#stylesel_0</styleUrl>
                    <Point id="geom_0">
                        <coordinates>18.432314,-33.988862,0.0</coordinates>
                    </Point>
                </Placemark>
            </Folder>
        </Document>
    </kml>

Above we created a :class:`simplekml.Point` inside of a :class:`simplekml.Folder` and then changed the color of the point's label by typing `pnt.style.labelstyle.color = 'ff0000ff'`. This resulted in a folder containing a :class:`simplekml.Placemark` with a point as a child element. The placemark also contains a reference to the :class:`simplekml.Style` `<styleUrl>#stylesel_0</styleUrl>`, which is a child of the folder with a labelstyle as a child.

The above is fine if we are dealing with one or to features, but if we are dealing with thousands of points the generated KML becomes very bloated, because every time you access a features style's properties a new style is created. Just imagine we modified the above to do the following::

    from simplekml import Kml

    kml = Kml()
    fol = kml.newfolder(name="A Folder")
    for lon in range(-180, 180, 10):
        for lat in range(-180, 180, 10):  # 10 Degree grid of points
            pnt = fol.newpoint(name="{0},{1}".format(lon, lat), coords=[(lon,lat)])
            pnt.style.labelstyle.color = 'ff0000ff'  # Red

    kml.save("manystyles.kml")

And the generated KML:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
        <Document id="feat_1">
            <Folder id="feat_2">
                <Style id="stylesel_0">
                    <LabelStyle>
                        <color>ff0000ff</color>
                        <colorMode>normal</colorMode>
                        <scale>1</scale>
                    </LabelStyle>
                </Style>
                <Style id="stylesel_1">
                    <LabelStyle>
                        <color>ff0000ff</color>
                        <colorMode>normal</colorMode>
                        <scale>1</scale>
                    </LabelStyle>
                </Style>
                <Style id="stylesel_2">
                    <LabelStyle>
                        <color>ff0000ff</color>
                        <colorMode>normal</colorMode>
                        <scale>1</scale>
                    </LabelStyle>
                </Style>

                ... many, many lines of kml go here

            </Folder>
        </Document>
    </kml>

The above was abbreviated a bit because the KML contains (2*180/10)^2 styles (one for each of the points we created, which is 1296 styles). As you can imagine, the resulting KML file will be quite huge! 

To make the KML much smaller we can create a 'shared' style and associate it with each feature::


    from simplekml import Kml, Style

    kml = Kml()

    fol = kml.newfolder(name="A Folder")

    sharedstyle = Style()
    sharedstyle.labelstyle.color = 'ff0000ff'  # Red

    for lon in range(-180, 180, 10):
        for lat in range(-180, 180, 10):  # 10 Degree grid of points
            pnt = fol.newpoint(name="{0},{1}".format(lon, lat), coords=[(lon,lat)])
        # pnt.style.labelstyle.color = 'ff0000ff'  # (Bad!) This results in (2*180/10)^2 styles
            pnt.style = sharedstyle  		   # (Much better!) This results in a single styles

    kml.save("sharedstyle.kml")

And the KML:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
        <Document id="feat_1">
            <Folder id="feat_2">
                <Style id="stylesel_0">
                    <LabelStyle>
                        <color>ff0000ff</color>
                        <colorMode>normal</colorMode>
                        <scale>1</scale>
                    </LabelStyle>
                </Style>
                <name>A Folder</name>
                <Placemark id="feat_3">
                    <name>-180,-180</name>
                    <styleUrl>#stylesel_0</styleUrl>
                    <Point id="geom_0">
                        <coordinates>-180,-180,0.0</coordinates>
                    </Point>
                </Placemark>
                <Placemark id="feat_4">
                    <name>-180,-170</name>
                    <styleUrl>#stylesel_0</styleUrl>
                    <Point id="geom_1">
                        <coordinates>-180,-170,0.0</coordinates>
                    </Point>
                </Placemark>

                ... many, many more points (1294 to be exact)

            </Folder>
        </Document>
    </kml>


Now this is much better! We only have one style at the beginning of the KML followed by all the points. What happened here is that a 'shared' style was created by creating an instance of the :class:`simplekml.Style` class `sharedstyle = Style()`, then the style's properties were changed and finally the `sharedstyle` was assigned to each point's style property.

In summary, there are two ways to style: changing the properties of an individual feature and creating a 'shared' style and assigning it to all the relevant features.

.. note::

    There is a 'shorthand' method when dealing with changing the properties of an individual feature. The following 'longhand' line of code::

      pnt.style.labelstyle.color = 'ff0000ff'  # Red

    is the same as this 'shorthand' version::

      pnt.labelstyle.color = 'ff0000ff'  # Red

    This helps to eliminate the need to type `.style` every time you need to change a style's property, as well as, reducing the size of your script. But, the `shorthand` makes the code less readable. It is suggested that you use the long hand method.

Styling a Point
---------------

A :class:`simplekml.Point` has two 'substyles' that can be altered to render it: :class:`simplekml.IconStyle` and :class:`simplekml.LabelStyle`. To change a point's style simply assign a value to one of its properties::

    pnt = kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
    pnt.style.labelstyle.color = 'ff0000ff'  # Red

That changed the text "Kirstenbosch" to red. See `the KML Reference <http://code.google.com/apis/kml/documentation/kmlreference.html#color the KML Reference>`_ for the format of the color string (you could also use the :class:`simplekml.Color` class). Now lets edit some more of the style::

    pnt.style.labelstyle.scale = 2  # Text twice as big
    pnt.style.iconstyle.color = 'ffff0000'  # Blue
    pnt.style.iconstyle.scale = 3  # Icon thrice as big
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/info-i.png'


Styling a LineString
--------------------

A :class:`simplekml.LineString` has one 'substyle' that can be altered to render it::

    lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                            coords=[(18.43312,-33.98924), (18.43224,-33.98914),
                                    (18.43144,-33.98911), (18.43095,-33.98904)])
    lin.style.linestyle.color = 'ff0000ff'  # Red
    lin.style.linestyle.width= 10  # 10 pixels


Styling a Polygon
-----------------

A :class:`simplekml.Polygon` has two 'substyles' that can be altered to render it:  :class:`simplekml.LineStyle` and :class:`simplekml.PolyStyle`. Below is code for a :class:`simplekml.Polygon` without a border that is slightly transparent::

    pol = kml.newpolygon(name="Atrium Garden",
                         outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004),
                                          (18.43410,-33.98972), (18.43371,-33.98952),
                                          (18.43348,-33.98985)],
                         innerboundaryis=[(18.43360,-33.98982), (18.43386,-33.98995),
                                          (18.43401,-33.98974), (18.43376,-33.98962),
                                          (18.43360,-33.98982)])
    pol.style.polystyle.color = '990000ff'  # Transparent red
    pol.style.polystyle.outline = 0
    
Styling MultiGeometry
---------------------

Applying a style to MultiGeometry applies the style to all the individual geometries in that MultiGeometry collection. Therefore, styling multigeometry is the same as styling normal geometry::

    from simplekml import Kml
    kml = Kml()
    multipnt = kml.newmultigeometry(name="Points")
    for lon in range(4):
        for lat in range(4):
            multipnt.newpoint(coords=[(lon,lat)])
    multipnt.style.labelstyle.color = 'ff0000ff'  # Red


