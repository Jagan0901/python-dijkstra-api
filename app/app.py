from flask import Flask, request, jsonify
from app.dijkstra import shortest_path, DijkstraError

app = Flask(__name__)


@app.route('/shortest_path', methods=['POST'])
def shortest_path_endpoint():
    """POST JSON payload:
    {
      "graph": { "A": {"B": 5}, "B": {} },
      "source": "A",
      "target": "B"
    }

    Response JSON on success:
    { "distance": 5.0, "path": ["A", "B"] }

    If target unreachable: { "distance": null, "path": [] }
    """
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Empty request body"}), 400

    graph = data.get('graph')
    source = data.get('source')
    target = data.get('target')

    if graph is None or source is None or target is None:
        return jsonify({"error": "Request must include graph, source, and target"}), 400

    try:
        distance, path = shortest_path(graph, source, target)
    except DijkstraError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal error: " + str(e)}), 500

    return jsonify({"distance": distance, "path": path})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
