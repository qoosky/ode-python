# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

from sys import version_info
from sys import exit

from os import environ
from os import getcwd
from os import chdir
from os import path
from os import pathsep

from ctypes.util import find_library
from subprocess import check_call
from tempfile import mkdtemp
from shutil import rmtree

def Main():

    if version_info.major < 3:
        exit('Python 2 is not supported.')

    localOdeInstallDir = path.join(environ.get('HOME'), '.pyode')
    if not CheckOde(localOdeInstallDir):
        InstallOde(localOdeInstallDir, odeSourceDir='ode-0.16.1')
    InstallPyOde()

def CheckOde(localOdeInstallDir):
    ldLibraryPath = environ.get('LD_LIBRARY_PATH')
    if ldLibraryPath is None:
        ldLibraryPath = []
    else:
        ldLibraryPath = ldLibraryPath.split(pathsep)
    ldLibraryPath.append(path.join(localOdeInstallDir, 'lib'))
    environ['LD_LIBRARY_PATH'] = pathsep.join(ldLibraryPath)
    return find_library('ode') is not None

def InstallOde(localOdeInstallDir, odeSourceDir):
    tmpDir = None
    originalWorkDir = getcwd()
    packageDir = path.dirname(path.abspath(__file__))
    try:
        tmpDir = mkdtemp()
        chdir(tmpDir)
        cmakeArgs = [
            '-DBUILD_SHARED_LIBS=ON',
            '-DODE_WITH_DEMOS=OFF',
            '-DODE_WITH_TESTS=OFF',
            '-DCMAKE_INSTALL_PREFIX={}'.format(localOdeInstallDir)
        ]
        check_call(['cmake', path.join(packageDir, odeSourceDir)] + cmakeArgs)
        check_call(['make'])
        check_call(['make', 'install'])
    finally:
        chdir(originalWorkDir)
        if tmpDir is not None:
            rmtree(tmpDir)

def InstallPyOde():
    setup(
        name='ode-python',
        version='0.0.2',
        url='https://github.com/qoosky/ode-python',
        license='MIT',
        description='Open Dynamics Engine (ODE) python binding.',
        long_description=open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        author='Qoosky',
        author_email='qoosky.webshop@gmail.com',
        classifiers=[
            'Programming Language :: Python :: 3 :: Only',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
        ],
        python_requires='>=3',
        install_requires=[],
    )

if __name__ == '__main__':
    Main()
