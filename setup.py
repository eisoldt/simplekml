"""
Copyright 2011-2018 Kyle Lancaster | 2019-2021 Patrick Eisoldt

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

import setuptools

setuptools.setup(
    name = 'simplekml',
    packages = ['simplekml'],
    version = '1.3.6',
    description = 'A Simple KML creator',
    author='2011-2018 Kyle Lancaster | 2019-2021 Patrick Eisoldt',
    author_email='patrick@eisoldt.com',
    url='http://readthedocs.org/projects/simplekml/',
    license='GNU Lesser General Public License v3+',
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.9',
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: GIS',
            'Topic :: Software Development :: Libraries :: Python Modules'
          ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
