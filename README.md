# Brython Quickstart

## Installation

Get the Brython source files:

```
cd ~/dev
git clone https://github.com/brython-dev/brython
```

In project root:

```
mkvirtualenv -p python3 brython
pip install Invoke
ln -s ~/dev/brython/www/src brython
```

## Running the server

```
inv serve
```
