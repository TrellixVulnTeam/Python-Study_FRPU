"""
This is a setup.py script generated by py2applet

pip install py2app==0.12

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['calculator.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

