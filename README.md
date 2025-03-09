## Features
- Add tasks with a time limit.
- Start a timer for each task.
- Receive an alarm when the time limit expires.

## Requirements
- Python 3.9+
- Docker (optional)

## How to Run

### Without Docker
1. Clone the repository.
2. Run the application:
   ```bash
   python run.py
   
## With Docker
docker build -t docker-gui-app .
docker run -it -rm docker-gui-app