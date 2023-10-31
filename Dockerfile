# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

VOLUME /app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

RUN pip install --upgrade pip

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose any required ports (if your application needs to listen on a specific port)
# EXPOSE 8000

# Command to run your Python application (replace "app.py" with your script's filename)
CMD ["bash"]

