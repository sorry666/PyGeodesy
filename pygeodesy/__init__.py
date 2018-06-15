
# -*- coding: utf-8 -*-

u'''A pure Python implementation of geodesy tools for various ellipsoidal
and spherical earth models using precision trigonometric, vector-based
and approximate methods for geodetic (lat-/longitude) and geocentric
cartesian (x/y/z) coordinates.

Transcribed from U{JavaScript originals<http://github.com/chrisveness/geodesy>}
by I{Chris Veness (C) 2005-2016} and published under the same U{MIT License
<http://opensource.org/licenses/MIT>}**.

There are two modules for ellipsoidal earth models, I{ellipsoidalVincenty}
and I{-Nvector} and two for spherical ones, I{sphericalTrigonometry} and
I{-Nvector}.  Each module provides a I{attributes-LatLon-html} class with
methods and functions to compute distance, initial and final bearing,
intermediate and nearest points, area, perimeter, conversions and unrolling,
among other things.  For more information and further details see the
U{documentation<http://mrjean1.github.io/PyGeodesy/>}, the descriptions
of U{Latitude/Longitude<http://www.movable-type.co.uk/scripts/latlong.html>},
U{Vincenty<http://www.movable-type.co.uk/scripts/latlong-vincenty.html>} and
U{Vector-based<http://www.movable-type.co.uk/scripts/latlong-vectors.html>}
geodesy and the original U{JavaScript source<http://github.com/chrisveness/geodesy>} or
U{docs<http://www.movable-type.co.uk/scripts/geodesy/docs/>}.

Also included are modules for conversions to and from
U{UTM<http://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html>}
(Universal Transverse Mercator) and U{Web Mercator
<http://wikipedia.org/wiki/Web_Mercator>} (Pseudo-Mercator) coordinates,
U{MGRS<http://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html>}
(NATO Military Grid Reference System) and
U{OSGR<http://www.movable-type.co.uk/scripts/latlong-os-gridref.html>}
(British Ordinance Survery Grid Reference) grid references and a module for
encoding and decoding U{Geohashes<http://www.movable-type.co.uk/scripts/geohash.html>}.

Two other modules provide Lambert conformal conic projections and positions
(from U{John P. Snyder, "Map Projections -- A Working Manual", 1987, pp 107-109
<http://pubs.er.USGS.gov/djvu/PP/PP_1395.pdf>}) and several functions to
U{simplify<http://bost.ocks.org/mike/simplify/>} or linearize a path of
I{LatLon} points (or a U{NumPy array
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html>}),
including implementations of the U{Ramer-Douglas-Peucker
<http://wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm>}, the
U{Visvalingam-Whyatt<http://hydra.hull.ac.uk/resources/hull:8338>} and the
U{Reumann-Witkam<http://psimpl.sourceforge.net/reumann-witkam.html>}
algorithms and modified versions of the former.

All Python source code has been statically U{checked
<http://github.com/ActiveState/code/tree/master/recipes/Python/546532_PyChecker_postprocessor>}
with U{PyChecker<http://pypi.python.org/pypi/pychecker>},
U{PyFlakes<http://pypi.python.org/pypi/pyflakes>},
U{PyCodeStyle<http://pypi.python.org/pypi/pycodestyle>} (formerly Pep8) and
U{McCabe<http://pypi.python.org/pypi/mccabe>} using Python 2.7.15 and with
U{Flake8<http://pypi.python.org/pypi/flake8>} on Python 3.6.5, both in
64-bit on macOS 10.13.5 High Sierra.

The tests have been run in 64-bit with U{PyPy-Python<http://pypy.org>}
2.7.13, Python 2.7.15 (with U{geographiclib
<http://pypi.python.org/pypi/geographiclib>} 1.49 and U{numpy
<http://pypi.python.org/pypi/numpy>} 1.14.0), U{Intel-Python
<http://software.intel.com/en-us/distribution-for-python>} 3.5.3 (and
U{numpy<http://pypi.python.org/pypi/numpy>} 1.11.3) and Python 3.6.5,
all on macOS 10.13.5 High Sierra and with U{Pythonista 3.2
<http://omz-software.com/pythonista/>} Python 2.7.12 and 3.6.1 (both
with U{numpy<http://pypi.python.org/pypi/numpy>} 1.8.0) on iOS 11.4.

Previously, the tests were run with 64-bit Python 2.6.9 (and numpy 1.6.2),
2.7.10 (and numpy 1.8.0rc1), 2.7.13, 2.7.14 (and numpy 1.13.1), 3.5.3,
3.6.2, 3.6.3 and 3.6.4 on MacOS X 10.10 Yosemite, MacOS X 10.11 El Capitan,
macOS 10.12 Sierra and/or macOS 10.13.4 High Sierra, with Pythonista 3.1
on iOS 10.3.3, 11.0.3, 11.1.2 and 11.3, with 32-bit Python 2.6.6 on
Windows XP SP3 and with 32-bit Python 2.7.14 on Window 10 Pro.

In addition to the U{PyGeodesy<http://pypi.python.org/pypi/PyGeodesy>} package,
the distribution files contain the tests, the test results and the complete
documentation (generated by U{Epydoc<http://pypi.python.org/pypi/epydoc>} using
command line:
C{epydoc --html --no-private --no-source --name=PyGeodesy --url=... -v pygeodesy}).

To install PyGeodesy, type C{pip install PyGeodesy} or C{easy_install PyGeodesy}
in a terminal or command window.  Alternatively, download C{PyGeodesy-} from
U{PyPI<http://pypi.python.org/pypi/PyGeodesy/>} or
U{GitHub<http://github.com/mrJean1/PyGeodesy>}, C{unzip} the downloaded file,
C{cd} to directory C{Pygeodesy-} and type C{python setup.py install}.  To
run all PyGeodesy tests, type C{python setup.py test} before installation.

Installation of U{NumPy<http://www.NumPy.org>} and U{GeographicLib
<http://GeographicLib.sourceforge.io>} is optional, but the latter is
required for two I{ellipsoidalVincenty} functions, I{areaOf} and I{perimeterOf}.

Some function and method names differ from the JavaScript version. In such
cases documentation tag B{JS name:} shows the original JavaScript name.

__

**) U{Copyright (C) 2016-2018 -- mrJean1 at Gmail dot com
<http://opensource.org/licenses/MIT>}

C{Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:}

C{The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.}

C{THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.}

@newfield example: Example, Examples
@newfield JSname: JS name, JS names

@var EPS:  System's M{epsilon} (float)
@var EPS1: M{1 - EPS} (float), about 0.9999999999999998
@var EPS2: M{sqrt(EPS)} (float)

@var F_D:   Format degrees as deg° (string).
@var F_DM:  Format degrees as deg°min′ (string).
@var F_DMS: Format degrees as deg°min′sec″ (string).
@var F_DEG: Format degrees as [D]DD without symbol (string).
@var F_MIN: Format degrees as [D]DDMM without symbols (string).
@var F_SEC: Format degrees as [D]DDMMSS without symbols (string).
@var F_RAD: Convert degrees to radians and format as RR (string).

@var PI:   Constant M{math.pi} (float)
@var PI2:  Two PI, M{math.pi * 2} (float)
@var PI_2: Half PI, M{math.pi / 2} (float)

@var R_M:  Mean, spherical earth radius (meter).
@var R_MA: Equatorial earth radius (meter) WGS84, EPSG:3785.
@var R_MB: Polar earth radius (meter) WGS84, EPSG:3785.
@var R_KM: Mean, spherical earth radius (kilo meter).
@var R_NM: Mean, spherical earth radius (nautical miles).
@var R_SM: Mean, spherical earth radius (statute miles).
@var R_FM: Former FAI Sphere earth radius (meter).
@var R_VM: Aviation/Navigation earth radius (meter).

@var S_DEG: Degrees symbol ° (string).
@var S_MIN: Minutes symbol ′ (string).
@var S_SEC: Seconds symbol ″ (string).
@var S_RAD: Radians symbol  (string).
@var S_SEP: Separator between deg°, min′ and sec″  (string).

@var Conics:     Registered conics (enum).
@var Datums:     Registered datums (enum).
@var Ellipsoids: Registered ellipsoids (enum).
@var Transforms: Registered transforms (enum).

@var version: Normalized PyGeodesy version (string).

'''

try:
    import bases as _ # PYCHOK expected
    del _  # hide private, internal modules
except ImportError:
    # extend sys.path to include this very directory
    # such that all public and private sub-modules can
    # be imported (and checked by PyChecker, etc.)
    import os, sys  # PYCHOK expected
    sys.path.insert(0, os.path.dirname(__file__))  # XXX __path__[0]
    del os, sys

# keep ellipsoidal, spherical and vector modules as sub-modules
import ellipsoidalNvector  # PYCHOK false
import ellipsoidalVincenty  # PYCHOK false
import geohash
import nvector  # PYCHOK false
import sphericalNvector  # PYCHOK false
import sphericalTrigonometry  # PYCHOK false
import vector3d  # PYCHOK false

Geohash       = geohash.Geohash
VincentyError = ellipsoidalVincenty.VincentyError

# all public sub-modules, contants, classes and functions
__all__ = ('ellipsoidalNvector', 'ellipsoidalVincenty',  # modules
           'sphericalNvector', 'sphericalTrigonometry',
           'datum', 'dms', 'fmath', 'geohash', 'lcc', 'mgrs',
           'nvector', 'osgr', 'points', 'simplify',
           'utils', 'utm', 'vector3d', 'webmercator',
           'Geohash', 'VincentyError',  # classes
           'R_M',  # to avoid duplicates from datum and utils
           'version')  # extended below
__version__ = '18.06.15'

# see setup.py for similar logic
version = '.'.join(map(str, map(int, __version__.split('.'))))

# lift all public classes, constants, functions, etc. but
# only from the following sub-modules ... (see also David
# Beazley's <http://dabeaz.com/modulepackage/index.html>)
from datum       import *  # PYCHOK __all__
from dms         import *  # PYCHOK __all__
from fmath       import *  # PYCHOK __all__
from lcc         import *  # PYCHOK __all__
from mgrs        import *  # PYCHOK __all__
from osgr        import *  # PYCHOK __all__
from points      import *  # PYCHOK __all__
from simplify    import *  # PYCHOK __all__
from utils       import *  # PYCHOK __all__
from utm         import *  # PYCHOK __all__
from webmercator import *  # PYCHOK __all__

import datum        # PYCHOK expected
import dms          # PYCHOK expected
import fmath        # PYCHOK expected
import lcc          # PYCHOK expected
import mgrs         # PYCHOK expected
import osgr         # PYCHOK expected
import points       # PYCHOK expected
import simplify     # PYCHOK expected
import utils        # PYCHOK expected
import utm          # PYCHOK expected
import webmercator  # PYCHOK expected

# concat __all__ with the public classes, constants,
# functions, etc. from the sub-modules mentioned above
for m in (datum, dms, fmath, lcc, mgrs, osgr, points,
          simplify, utils, utm, webmercator):
    __all__ += tuple(_ for _ in m.__all__ if _ not in ('R_M',))
del m

# for backward compatibility with old names
areaof      = points.areaOf
perimeterof = points.perimeterOf


def equirectangular3(lat1, lon1, lat2, lon2, **options):
    '''For backward compatibility only, obsolete, replaced by
       function L{utils.equirectangular_}.

       See function L{utils.equirectangular_} for more details,
       the available I{options} and errors raised.

       @return: 3-Tuple (distance2, delta_lat, delta_lon).
    '''
    return utils.equirectangular_(lat1, lon1, lat2, lon2, **options)[:3]


if __name__ == '__main__':

    __all__ += 'areaof***', 'equirectangular3***', 'perimeterof***'

    d, e, p = locals(), 0, ''
    for i, a in enumerate(sorted(__all__)):
        n = a.rstrip('*')
        r = repr(d[n]).replace(' ' + n + ' ', ' ') \
                      .replace(" '" + n + "' ", ' ')
        if n == p:
            e += 1
            s = '***'
        else:
            s = ''
            p = n
        print('%s %s%s %s' % (i + 1, a, s, r))

    print('--- PyGeodesy %s (%s duplicates)' % (__version__, e or 'no'))

# **) MIT License
#
# Copyright (C) 2016-2018 -- mrJean1 at Gmail dot com
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
