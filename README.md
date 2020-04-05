# ode-python

This is yet another Python binding of [Open Dynamics Engine (ODE)](https://www.ode.org/).

# Instalation

Python3 on Linux system is required.

	pip3 install ode-python

Please install ODE or cmake beforehand. pip3 first tries to build and install ODE using cmake if ODE cannot be found on the system.

For example, on debian:

	apt install cmake

or

	apt install libode-dev

# Uploading to PyPI

Please refer to [this page](https://packaging.python.org/tutorials/packaging-projects/).

	python3 -m pip install --user --upgrade setuptools wheel
	python3 -m pip install --user --upgrade twine
	
	python3 setup.py sdist bdist_wheel
	
	python3 -m twine upload --repository testpypi dist/*
	python3 -m twine upload --repository pypi dist/*
