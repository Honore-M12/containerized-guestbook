# Containerized Guestbook

A multi-container web application orchestrated with Docker Compose, with a CI/CD pipeline that automatically tests and publishes the Docker image on every push.

![CI Pipeline](https://github.com/Honore-M12/containerized-guestbook/actions/workflows/ci.yml/badge.svg)

## Architecture

Browser → Nginx (port 80) → Flask (port 5000) → PostgreSQL (port 5432)

## Tech Stack

- **Nginx** — reverse proxy, handles incoming HTTP requests
- **Flask** — Python web application, handles business logic
- **PostgreSQL** — relational database, persists messages

## CI/CD Pipeline

Every push to `main` triggers a two-job GitHub Actions pipeline:

1. **Test** — installs dependencies, runs `pytest` and `flake8`
2. **Build & Push** — builds the Docker image and pushes it to Docker Hub

The build job only runs if the test job passes.

## Getting Started

```bash
git clone https://github.com/Honore-M12/containerized-guestbook.git
cd containerized-guestbook
docker compose up --build
```

> **Note — if `docker compose up --build` fails with a `buildx` error:**
> This happens on some systems where the buildx plugin is not correctly linked.
> Run the following commands, then retry:
> ```bash
> sudo apt install docker-buildx -y
> sudo ln -s /usr/libexec/docker/cli-plugins/docker-buildx /usr/local/lib/docker/cli-plugins/docker-buildx
> ```
> The first command installs the buildx plugin. The second creates a symbolic link
> so Docker can find it in the expected location.

Then open http://localhost in your browser.

## Key Concepts Demonstrated

- Multi-container orchestration with Docker Compose
- Nginx as a reverse proxy
- Data persistence with Docker volumes
- Environment variables for service configuration
- Container networking (services communicate by name)
- Automated testing with pytest and flake8
- CI/CD pipeline with GitHub Actions
- Docker image publishing to Docker Hub
