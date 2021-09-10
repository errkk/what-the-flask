# syntax=docker/dockerfile:1

# This file tells docker what stuff we want on the container
# When we run the build command, it will step through all of these lines and make the container for us


# It's based off a container someone else already made, that can do python!
FROM python:3.7-alpine

# We do need to install a bunch of stuff tho. hey ho.
RUN apk add --no-cache gcc musl-dev linux-headers libressl-dev musl-dev libffi-dev python3-dev bash make libevent-dev build-base postgresql-dev postgresql-client

# We're going to keep everything in this /code folder (on the container) it doesn't know about the rest of our stuff
WORKDIR /code

# First we copy this list of requirements.
# Tells the package manager, pip, to install the python dependencies
# It's like yarn or NPM
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# We're going to bind to port 5000 on the host machine, so we can use Chrome, or an API client to see the web responses
EXPOSE 5000

# Copy the code over! This is so it can install.
# Afterwards, we'll mount the volume, so we can edit the files as we go
COPY src src
WORKDIR /code/src

# This installs the project, so it know's it's thing, and means that we can import stuff between files
# to make verything tidier
RUN python3 setup.py develop

ENV FLASK_APP="server/app.py"
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST="0.0.0.0"

# This runs the development server, so its already going whenever we run docker-compose up
CMD ["flask", "run"]
