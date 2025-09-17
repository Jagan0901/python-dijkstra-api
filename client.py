import requests

PAYLOAD = {
    "graph": {"A": {"B": 2}, "B": {"D": 5}, "D": {}},
    "source": "A",
    "target": "D"
}

if __name__ == "__main__":
    resp = requests.post('http://localhost:5000/shortest_path', json=PAYLOAD)
    print(resp.json())
