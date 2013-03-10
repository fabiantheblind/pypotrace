#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy


ext_modules = [
        Extension("potrace._potrace", ["potrace/_potrace.pyx"], 
                libraries=["potrace"], library_dirs=['/opt/local/lib'], include_dirs=['/opt/local/include', numpy.get_include()]),
        Extension("potrace.bezier", ["potrace/bezier.pyx"],
            libraries=["agg"], language="c++"),
        Extension("potrace.agg.curves", ["potrace/agg/curves.pyx"],
            libraries=["agg"], language="c++"),
                ]


setup(
    name = "pypotrace",
    author = "Luper Rouch",
    author_email = "luper.rouch@gmail.com",
    url = "http://github.com/flupke/pypotrace",
    description = "potrace Python bindings",
    long_description = open("README.rst").read(),
    version = "0.1",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],

    packages = ["potrace", "potrace.agg"],
    ext_modules = ext_modules,

    cmdclass = {"build_ext": build_ext},
)
