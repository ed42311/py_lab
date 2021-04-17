# Random python tools #

## What is this repository for? ##

Python is a great langauge for quick prototyping
It is the langauge that runs the core of the AWS CLI with [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
It's also just great.

* Using [Pipenv](https://packaging.python.org/tutorials/managing-dependencies.html)

* Version
0.1.1
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## Setup

## Dev

**Activate the virtaul env**

`source env/bin/activate`

**Confirm the virtaul env**

`which python`

It should point to your virtaul env path:  `from/root/to/env/bin/python`

**Leave Virtaul Env**

`deactivate`

### Download aviationStack data

You will need a aviationStack Key

`python3 airport_reader.py`

### Upload to 3s

`python3 upload_to_s3.py`