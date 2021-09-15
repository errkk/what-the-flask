# syntax=docker/dockerfile:1

# This file tells docker what stuff we want on the container
# Relevant at build time
# Specifically, this file defines an Image, and contains a list of steps to create the image, such as:
# How to configure the os
# What software to install
# When we run the build command, Docker will read through all of these lines IN ORDER and make the Image for us
# We can then run the image to get a container

# Let's configure the environment ! 
# It's based off a container someone else already made, that can do python!

# Firstly, define the underlying operating system (the base/parent image from which you are building)
# Dockerfiles ALWAYS start with a FROM command
# we want python with alpine installed (alpine makes images as small as possible)
FROM python:3.7-alpine

# We do need to install a bunch of stuff tho. hey ho.
# The RUN instruction will execute any commands in a new layer on top of the current image and commit the results
# The resulting committed image will be used for the next step in the Dockerfile.
RUN apk add --no-cache gcc musl-dev linux-headers libressl-dev musl-dev libffi-dev python3-dev bash make libevent-dev build-base postgresql-dev postgresql-client

# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
# We're going to keep everything in this /code folder (on the container); it doesn't know about the rest of our stuff
WORKDIR /code

# Copy our files (list of requirements) inside the image using the COPY keyword.
# Copy contents of what-the-flask/requirements.txt, into the container @ /code/requirements.txt
COPY requirements.txt requirements.txt

# RUN tells the package manager, pip, to install the python dependencies in /code
# It's like yarn or NPM
RUN pip install -r requirements.txt

# EXPOSE means when we run the image and get the container, the container will listen on port 5000 on the host machine
# Therefore we can use Chrome, or an API client to see the web responses
EXPOSE 5000

# Copy our code over! This is so it can install. Copy our src folder into code/src
# Afterwards, we'll mount the volume, so we can edit the files as we go
COPY src src
WORKDIR /code/src

# This RUN command installs the project, so it knows its thing, and means that we can import stuff between files
# to make everything tidier
RUN python3 setup.py develop


#Environment variables are declared with the ENV statement
ENV FLASK_APP="server/app.py"
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST="0.0.0.0"

# This runs the development server, so its already going whenever we run docker-compose up
CMD ["flask", "run"]

# The first time you build, you have to download all the layers that make up the image
# Then it copies our files inside
# At the end, it outputs our new image