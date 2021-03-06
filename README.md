# Monet API

API created from plain text files through a django command.

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

Run the migrate command to have the db structure on your local db:

```bash
pipenv run migrate
```

Run the following command with the plain file to process:
```bash
pipenv run file_process FILE_PATH
```

And then you can run the server and go to te api/control  and api/detalle endpoints
to check if the file info is in the API.
```bash
pipenv run server
```


Note: The migrate, server and file_process commands are configured in the Pipfile.


