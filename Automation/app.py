import json
from pathlib import Path

from flask import Flask, jsonify

equipment_file = Path(__file__).resolve().parent.parent / "config" / "equipment.json"

with equipment_file.open("r", encoding="utf-8") as f:
    equipment = json.load(f)

app = Flask(__name__)


@app.get("/api/equipment")
def get_equipment():
    return jsonify(list(equipment.values()))


@app.get("/api/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    item = equipment.get(str(equipment_id))
    if item is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)