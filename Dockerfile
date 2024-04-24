# Ansar Khan

# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        musl-dev \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose the port on which the development server will run
EXPOSE 8000

# Command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
