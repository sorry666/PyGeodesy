
# -*- coding: utf-8 -*-

# The setuptools script to build, install and test a PyGeodesy distribution.

# Tested with 64-bit Python 2.7.13, 2.7.14, 3.6.1 and 3.6.2 (using setuptools
# 28.8.0) but only on macOS 10.12.3, 10.12.4 and 10.12.5, 10.12.6 Sierra.

# python setup.py sdist --formats=gztar,bztar,zip  # ztar,tar
# python setup.py bdist_wheel --universal  # XXX
# python setup.py test
# python setup.py install

# <http://packaging.Python.org/key_projects/#setuptools>
# <http://packaging.Python.org/distributing>
# <http://docs.Python.org/2/distutils/sourcedist.html>
# <http://docs.Python.org/3.6/distutils/sourcedist.html>
# <http://setuptools.ReadTheDocs.io/en/latest/setuptools.html#developer-s-guide>
# <http://setuptools.ReadTheDocs.io/en/latest/setuptools.html#test-build-package-and-run-a-unittest-suite>
# <http://ZetCode.com/articles/packageinpython>

from setuptools import setup

__all__ = ()
__version__ = '18.10.16'


def _c2(*names):
    return ' :: '.join(names)


def _long_description():
    with open('README.rst', 'rb') as f:
        t = f.read()
        if isinstance(t, bytes):
            t = t.decode('utf-8')
        return t


def _version():
    with open('pygeodesy/__init__.py') as f:
        for t in f.readlines():
            if t.startswith('__version__'):
                v = t.split('=')[-1].strip().strip('\'"')
                return '.'.join(map(str, map(int, v.split('.'))))


_KeyWords=('antipode', 'area', 'azimuth', 'bearing',
           'cartesian', 'conic', 'curvature',
           'datum', 'development', 'distance',
           'earth', 'elevation', 'ellipsoid', 'equirectangular',
           'geocentric', 'geodesy', 'geodetic', 'GeodTest',
           'geographiclib', 'geohash', 'geoid', 'geoidHeight',
           'haversine', 'horizon', 'Karney', 'Krueger', 'Krüger',
           'Lambert', 'latitude', 'linearize', 'longitude',
           'MGRS', 'nearest', 'numpy', 'n-vector', 'Nvector', 'OSGR',
           'perimeter', 'polar', 'Pseudo-Mercator', 'PyGeodesy', 'PyPy',
           'radii', 'radius', 'Ramer-Douglas-Peucker', 'Reumann-Witkam', 'rhumb',
           'simplify', 'sphere', 'TMcoords', 'trigonometry', 'unroll', 'UTM',
           'Vincenty', 'Visvalingam-Whyatt', 'Web-Mercator', 'WGS')

setup(
    name='PyGeodesy',
    packages=['pygeodesy'],
    description='Pure Python geodesy tools',
    version=_version(),

    author='Jean M. Brouwers',
    author_email='mrJean1@Gmail.com',  # 'mrJean1 at Gmail dot com'
    maintainer='Jean M. Brouwers',
    maintainer_email='mrJean1@Gmail.com',  # 'mrJean1 at Gmail dot com'

    license='MIT',
    keywords=' '.join(_KeyWords),
    url='http://GitHub.com/mrJean1/PyGeodesy',

    long_description=_long_description(),

    package_data={'pygeodesy': ['LICENSE']},

#   data_files=[('docs',        ['docs/*.*']),
#               ('images',      ['test/testRoute.jpg']),
#               ('test',        ['test/test*.py']),
#               ('testresults', ['testresults/*.txt'])],
#   data_files fails somehow, see file MANIFEST.in

    test_suite='test.TestSuite',

    zip_safe=False,

    # <http://PyPI.org/project?%3Aaction=list_classifiers>
    classifiers=[
        _c2('Development Status', '5 - Production/Stable'),
        _c2('Environment', 'Console'),
        _c2('Intended Audience', 'Developers'),
        _c2('License', 'OSI Approved', 'MIT License'),
        _c2('Operating System', 'OS Independent'),
        _c2('Programming Language', 'Python'),
        _c2('Programming Language', 'Python', '2.6'),
        _c2('Programming Language', 'Python', '2.7'),
        _c2('Programming Language', 'Python', '3.5'),
        _c2('Programming Language', 'Python', '3.6'),
        _c2('Programming Language', 'Python', '3.7'),
        _c2('Topic', 'Software Development'),
        _c2('Topic', 'Scientific/Engineering', 'GIS'),
    ],

#   download_url='http://GitHub.com/mrJean1/PyGeodesy',
#   entry_points={},
#   include_package_data=False,
#   install_requires=[],
#   namespace_packages=[],
#   py_modules=[],
)
