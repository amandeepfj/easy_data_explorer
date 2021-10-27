from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Easy Data Explorer'
LONG_DESCRIPTION = 'Python library to do common data exploring tasks.'

# Setting up
setup(
    name="easy_data_explorer",
    version=VERSION,
    author="amandeepfj (Amandeep Jiddewar)",
    author_email="<amandeep.jiddewar@alumni.emory.edu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'data explore'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)