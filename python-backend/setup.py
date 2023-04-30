import os
from setuptools import setup, find_packages

DISTNAME = 'whisperpod'
PACKAGES = find_packages()
EXTENSIONS = []
DESCRIPTION = 'Whisper to your pods'
AUTHOR = 'sters'
LICENSE = 'Revised BSD'
URL = ''
CLASSIFIERS = ['development status :: 3 - Alpha',
               'programming language :: Python :: 3',
               'topic :: Entertainment/Podcasting',
               'operating system :: OS Independent',
               ]
DEPENDENCIES = [
    "pandas",
    "ipdb",
    "whisper",
    "getpodcast",
    "openai-whisper",
    "pymongo",
    ]
VERSION="0.0.1"

# use README file as the long description
file_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(file_dir, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(name=DISTNAME,
      version=VERSION,
      packages=PACKAGES,
      ext_modules=EXTENSIONS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      maintainer_email="",
      license=LICENSE,
      url=URL,
      classifiers=CLASSIFIERS,
      zip_safe=False,
      install_requires=DEPENDENCIES,
      scripts=[],
      include_package_data=True
      )
