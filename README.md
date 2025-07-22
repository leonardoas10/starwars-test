# Star Wars CLI Application

A FastAPI backend service and CLI client for exploring the Star Wars API (SWAPI).

## Features

- FastAPI service with `/people` and `/planets` endpoints
- Query parameters: pagination, search, sorting
- CLI client with rich table output and loading spinners
- Docker support with environment variables
- Bonus AI insight endpoint
- Request logging and monitoring
- Unit tests included

## Setup

1. Copy environment file:
```bash
cp .env.example .env
```

### Local Development

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

4. Server runs on http://localhost:8000

### Docker

2. Build and run with docker-compose:
```bash
docker-compose up --build
```

3. Service available on http://localhost:6969

4. Run CLI with Docker:
```bash
# Option 1: Direct commands
docker-compose run --rm starwars-cli python cli.py people

# Option 2: Start CLI service and exec
docker-compose --profile cli up -d
docker-compose exec starwars-cli python cli.py people
```

## API Usage

### Endpoints

- `GET /people` - List Star Wars characters
- `GET /planets` - List Star Wars planets
- `GET /simulate-ai-insight` - Get AI insights (bonus)

### Query Parameters

- `page` (int): Page number (default: 1)
- `search` (str): Search by name (case-insensitive)
- `sort_by` (str): Sort by field (name, created, edited)

### Examples

```bash
# Get first page of people
curl "http://localhost:8000/people"

# Search for Luke
curl "http://localhost:8000/people?search=luke"

# Get planets sorted by name
curl "http://localhost:8000/planets?sort_by=name"

# AI insight endpoint
curl "http://localhost:8000/simulate-ai-insight?type=person&name=Luke"
```

## CLI Usage

### Install CLI

```bash
pip install -e .
```

### Commands

```bash
# List people
python cli.py people

# Search people
python cli.py people --search "luke"

# List planets with pagination
python cli.py planets --page 2

# Sort people by name (descending)
python cli.py people --sort-by name --order desc

# List planets with search and sort
python cli.py planets --search "desert" --sort-by name
```

### CLI Options

- `--page, -p`: Page number
- `--search, -s`: Search term
- `--sort-by`: Sort field (name, created, edited)
- `--order, -o`: Sort order (asc, desc)

## Environment Variables

Copy `.env.example` to `.env` and configure:

- `SWAPI_BASE_URL`: Base URL for SWAPI (default: https://swapi.dev/api)
- `API_BASE_URL`: Base URL for local API (default: http://localhost:8000)
- `EXTERNAL_PORT`: External port for Docker (default: 6969)
- `INTERNAL_PORT`: Internal port for FastAPI (default: 8000)

## Development

### API Documentation

Visit http://localhost:8000/docs for interactive API documentation.

### Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

### Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── models.py        # Pydantic models
├── tests/
│   ├── __init__.py
│   ├── test_api.py      # API tests
│   └── test_cli.py      # CLI tests
├── cli.py               # CLI client
├── setup.py             # Package setup
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md           # This file
```