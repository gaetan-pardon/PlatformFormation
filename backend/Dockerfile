# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.13.12
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN apt-get update && apt-get install -y --no-install-recommends curl gnupg unixodbc

    #curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    # Automatically use the correct Debian/Ubuntu version
#RUN curl https://packages.microsoft.com/config/debian/$(. /etc/os-release && echo "$VERSION_ID")/prod.list > /etc/apt/sources.list.d/mssql-release.list 
#RUN apt-get update 
# RUN ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 
# optional: mssql-tools18 if you want sqlcmd/isql
# ACCEPT_EULA=Y apt-get install -y --no-install-recommends mssql-tools18 && \
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python -m uvicorn main:app --host 0.0.0.0
