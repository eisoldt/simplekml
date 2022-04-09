"""
Create a KML file with networklink with a relative link to another KML file
both inside the same KMZ file.
"""

import os
from zipfile import ZipFile
import simplekml

with ZipFile(os.path.splitext(__file__)[0] + ".kmz", 'w') as zipObj:

    # first create root KML with NetworkLink
    kml = simplekml.Kml()
    netlink = kml.newnetworklink(name="Network Link")
    netlink.link.href = "linked.kml"
    # doc.kml should be first entry in KMZ file
    zipObj.writestr('doc.kml', str(kml))

    # next create the networklinked KML file
    # and add that to the KMZ file

    kml = simplekml.Kml()
    pol = kml.newpolygon()
    pol.name = 'Protea Hotel'
    pol.description = 'A hotel.'
    pol.outerboundaryis = [(18.41543354224076, -33.90815042775773, 0), (18.41588475318415, -33.90785215367858, 0),
                           (18.41559067227835, -33.90755041505265, 0), (18.41514037818727, -33.907849668799, 0),
                           (18.41543354224076, -33.90815042775773, 0)]
    pol.innerboundaryis = [(18.41544664378987, -33.90797757844747, 0), (18.415668772438, -33.90782646170953, 0),
                           (18.41557012808532, -33.90772429063932, 0), (18.4153486707404, -33.90787067928737, 0),
                           (18.41544664378987, -33.90797757844747, 0)]
    pol.style.linestyle.color = 'ff0000ff'
    pol.linestyle.width = 5
    pol.style.polystyle.color = 'ffff00ff'

    # add KML to KMZ file as "linked.kml"
    zipObj.writestr('linked.kml', str(kml))
