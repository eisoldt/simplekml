Tour Tutorial
-------------

About
^^^^^

How to create a tour. We will create a KML that will reproduce the tour sample in the `KML Reference <https://developers.google.com/kml/documentation/kmlreference#gxtour>`_ with the edition of :class:`simplekml.GxSoundCue`.

Creating the Code
^^^^^^^^^^^^^^^^^

First import simplekml and create a KML object::

    import simplekml
    kml = simplekml.Kml(open=1) # the document will be open in the table of contents

Next create a point feature and style it (note, we change the scale of the icon, this is going to be changed later during the tour::

    pnt = kml.newpoint(name="New Zealand's Southern Alps", coords=[(170.144,-43.605)])
    pnt.style.iconstyle.scale = 1.0

Now for the important part, creating the tour::

    tour = kml.newgxtour(name="Play me!")

Once we have a tour we can create a playlist which will be contained inside of the tour::

    playlist = tour.newgxplaylist()

A playlist is a collection of tour primitives (which are basically different events that happen during the tour), whose order is very important. The order that the tour primitives are added to the playlist is the order in which they play. There are five different tour primitives - :class:`simplekml.GxAnimatedUpdate`, :class:`simplekml.GxFlyTo`, :class:`simplekml.GxSoundCue`, :class:`simplekml.GxTourControl` and :class:`simplekml.GxWait`. In the following code snippet we will create all of the tour primitives and add them to the playlist::

    soundcue = playlist.newgxsoundcue()
    soundcue.href = "http://code.google.com/p/simplekml/source/browse/samples/drum_roll_1.wav"
    soundcue.gxdelayedstart = 2

    animatedupdate = playlist.newgxanimatedupdate(gxduration=6.5)
    animatedupdate.update.change = '<IconStyle targetId="{0}"><scale>10.0</scale></IconStyle>'.format(pnt.style.iconstyle.id)

    flyto = playlist.newgxflyto(gxduration=4.1)
    flyto.camera.longitude = 170.157
    flyto.camera.latitude = -43.671
    flyto.camera.altitude = 9700
    flyto.camera.heading = -6.333
    flyto.camera.tilt = 33.5
    flyto.camera.roll = 0

    wait = playlist.newgxwait(gxduration=2.4)

The order in which we added the tour primitives to the playlist is important. If the :class:`simplekml.GxSoundCue` was added after the :class:`simplekml.GxFlyTo`, then Google Earth would wait for the :class:`simplekml.GxFlyTo` to finish before playling the :class:`simplekml.GxSoundCue`, but if the :class:`simplekml.GxSoundCue` is added first it will play at the same time as the :class:`simplekml.GxFlyTo`. It is best to have a look at the `touring section of the KML Reference <https://developers.google.com/kml/documentation/kmlreference#gxtour>`_ to familiarise yourself with what exactly is going on with tours. In this example the :class:`simplekml.GxSoundCue` is delayed from playing by 2 second so the sound with stop playling at about the same time as the whole tour (the sound clip is about 4 seconds long).

.. note::

    According the the `KML Reference <https://developers.google.com/kml/documentation/kmlreference#gxtour>`_ a tour needs either a :class:`simplekml.GxFlyTo` or :class:`simplekml.GxWait` to hold a tour open. If you just have an :class:`simplekml.GxAnimatedUpdate` the tour plays for zero seconds in Google Earth. So, if you only want a :class:`simplekml.GxAnimated` make sure you add a :class:`simplekml.GxWait` tour primitive to the end of the tour with the same duration as the class:`simplekml.GxAnimated`.

And finally we save the kml::

    kml.save("tut_tours.kml")

Complete Code Example
^^^^^^^^^^^^^^^^^^^^^

Here is the complete code::

    import simplekml

    kml = simplekml.Kml(name='9_tours', open=1)

    pnt = kml.newpoint(name="New Zealand's Southern Alps", coords=[(170.144,-43.605)])
    pnt.style.iconstyle.scale = 1.0

    tour = kml.newgxtour(name="Play me!")
    playlist = tour.newgxplaylist()

    soundcue = playlist.newgxsoundcue()
    soundcue.href = "http://code.google.com/p/simplekml/source/browse/samples/drum_roll_1.wav"
    soundcue.gxdelayedstart = 2

    animatedupdate = playlist.newgxanimatedupdate(gxduration=6.5)
    animatedupdate.update.change = '<IconStyle targetId="{0}"><scale>10.0</scale></IconStyle>'.format(pnt.style.iconstyle.id)

    flyto = playlist.newgxflyto(gxduration=4.1)
    flyto.camera.longitude = 170.157
    flyto.camera.latitude = -43.671
    flyto.camera.altitude = 9700
    flyto.camera.heading = -6.333
    flyto.camera.tilt = 33.5
    flyto.camera.roll = 0

    wait = playlist.newgxwait(gxduration=2.4)

    kml.save("tut_tours.kml")

