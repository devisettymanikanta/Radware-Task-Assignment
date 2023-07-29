# Based on linux OS latest image
FROM alpine:latest

# Define environment variable VERSION=1.2.0
ENV VERSION=1.2.0

# Install python, vim, zip, and unzip
RUN apk update && \
    apk add --no-cache python3 vim zip unzip

# Copy zip_job.py into the image's /tmp folder
COPY zip_job.py /tmp/

# Run a command to print OS type and architecture + verify /tmp/zip_job.py exists
CMD uname -a && ls -l /tmp/zip_job.py
