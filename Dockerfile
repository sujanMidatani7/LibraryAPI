FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy local code to the container image
COPY . .
# Make /app the working directory for all


RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc && \
    . ~/.bashrc && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only=main

EXPOSE 80

# Run the web service on container startup
CMD ["uvicorn", "main:app", "--reload"]