from flask import Flask, request, jsonify
from dotenv import load_dotenv

from src.classifier import classify_file
from src.validate_file_type import allowed_file

load_dotenv()

app = Flask(__name__)

@app.route('/classify_file', methods=['POST'])

def classify_file_route():

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    file_class = classify_file(file)
    return jsonify({"file_class": file_class}), 200


if __name__ == '__main__':
    app.run(debug=True)
