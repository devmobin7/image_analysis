## Image Summarization Service

This Django project exposes an API endpoint that utilizes the CHAT GPT v4 Vision API to generate summaries for images.

**Base URL:** `http://0.0.0.0:8000/`  
**API Endpoint:** `perform-analysis/`  
**Front-End Endpoint:** `upload-picture/`

To perform testing, follow these steps: 

1. Replace `OPENAI_API_KEY` with your unique API key.
2. Execute migrations using the command: `python manage.py makemigrations && python manage.py migrate`.
3. Launch the Docker container with the command: `docker-compose up --build`.

### Additional Achievements

- Implementation of Dockerization for seamless deployment.

### Developer

Authored by: Ansar Khan
