Release History
===============

simplekml 1.3.4 - 02 April 2020
-------------------------------
**Fixes**
  * Changed pixel to pixels in class Units
  * Removed a space in class RefreshMode

simplekml 1.3.3 - 28 January 2020
---------------------------------
**Fixes**
  * Changed cgi module to html for Python 3

simplekml 1.3.2 - 28 January 2020
---------------------------------
**Fixes**
  * Changed cgi module to html for Python 3

simplekml 1.3.1 - 08 August 2018
--------------------------------
**Changes**
  * Removed email from source files
  * Changed PyPi classifications for Python 3 to all versions of 3
  * Updated readme by removing expired websites

simplekml 1.3.0 - 18 March 2016
-------------------------------
**Fixes**
  * Made KmlElement class thread safe.
  * Fixed formatting of gx:angles.

**Changes**
  * Changed the license from GPL to LGPL


simplekml 1.2.8 - 07 June 2015
------------------------------
**Fixes**
  * Fixed "global" styles repeating in each container.
  * Fixed ampersand (&) not escaping correctly in urls.
  * Fixed problem where files added via :func:`simplekml.Kml.addfile` were forgotten.
  
**Changes**
  * Moved the method :func:`simplekml.Kml.addfile` from being available from all classes to being available only via :class:`simplekml.Kml`

simplekml 1.2.7 - 08 February 2015
----------------------------------
**Fixes**
  * Fixed adding unnecessary tag (gxlabelvisibility) when it is not being used.
  
simplekml 1.2.6 - 08 February 2015
----------------------------------
**Fixes**
  * Fixed missing gxlabelvisibility property from :class:`simplekml.LineStyle`.

simplekml 1.2.5 - 07 December 2014
----------------------------------
**Fixes**
  * Fixed syntax error for Python 3

simplekml 1.2.4 - 28 November 2014
----------------------------------
**Fixes**
  * Fixed missing gxvieweroptions property from :class:`simplekml.Camera` and :class:`simplekml.LookAt`.

simplekml 1.2.3 - 26 October 2013
---------------------------------
**Fixes**
  * Fixed unicode errors where some KML elements were causing an error when using unicode.

simplekml 1.2.2 - 07 June 2013
------------------------------
**Fixes**
  * Changed added model to :class:`simplekml.GxTrack`
  * Added __version__ property

simplekml 1.2.1 - 16 December 2012
-----------------------------------
**Fixes**
  * Changed newangle in :class:`simplekml.GxTrack` to :func:`simplekml.GxTrack.newgxangle`

simplekml 1.2.0 - 03 December 2012
----------------------------------
**New Features**
  * Added a method :func:`simplekml.Kml.addfile`. This method adds additional files to a KMZ. Useful for adding
    images to the KMZ that you want to display in a description balloon.

**Fixes**
  * Fixed documentation of coordinates where it incorrectly showed a coordinate being first latitude, then longitude,
    when it should have been the other way around
  * Fixed paths included in a KMZ, changed backslashes to forward slashes

simplekml 1.1.2 - 17 September 2012
-----------------------------------
**Fixes**
  * Fixed the import error regarding networklinkcontrol

simplekml 1.1.1 - 16 September 2012
-----------------------------------
**New Features**
  * Added the property *gxballoonvisibility* to all features
  * Added :attr:`simplekml.Kml.networklinkcontrol` to the :class:`simplekml.Kml`. Thus, there is a new class called
    :class:`simplekml.NetworkLinkControl` and relevant properties (including :class:`simplekml.LinkSnippet`)

simplekml 1.1.0 - 09 August 2012
--------------------------------
**New Features**
  * Added methods to all container classes for querying features already created. The new methods are: features,
    allfeatures, geometries, allgeometries, containers, allcontainers, styles, allstyles, stylemaps, and allstylemaps
  * Added a hint attribute to the Kml class that allows hints to be added to the kml tag, such as: *target=moon*

**Enhancements**
  * The CDATA tags within text attributes are not escaped with the rest of the text and remain as is whether or not
    parsetext of the Kml class is set to True or False

**Fixes**
  * FlyTo is now generating the Abstract View (Camera and LookAt) tag correctly

simplekml 1.0.0 - 24 July 2012
------------------------------
First production version release.