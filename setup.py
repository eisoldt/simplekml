"""
Copyright 2011-2016 Kyle Lancaster

Simplekml is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from distutils.core import setup

setup(
    name = 'simplekml',
    packages = ['simplekml'],
    version = '1.3.1',
    description = 'A Simple KML creator',
    author='Kyle Lancaster',
    author_email='kyle.lan@gmail.com',
    url='http://readthedocs.org/projects/simplekml/',
    license='GNU Lesser General Public License v3+',
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: GIS',
            'Topic :: Software Development :: Libraries :: Python Modules'
          ],
    long_description=open('README.txt').read()
)
