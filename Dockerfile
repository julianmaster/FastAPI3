# Use the official Python image
FROM python:3.12-slim

COPY src/requirements.txt app/requirements.txt
WORKDIR /app
RUN pip install -r /app/requirements.txt
COPY ./src /app/src

RUN ["python", "src/utils/embedding.py"]

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]
