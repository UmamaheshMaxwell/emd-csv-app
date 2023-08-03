# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app


COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "emd.py"]




