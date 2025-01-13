from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data from JSON file
def load_data():
    with open("q-vercel-python.json", "r") as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Load data from the JSON file
    data = load_data()

    # Extract 'name' parameters from the request
    names = request.args.getlist('name')

    # Find marks for the requested names
    marks = [item['marks'] for item in data if item['name'] in names]

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
