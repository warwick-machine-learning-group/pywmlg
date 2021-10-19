"""Setup script for pywmlg"""

from setuptools import find_packages, setup

setup(
    author="Warwick Machine Learning Group",
    description="",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "pydantic>=1.8.0",
    ],
    name="pywmlg",
    packages=find_packages(),
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)