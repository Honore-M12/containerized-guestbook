# Containerized Guestbook
A multi-container web application orchestrated with Docker Compose, featuring a CI/CD pipeline that automatically tests and publishes the Docker image on every push.

![CI Pipeline](https://github.com/Honore-M12/containerized-guestbook/actions/workflows/ci.yml/badge.svg)

## Architecture
Browser → Nginx (port 80) → Flask (port 5000) → PostgreSQL (port 5432)
                                ↘ prometheus ( port 9090)  → Grafana (port 3000)    
                                           ↓
                                Node-exporter (port 9100)
## Tech Stack

- **Nginx**: Reverse proxy, handles incoming HTTP requests
- **Flask**: Python web application, handles business logic
- **PostgreSQL**: Relational database, persists messages
- **Prometheus**: Monitoring tool, collects and stores metrics as time-series data
- **Grafana**: Visualization platform, used to analyze and visualize metrics in real time
- **Node Exporter**: Exposes system-level metrics (CPU, memory, disk) to Prometheus

## CI/CD Pipeline

Every push to `main` triggers a two-job GitHub Actions pipeline:

1. **Test**: Installs dependencies, runs `pytest` and `flake8`
2. **Build & Push**: Builds the Docker image and pushes it to Docker Hub

*The build job only runs if the test job passes.*

## Monitoring (Prometheus + Grafana)

The application is instrumented with custom Prometheus metrics, exposed on `/metrics`:

| Metric | Type | Description |
|--------|------|-------------|
| `messages_submitted_total` | Counter | Total messages submitted since startup |
| `messages_in_database_count` | Gauge | Current number of messages in the database |
| `message_length_chars` | Histogram | Distribution of submitted message lengths |

System-level metrics (CPU, memory, disk) are collected via Node Exporter and available in Grafana alongside application metrics.

## Getting Started

```bash
git clone https://github.com/Honore-M12/containerized-guestbook.git
cd containerized-guestbook
docker compose up --build
```

> **Note: if `docker compose up --build` fails with a `buildx` error:**
> This happens on some systems where the buildx plugin is not correctly linked.
> Run the following commands, then retry:
> ```bash
> sudo apt install docker-buildx -y
> sudo ln -s /usr/libexec/docker/cli-plugins/docker-buildx /usr/local/lib/docker/cli-plugins/docker-buildx
> ```
> The first command installs the buildx plugin. The second creates a symbolic link so Docker can find it in the expected location.

| Service | URL | Notes |
|---------|-----|-------|
| Guestbook | http://localhost | Main application |
| Prometheus | http://localhost:9090 | Query and explore metrics |
| Grafana | http://localhost:3000 | Dashboards and visualization (`admin/admin`) |

## Key Concepts Demonstrated

- Multi-container orchestration with Docker Compose
- Nginx as a reverse proxy
- Data persistence with Docker volumes
- Environment variables for service configuration
- Container networking (services communicate by name)
- Automated testing with `pytest` and `flake8`
- CI/CD pipeline with GitHub Actions
- Docker image publishing to Docker Hub
- Application instrumentation with custom Prometheus metrics
- System monitoring with Node Exporter
- Real-time visualization with Grafana dashboards
