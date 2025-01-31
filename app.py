from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DND_API_BASE_URL = "https://www.dnd5eapi.co/api/"

@app.route('/get_dnd_data', methods=['GET'])
def get_dnd_data():
    category = request.args.get("category", "")  # e.g., "monsters"
    item = request.args.get("item", "")  # e.g., "adult-red-dragon"

    if not category:
        return jsonify({"error": "No category provided"}), 400

    # Construct the full API URL
    api_url = f"{DND_API_BASE_URL}{category}"

    if item:
        api_url += f"/{item}"  # Append item name if provided

    response = requests.get(api_url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)
