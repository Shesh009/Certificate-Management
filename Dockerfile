# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any necessary packages from requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 available for the Streamlit app
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "Total.py"]
