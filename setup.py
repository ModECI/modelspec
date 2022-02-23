from setuptools import setup

import modelspec

version = modelspec.__version__

setup(
    name="modelspec",
    version=version,
    author="Padraig Gleeson",
    author_email="p.gleeson@gmail.com",
    packages=["modelspec"],
    url="https://github.com/ModECI/modelspec",
    license="LICENSE.lesser",
    description="A common JSON/YAML based format for compact model specification",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["pyyaml", "numpy", "tabulate"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ],
)
