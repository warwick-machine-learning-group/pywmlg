# use the base python image
FROM python:3.9

# set a project directory and move to this directory
ENV PROJECT_DIR /app/pywmlg
WORKDIR ${PROJECT_DIR}

# copy the project to the docker image
COPY . ${PROJECT_DIR}

# install the python package
RUN pip install ${PROJECT_DIR}