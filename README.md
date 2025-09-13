# 🐍 Python — Shortest Path Microservice (Work in Progress 🚧)

## 📌 Overview
This project implements a REST API in Python using **Flask** that computes the **shortest path** in a weighted graph using **Dijkstra’s algorithm**.

The API accepts a graph (nodes, edges, weights) as input in JSON format and returns:
- ✅ The shortest distance from source to target  
- ✅ The shortest path (list of nodes)

This is part of my portfolio projects for the **Google Software Application Development Apprenticeship**.

---

## 🚀 Planned Features
- Implement Dijkstra’s algorithm with a min-heap (priority queue)
- REST API endpoint (`/shortest_path`) using Flask
- Input validation and error handling
- Unit tests with **pytest**
- Example usage with `curl` and Postman
- Complexity analysis (Big-O notation)
- Dockerfile for containerization (optional)

---

## 📂 Project Structure (Planned)
```
python-dijkstra-api/
├── app/
│   ├── dijkstra.py       # Core algorithm
│   ├── app.py            # Flask app entry point
├── tests/
│   └── test_dijkstra.py  # Unit tests
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack
- Python 3.10+
- Flask (REST API)
- Pytest (testing)

---

## 📅 Timeline
- **Day 1:** Implement core Dijkstra algorithm + basic Flask endpoint  
- **Day 2:** Add unit tests + example requests  
- **Day 3:** Polish README + finalize demo  

---

## 🔗 Status
- ✅ Repo created  
- 🚧 Implementation in progress  
- ⏳ Code will be completed within 3 days  

---

## ✨ Future Improvements
- Add support for multiple source nodes  
- Extend to other shortest-path algorithms (Bellman-Ford, A*)  
- Deploy API on a cloud platform for public use  

---
