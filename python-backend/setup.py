import os
from setuptools import setup, find_packages

DISTNAME = 'whisperpod'
PACKAGES = find_packages()
EXTENSIONS = []
DESCRIPTION = 'Whisper to your pods'
AUTHOR = 'sters'
AUTHOR_EMAIL = 'you@example.com'
MAINTAINER = 'you'
MAINTAINER_EMAIL = 'you@example.com'
LICENSE = 'Revised BSD'
URL = ''
CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Programming Language :: Python :: 3',
               'Topic :: Multimedia :: Sound/Audio :: Players',
               'Operating System :: OS Independent',
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
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      url=URL,
      classifiers=CLASSIFIERS,
      zip_safe=False,
      install_requires=DEPENDENCIES,
      scripts=[],
      include_package_data=True
      )
