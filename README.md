# ode-python

This is yet another Python binding of [Open Dynamics Engine (ODE)](https://www.ode.org/). Python3 on Linux system is required.

	pip3 install ode-python

Please install ODE somewhere on the system. For example, on debian:

	apt install libode8

# Uploading to PyPI

Please refer to [this page](https://packaging.python.org/tutorials/packaging-projects/).

	python3 -m pip install --user --upgrade setuptools wheel
	python3 -m pip install --user --upgrade twine
	
	python3 setup.py sdist bdist_wheel
	
	python3 -m twine upload --repository testpypi dist/*
	python3 -m twine upload --repository pypi dist/*
