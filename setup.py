"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

with open(r'./requirements.txt') as f:
    required = f.read().splitlines()

print("Requirements: {}".format(required))
APP = ['widget.py']
DATA_FILES = []
APP_NAME = 'Memory Indicator'
OPTIONS = {
    'packages': required,
    'argv_emulation': 1,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Simple Memory Indicator",
        'CFBundleIdentifier': "com.gs.osx.memory.indicator",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2015, Avneesh Srivastava, All Rights Reserved",
        'LSUIElement': 1
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
