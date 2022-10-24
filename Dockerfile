# Base image
FROM python:3.10

# Working directory
WORKDIR /psswrd

# Dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy content to working directory
COPY src/ /psswrd/src
COPY data/ /psswrd/data
COPY tests/ /psswrd/tests
