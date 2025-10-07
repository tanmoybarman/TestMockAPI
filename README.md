# Healthcare Mock API Service

A mock API service that simulates healthcare-related endpoints for member, coverage, and accumulator data. This service is designed for testing and development purposes.

## Features

- **Member Search**: Retrieve member information by ID
- **Coverage Search**: Fetch coverage details by ID
- **Accumulator Search**: Get accumulator information by ID
- **Error Handling**: Simulates error responses for testing error handling
- **Response**: Returns hardcoded member details
- **Example**: 
  ```
  GET /searchMemberById/01234567
  ```

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. Navigate to the project directory:
   ```bash
   cd C:\Users\tanmoy\Documents\wind\MockAPI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the server using Uvicorn:
```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Testing the Endpoint

You can test the endpoint using curl or any API client:

```bash
curl http://localhost:8000/searchMemberById/01234567
```

Or open it directly in your browser:
```
http://localhost:8000/searchMemberById/01234567
```

## API Documentation

- **Interactive API docs (Swagger UI)**: `http://127.0.0.1:8000/docs`
- **Alternative API docs (ReDoc)**: `http://127.0.0.1:8000/redoc`

## Adding More Endpoints

To add more endpoints, edit the `main.py` file and add new route handlers as needed. Follow the same pattern as the existing endpoint.
