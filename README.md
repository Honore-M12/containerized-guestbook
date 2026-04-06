# Containerized Guestbook

A multi-container web application orchestrated with Docker Compose.
Users can post and read messages through a simple web interface.

## Architecture
Browser → Nginx (port 80) → Flask (port 5000) → PostgreSQL (port 5432)
## Tech Stack

- **Nginx** — reverse proxy, handles incoming HTTP requests
- **Flask** — Python web application, handles business logic
- **PostgreSQL** — relational database, persists messages

## Getting Started
```bash
git clone https://github.com/Honore-M12/containerized-guestbook.git
cd containerized-guestbook
docker compose up --build
```

Then open http://localhost in your browser.

## Key Concepts Demonstrated

- Multi-container orchestration with Docker Compose
- Nginx as a reverse proxy
- Data persistence with Docker volumes
- Environment variables for service configuration
- Container networking (services communicate by name)
