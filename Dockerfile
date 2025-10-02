# Use an official lightweight Python image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port Gunicorn will run on. Cloud Run expects 8080 by default.
EXPOSE 8080

# The command to run your application in production
CMD ["gunicorn", "portfolio_backend.wsgi", "--bind", "0.0.0.0:8080"]