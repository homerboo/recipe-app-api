FROM python:3.8-alpine
#who is maintianing
LABEL key="homerboo" 
# python unbuffered environment variable
# recommended value for python in docker containers
#    The output won't be buffered and will be printed directly
ENV PYTHONUNBUFFERED 1

# Point to dependencies
# COPY Source WhereInDockerImageShouldItBe
COPY ./requirements.txt /requirements.txt

# Intsall into the docker image requirements file using pip
RUN pip install -r /requirements.txt

# Make directory for application source code
#  1. Creates an empty folder on the docker image called app
#  2. Switches to that as the default directory
#     Any application we run using the docker container will start here
#     Unless otherwise specified
#  3. Copies from local machine app onto the app directory on the image
#     Allows us to take the code into the docker image
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create user to run app using docker
# -D means run applications only
RUN adduser -D user

# Switch docker to user
# This is for security
#  Otherwise the image will run using root
#   which means if someone compromises app, they are root (can do anything), user limits scope
USER user