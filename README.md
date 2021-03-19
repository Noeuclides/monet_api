# Monet API

This repository has a django command that fills the database to look that info at the 
api endpoints.

## Requirements
Python3.7 or greater.

You have to set mysql on your local machine.

On linux you may need to run:

```bash
sudo apt-get install python3.7-dev libmysqlclient-dev
```

To run the django app use the python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).


## Installation

Install the dependencies:

```bash
pipenv install
```

Configure mysql database:
```bash
pipenv run python configDB.py 
```

## Usage
Run the following command with the plain file to process:
```bash
pipenv run file_process FILE_PATH
```

And then run the django server:

```bash
pipenv run migrate
pipenv run server
```
Note: The migrate and server commands are set in the Pipfile.

Go to te api/control  and api/detalle endpoints.
