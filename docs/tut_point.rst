Points Tutorial
---------------

About
^^^^^

How to create a simple point and change the points properties.

Creating the Code
^^^^^^^^^^^^^^^^^

First import simplekml and create a KML object::

    import simplekml

We then have some base data to work with. It is a list of tuples containing (in the following order) a city name, time corresponding to 12:00 noon Eastern Standard Time, latitude and logitude::

    cities = [
        ('Aberdeen, Scotland', '5:00 p.m.', 57.15, -2.15),
        ('Adelaide, Australia', '2:30 a.m.', -34.916667, 138.6),
        ('Algiers, Algeria', '6:00 p.m.', 36.833333, 3),
        # ...many, many more cities, and then...
        ('Zurich, Switzerland', '6:00 p.m.', 47.35, 8.516667)
    ]

Create the KML object::

    kml = simplekml.Kml(open=1) # the folder will be open in the table of contents

Next is a simple point example, we create a point feature at 0 degrees latitude and logitude and name it "The World". Here we pass all the information to the named parameters (note - the coordinates can contain an optional height value)::

    single_point = kml.newpoint(name="The World", coords=[(0.0,0.0)])

Next is a real world example, we create a point for each city. The points' properties are assigned after the point is created::

    for city, time, lat, lon in cities:
        pnt = kml.newpoint()
        pnt.name = city
        pnt.description = "Time corresponding to 12:00 noon, Eastern Standard Time: {0}".format(time)
        pnt.coords = [(lon, lat)]

And finally we save the kml::

    kml.save("T00 Points.kml")

Complete Code Example
^^^^^^^^^^^^^^^^^^^^^

Here is the complete code::

    import simplekml

    # Cities of the World with their coordinates and time corresponding to 12:00 noon, Eastern Standard Time
    # Source: http://www.infoplease.com/ipa/A0001769.html
    cities = [
        ('Aberdeen, Scotland', '5:00 p.m.', 57.15, -2.15),
        ('Adelaide, Australia', '2:30 a.m.', -34.916667, 138.6),
        ('Algiers, Algeria', '6:00 p.m.', 36.833333, 3),
        ('Amsterdam, Netherlands', '6:00 p.m.', 52.366667, 4.883333),
        ('Ankara, Turkey', '7:00 p.m.', 39.916667, 32.916667),
        ('Asuncion, Paraguay', '1:00 p.m.', -25.25, -57.666667),
        ('Athens, Greece', '7:00 p.m.', 37.966667, 23.716667),
        ('Auckland, New Zealand', '5:00 a.m.', -36.866667, 174.75),
        ('Bangkok, Thailand', 'midnight', 13.75, 100.5),
        ('Barcelona, Spain', '6:00 p.m.', 41.383333, 2.15),
        ('Beijing, China', '1:00 a.m.', 39.916667, 116.416667),
        ('Belem, Brazil', '2:00 p.m.', -1.466667, -48.483333),
        ('Belfast, Northern Ireland', '5:00 p.m.', 54.616667, -5.933333),
        ('Belgrade, Serbia', '6:00 p.m.', 44.866667, 20.533333),
        ('Berlin, Germany', '6:00 p.m.', 52.5, 13.416667),
        ('Birmingham, England', '5:00 p.m.', 52.416667, -1.916667),
        ('Bogota, Colombia', '12:00 noon', 4.533333, -74.25),
        ('Bombay, India', '10:30 p.m.', 19, 72.8),
        ('Bordeaux, France', '6:00 p.m.', 44.833333, -0.516667),
        ('Bremen, Germany', '6:00 p.m.', 53.083333, 8.816667),
        ('Brisbane, Australia', '3:00 a.m.', -27.483333, 153.133333),
        ('Bristol, England', '5:00 p.m.', 51.466667, -2.583333),
        ('Brussels, Belgium', '6:00 p.m.', 50.866667, 4.366667),
        ('Bucharest, Romania', '7:00 p.m.', 44.416667, 26.116667),
        ('Budapest, Hungary', '6:00 p.m.', 47.5, 19.083333),
        ('Buenos Aires, Argentina', '2:00 p.m.', -34.583333, -58.366667),
        ('Cairo, Egypt', '7:00 p.m.', 30.033333, 31.35),
        ('Calcutta, India', '10:30 p.m.', 22.566667, 88.4),
        ('Canton, China', '1:00 a.m.', 23.116667, 113.25),
        ('Cape Town, South Africa', '7:00 p.m.', -33.916667, 18.366667),
        ('Caracas, Venezuela', '1:00 p.m.', 10.466667, -67.033333),
        ('Cayenne, French Guiana', '2:00 p.m.', 4.816667, -52.3),
        ('Chihuahua, Mexico', '10:00 a.m.', 28.616667, -106.083333),
        ('Chongqing, China', '1:00 a.m.', 29.766667, 106.566667),
        ('Copenhagen, Denmark', '6:00 p.m.', 55.666667, 12.566667),
        ('Cordoba, Argentina', '2:00 p.m.', -31.466667, -64.166667),
        ('Dakar, Senegal', '5:00 p.m.', 14.666667, -17.466667),
        ('Darwin, Australia', '2:30 a.m.', -12.466667, 130.85),
        ('Djibouti, Djibouti', '8:00 p.m.', 11.5, 43.05),
        ('Dublin, Ireland', '5:00 p.m.', 53.333333, -6.25),
        ('Durban, South Africa', '7:00 p.m.', -29.883333, 30.883333),
        ('Edinburgh, Scotland', '5:00 p.m.', 55.916667, -3.166667),
        ('Frankfurt, Germany', '6:00 p.m.', 50.116667, 8.683333),
        ('Georgetown, Guyana', '1:00 p.m.', 6.75, -58.25),
        ('Glasgow, Scotland', '5:00 p.m.', 55.833333, -4.25),
        ('Guatemala City, Guatemala', '11:00 a.m.', 14.616667, -90.516667),
        ('Guayaquil, Ecuador', '12:00 noon', -2.166667, -79.933333),
        ('Hamburg, Germany', '6:00 p.m.', 53.55, 10.033333),
        ('Hammerfest, Norway', '6:00 p.m.', 70.633333, 23.633333),
        ('Havana, Cuba', '12:00 noon', 23.133333, -82.383333),
        ('Helsinki, Finland', '7:00 p.m.', 60.166667, 25),
        ('Hobart, Tasmania', '3:00 a.m.', -42.866667, 147.316667),
        ('Hong Kong, China', '1:00 a.m.', 22.333333, 114.183333),
        ('Iquique, Chile', '1:00 p.m.', -20.166667, -70.116667),
        ('Irkutsk, Russia', '1:00 a.m.', 52.5, 104.333333),
        ('Jakarta, Indonesia', 'midnight', -6.266667, 106.8),
        ('Johannesburg, South Africa', '7:00 p.m.', -26.2, 28.066667),
        ('Kingston, Jamaica', '12:00 noon', 17.983333, -76.816667),
        ('Kinshasa, Congo', '6:00 p.m.', -4.3, 15.283333),
        ('Kuala Lumpur, Malaysia', '1:00 a.m.', 3.133333, 101.7),
        ('La Paz, Bolivia', '1:00 p.m.', -16.45, -68.366667),
        ('Leeds, England', '5:00 p.m.', 53.75, -1.5),
        ('Lima, Peru', '12:00 noon', -12, -77.033333),
        ('Lisbon, Portugal', '5:00 p.m.', 38.733333, -9.15),
        ('Liverpool, England', '5:00 p.m.', 53.416667, -3),
        ('London, England', '5:00 p.m.', 51.533333, -0.083333),
        ('Lyons, France', '6:00 p.m.', 45.75, 4.833333),
        ('Madrid, Spain', '6:00 p.m.', 40.433333, -3.7),
        ('Manchester, England', '5:00 p.m.', 53.5, -2.25),
        ('Manila, Philippines', '1:00 a.m.', 14.583333, 120.95),
        ('Marseilles, France', '6:00 p.m.', 43.333333, 5.333333),
        ('Mazatlan, Mexico', '10:00 a.m.', 23.2, -106.416667),
        ('Mecca, Saudi Arabia', '8:00 p.m.', 21.483333, 39.75),
        ('Melbourne, Australia', '3:00 a.m.', -37.783333, 144.966667),
        ('Mexico City, Mexico', '11:00 a.m.', 19.433333, -99.116667),
        ('Milan, Italy', '6:00 p.m.', 45.45, 9.166667),
        ('Montevideo, Uruguay', '2:00 p.m.', -34.883333, -56.166667),
        ('Moscow, Russia', '8:00 p.m.', 55.75, 37.6),
        ('Munich, Germany', '6:00 p.m.', 48.133333, 11.583333),
        ('Nagasaki, Japan', '2:00 a.m.', 32.8, 129.95),
        ('Nagoya, Japan', '2:00 a.m.', 35.116667, 136.933333),
        ('Nairobi, Kenya', '8:00 p.m.', -1.416667, 36.916667),
        ('Nanjing (Nanking), China', '1:00 a.m.', 32.05, 118.883333),
        ('Naples, Italy', '6:00 p.m.', 40.833333, 14.25),
        ('New Delhi, India', '10:30 p.m.', 28.583333, 77.2),
        ('Newcastle-on-Tyne, England', '5:00 p.m.', 54.966667, -1.616667),
        ('Odessa, Ukraine', '7:00 p.m.', 46.45, 30.8),
        ('Osaka, Japan', '2:00 a.m.', 34.533333, 135.5),
        ('Oslo, Norway', '6:00 p.m.', 59.95, 10.7),
        ('Panama City, Panama', '12:00 noon', 8.966667, -79.533333),
        ('Paramaribo, Suriname', '2:00 p.m.', 5.75, -55.25),
        ('Paris, France', '6:00 p.m.', 48.8, 2.333333),
        ('Perth, Australia', '1:00 a.m.', -31.95, 115.866667),
        ('Plymouth, England', '5:00 p.m.', 50.416667, -4.083333),
        ('Port Moresby, Papua New Guinea', '3:00 a.m.', -9.416667, 147.133333),
        ('Prague, Czech Republic', '6:00 p.m.', 50.083333, 14.433333),
        ('Rangoon, Myanmar', '11:30 p.m.', 16.833333, 96),
        ('Reykjavik, Iceland', '5:00 p.m.', 64.066667, -21.966667),
        ('Rio de Janeiro, Brazil', '2:00 p.m.', -22.95, -43.2),
        ('Rome, Italy', '6:00 p.m.', 41.9, 12.45),
        ('Salvador, Brazil', '2:00 p.m.', -12.933333, -38.45),
        ('Santiago, Chile', '1:00 p.m.', -33.466667, -70.75),
        ('St. Petersburg, Russia', '8:00 p.m.', 59.933333, 30.3),
        ('Sao Paulo, Brazil', '2:00 p.m.', -23.516667, -46.516667),
        ('Shanghai, China', '1:00 a.m.', 31.166667, 121.466667),
        ('Singapore, Singapore', '1:00 a.m.', 1.233333, 103.916667),
        ('Sofia, Bulgaria', '7:00 p.m.', 42.666667, 23.333333),
        ('Stockholm, Sweden', '6:00 p.m.', 59.283333, 18.05),
        ('Sydney, Australia', '3:00 a.m.', -34, 151),
        ('Tananarive, Madagascar', '8:00 p.m.', -18.833333, 47.55),
        ('Teheran, Iran', '8:30 p.m.', 35.75, 51.75),
        ('Tokyo, Japan', '2:00 a.m.', 35.666667, 139.75),
        ('Tripoli, Libya', '7:00 p.m.', 32.95, 13.2),
        ('Venice, Italy', '6:00 p.m.', 45.433333, 12.333333),
        ('Veracruz, Mexico', '11:00 a.m.', 19.166667, -96.166667),
        ('Vienna, Austria', '6:00 p.m.', 48.233333, 16.333333),
        ('Vladivostok, Russia', '3:00 a.m.', 43.166667, 132),
        ('Warsaw, Poland', '6:00 p.m.', 52.233333, 21),
        ('Wellington, New Zealand', '5:00 a.m.', -41.283333, 174.783333),
        ('Zurich, Switzerland', '6:00 p.m.', 47.35, 8.516667)
    ]

    # Create an instance of Kml
    kml = simplekml.Kml(open=1)

    # Create a point named "The World" attached to the KML document with its coordinate at 0 degrees latitude and longitude.
    # All the point's properties are given when it is constructed.
    single_point = kml.newpoint(name="The World", coords=[(0.0,0.0)])

    # Create a point for each city. The points' properties are assigned after the point is created
    for city, time, lat, lon in cities:
        pnt = kml.newpoint()
        pnt.name = city
        pnt.description = "Time corresponding to 12:00 noon, Eastern Standard Time: {0}".format(time)
        pnt.coords = [(lon, lat)]

    # Save the KML
    kml.save("T00 Point.kml")

