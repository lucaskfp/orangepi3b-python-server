# Copilot Instructions for orangepi3b-python-server

## Project Overview
Minimal FastAPI REST API server designed for deployment on Orange Pi 3B hardware. The project uses containerized deployment with a Python 3.14 base image.

## Architecture
- **Entry point**: `app/main.py` - single-file FastAPI application
- **Package structure**: `app/` module with `__init__.py` marker
- **Deployment**: Docker container running on port 80 using FastAPI CLI

## Tech Stack & Dependencies
- **FastAPI 0.121.0**: Web framework (uses modern async/await patterns)
- **Uvicorn 0.38.0**: ASGI server with standard extras
- **Pydantic 2.12.3**: Data validation (v2 API - not compatible with v1 patterns)

## Development Workflow

### Running Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
fastapi dev app/main.py
# or production mode:
fastapi run app/main.py --port 80
```

### Docker Build & Run
```bash
# Build image
docker build -t python-server .

# Run container
docker run -p 80:80 python-server
```

## Code Conventions

### Route Definitions
- Use function-based route handlers (not class-based)
- Type hints required: use `Union[Type, None]` for optional query params (Python 3.9+ compatible)
- Path parameters in URL, query parameters as function arguments
- Example pattern from `app/main.py`:
  ```python
  @app.get("/items/{item_id}")
  def read_item(item_id: int, q: Union[str, None] = None):
      return {"item_id": item_id, "q": q}
  ```

### Project-Specific Patterns
- **No routers or blueprints**: All routes defined directly on the `app` instance in `main.py`
- **No models directory**: Pydantic models (when needed) should be defined in `main.py` or co-located with routes
- **No config abstraction**: Environment-specific settings not yet implemented
- **Synchronous handlers**: Use `def` (not `async def`) unless explicitly working with async operations

## Key Files
- `app/main.py`: Complete application logic and route definitions
- `requirements.txt`: Pinned dependency versions (always use exact versions as shown)
- `Dockerfile`: Production deployment configuration targeting port 80

## Hardware Context
This server targets Orange Pi 3B ARM hardware. Consider resource constraints when adding features (memory, CPU).
