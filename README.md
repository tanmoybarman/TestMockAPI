# Healthcare Mock API

A FastAPI-based mock API service for healthcare data with pre-defined endpoints for testing and development.

## Features

- RESTful API endpoints for member, coverage, and accumulator data
- Built with FastAPI for high performance
- Automatic API documentation with Swagger UI and ReDoc
- CORS enabled for cross-origin requests
- Health check endpoint
- Environment variable configuration

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TestMockAPI
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

### Development Mode

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## API Documentation

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- **Health Check**: `/health`

## Available Endpoints

### Member Endpoints
- `GET /searchMemberById/m-a` - Get member details for ID 'm-a'
- `GET /searchMemberById/m-b-m-n` - Get member details for ID 'm-b-m-n'
- `GET /searchMemberById/m-n-a-c` - Get member details for ID 'm-n-a-c'
- `GET /searchMemberById/m-e-r` - Simulate error response for member search

### Coverage Endpoints
- `GET /searchCoverageById/c-s` - Get coverage details for ID 'c-s'
- `GET /searchCoverageById/c-n-m-id` - Get coverage details for ID 'c-n-m-id'
- `GET /searchCoverageById/c-n-a-c` - Get coverage details for ID 'c-n-a-c'
- `GET /searchCoverageById/c-e-r` - Simulate error response for coverage search

### Accumulator Endpoints
- `GET /searchAccums/acc-succ` - Get accumulator details for ID 'acc-succ'
- `GET /searchAccums/acc-rem-amt-miss` - Get accumulator details for ID 'acc-rem-amt-miss'
- `GET /searchAccums/acc-f` - Simulate error response for accumulator search

## Environment Variables

- `PORT` - Port to run the server on (default: 8000)
- `ALLOWED_ORIGINS` - Comma-separated list of allowed origins (default: "*")
- `ENV` - Environment (development/production)

## Example Requests

```bash
# Get member details
curl http://localhost:8000/searchMemberById/m-a

# Get coverage details
curl http://localhost:8000/searchCoverageById/c-s

# Get accumulator details
curl http://localhost:8000/searchAccums/acc-succ
```

## Deployment

### Local Deployment
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Cloud Deployment
This API can be deployed to any cloud platform that supports Python applications, such as:
- AWS Elastic Beanstalk
- Google App Engine
- Microsoft Azure App Service
- Heroku
- Railway

## License

[Specify your license here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

