"""
Demonstrates touring with the reproduction of the tour sample in the KML Reference https://developers.google.com/kml/documentation/kmlreference#gxtour with the addition of GxSoundCue
"""

import os
import simplekml

# Create an instance of kml
kml = simplekml.Kml(name="Tours", open=1)

# Create a new point and style it
pnt = kml.newpoint(name="New Zealand's Southern Alps", coords=[(170.144,-43.605)])
pnt.style.iconstyle.scale = 1.0

# Create a tour and attach a playlist to it
tour = kml.newgxtour(name="Play me!")
playlist = tour.newgxplaylist()

# Attach a gx:SoundCue to the playlist and delay playing by 2 second (sound clip is about 4 seconds long)
soundcue = playlist.newgxsoundcue()
soundcue.href = "http://simplekml.googlecode.com/hg/samples/resources/drum_roll_1.wav"
soundcue.gxdelayedstart = 2

# Attach a gx:AnimatedUpdate to the playlist
animatedupdate = playlist.newgxanimatedupdate(gxduration=6.5)
animatedupdate.update.change = '<IconStyle targetId="{0}"><scale>10.0</scale></IconStyle>'.format(pnt.style.iconstyle.id)

# Attach a gx:FlyTo to the playlist
flyto = playlist.newgxflyto(gxduration=4.1)
flyto.camera.longitude = 170.157
flyto.camera.latitude = -43.671
flyto.camera.altitude = 9700
flyto.camera.heading = -6.333
flyto.camera.tilt = 33.5
flyto.camera.roll = 0

# Attach a gx:Wait to the playlist to give the gx:AnimatedUpdate time to finish
wait = playlist.newgxwait(gxduration=2.4)

# Save to file
kml.save(os.path.splitext(__file__)[0] + ".kml")