FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy local code to the container image
COPY . .

# Install uvicorn
RUN pip install uvicorn

# Install dependencies using Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only=main

EXPOSE 8000

# Run the web service on container startup
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
