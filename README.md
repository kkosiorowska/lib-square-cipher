# lib-square-cipher

## Create a file

* python setup.py sdist

## Install pypiserver

* pip install pypiserver

## Running pypiserver

* pypi-server -p 8080 ./packages &

## Download and install hosted packages

* pip install --extra-index-url http://localhost:8080 lib-square-cipher==1.0
* pip install --extra-index-url http://localhost:8080 lib-square-cipher==2.0
* pip install --extra-index-url http://localhost:8080 lib-square-cipher==3.0

## Uninstall hosted packages

* pip uninstall lib-square-cipher

