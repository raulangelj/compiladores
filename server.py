from flask import Flask, request, jsonify
from main import evaluate_code
from antlr4 import *
from flask_cors import CORS
import json
import io


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

@app.route('/', methods=['POST'])
def my_endpoint():
  # Extracting the parameter named 'code' from the POST request
  dictionary_obj = json.loads(request.get_data())
  
  if not dictionary_obj['code']:
    return jsonify({"error": "Parameter 'code' not provided"}), 400

  # Process the parameter as needed
  # For this example, we'll just return it in the response
  success, errors = evaluate_code(InputStream(dictionary_obj['code']))
  return jsonify({"errors": errors, "success": success})
