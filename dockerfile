# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy program and requirements
COPY library_fine_calculator.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the program
CMD ["python", "library_fine_calculator.py"]