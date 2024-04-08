FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy local code to the container image
COPY . .
# Make /app the working directory for all
RUN python3 -m venv .venv
RUN source .venv/bin/activate
# RUN pip install uvicorn

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only=main

EXPOSE 80

# Run the web service on container startup
CMD ["uvicorn", "main:app", "--reload" ]