# Installation

## Requirements

Python >=3.7 is required. Support on Python 3.11 is limited (see [here](https://github.com/ModECI/modelspec/issues/25)).

## Installation using pip

Use pip to install the latest version of Modelspec (plus dependencies) from [PyPI](https://pypi.org/project/modelspec):
```
pip install modelspec
```

## Installation from source
To install the modelspec package from [source](https://github.com/ModECI/modelspec) and run it locally:

### 1) Create a virtual environment (e.g. called `modelspec-env`)
```
pip install virtualenv
virtualenv modelspec-env
```

### 2) Activate the virtual environment
```
source modelspec-env/bin/activate
```

### 3) Clone this repository
```
git clone https://github.com/ModECI/modelspec.git
```

### 4) Change to the directory
```
cd modelspec
```

### 5) Install the package
```
pip install .
```

Alternatively, to install modelspec plus optional dependencies:

```
pip install .[all]
```

## Generating modelspec documentation offline

Here is a walkthrough on how to generate the modelspec documentation offline

### Requirements

The documentation is generated using [Sphinx](https://www.sphinx-doc.org). Make is also required. For **Windows** installation of Make, see [here](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows). For **Mac** installation of Make, see [here](https://formulae.brew.sh/formula/make)



#### 1) Create a virtual environment with python
```
# install virtual environment

pip install virtualenv

# create & activate a virtual environment for your current or preferred python version

python -m virtualenv modelspec-env
modelspec-env\Scripts\activate
```

#### 2) Clone modelspec repository from GitHub into your local machine
```
git clone https://github.com/ModECI/modelspec.git
```

#### 3) Change into the modelspec directory
```
cd modelspec
```

#### 4) Install all modelspec package into the virtual environment
```
pip install .[all]
```

#### 5) Change directory into sphinx folder
```
# for windows
cd docs\sphinx

# for Mac/Linux
cd docs/sphinx
```

#### 6) Create offline documentation in sphinx folder
```
# To allow a fresh start when making the documentation
make clean

# To make the documentation
make html
```

#### 7) Change directory into html folder and run the documentation offline
```
# for Windows go into build\html folder and double click on the index.html file, or:

cd build\html
index.html

# for Mac, go into build/html folder and double click on the index.html file or:
cd build/html
open index.html
```

The documentation will open up in your browser automatically or right click on the file and open in any browser of your choice.
