# Shortest-Path Microservice (Dijkstra API)

## Overview
A Python REST API that computes the **shortest path in weighted graphs** using **Dijkstra’s algorithm**.  
Designed as a clean microservice to demonstrate algorithmic problem solving, API design, and unit testing — perfect for showcasing coding and system design skills.

---

## Features
- Compute shortest paths between nodes in a weighted graph.
- REST API endpoint (`/shortest_path`) returns distance and path as JSON.
- Handles edge cases (disconnected graphs, invalid requests).
- Unit-tested core algorithm using **pytest**.
- Example client script to interact with the API.

---

## Tech Stack
- Python 3.10+
- Flask (REST API)
- Pytest (unit testing)
- Requests (client script)

---

## Folder Structure
```
python-dijkstra-api/
 ├─ app/
 │   ├─ __init__.py
 │   ├─ app.py           # Flask server
 │   └─ dijkstra.py      # Dijkstra algorithm
 ├─ tests/
 │   ├─ test_dijkstra.py # Unit tests
 │   └─ conftest.py      # Adds project root to sys.path
 ├─ client.py            # Example client script
 ├─ requirements.txt
 ├─ .gitignore
 └─ README.md
```

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/Jagan0901/python-dijkstra-api.git
cd python-dijkstra-api
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows CMD:**
```cmd
venv\Scripts\activate
```

**Linux / Git Bash / macOS:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running the API

Start the Flask server:
```bash
python -m app.app
```

Server will run at: `http://127.0.0.1:5000` (or your local network IP).

---

## Example Client Usage

```python
import requests

PAYLOAD = {
    "graph": {"A": {"B": 2}, "B": {"D": 5}, "D": {}},
    "source": "A",
    "target": "D"
}

resp = requests.post('http://127.0.0.1:5000/shortest_path', json=PAYLOAD)
print(resp.json())
```

Expected output:
```json
{"distance": 7.0, "path": ["A", "B", "D"]}
```

---

## Running Unit Tests

```bash
pytest -q
```

All tests should pass, verifying correctness of the Dijkstra implementation.

---

## Notes

- Handles disconnected graphs: returns `{"distance": null, "path": []}` if target is unreachable.
- Designed for easy extension to other shortest path algorithms (e.g., Bellman-Ford, A*).

---

