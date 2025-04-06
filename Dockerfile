# Use Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY app.py /app

# Install dependencies
RUN pip install flask requests

# Expose the webhook port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

