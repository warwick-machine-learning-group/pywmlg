# pywmlg
Python package template for machine learning research

## Getting started

You can use this template for your own project:
1. On GitHub, click the "New Repository" buttom.
2. Under "Repository template" select "warwick-machine-learning-group/pywmlg".
3. Create the repository, then clone it to your computer.
4. On your computer, create a new branch.
5. Use an IDE such as VSCode to find occurences of "pywmlg", and change them to be the name of your new repo/package.
6. Change the name of the directory pywmlg to be the name of your python package.
7. Create a pull request, then merge into the main branch once the tests have passed.

We recommend always using a virtual environment for every new project. For example, here is how to create and activate a new conda environment:

```bash
conda create -n pywmlg python=3.9
conda activate pywmlg
```

## Installation

Install the package with pip

```bash
pip install pywmlg
```

## Tests

Run the unit tests with pytest:

```bash
pytest
```

## Docker

[Docker is great for reprodicible research](https://reproducible-analysis-workshop.readthedocs.io/en/latest/8.Intro-Docker.html).
To build the image:

```bash
docker build -t pywmlg:latest .
```

## Linting

Keeps the code neat and tidy.
We use [pylint](https://www.pylint.org/) and [mypy](http://mypy-lang.org/).
You can change pylint settings in the `.pylintrc` file.

```
pylint pywmlg/*
mypy pywmlg
```

Some of the smaller linting issues can be cured by running the [black formatter](https://github.com/psf/black):

```bash
black */
```

