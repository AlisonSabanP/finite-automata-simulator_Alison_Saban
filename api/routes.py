from flask import Blueprint, request, jsonify
from app.automata import Automata 
import json

api = Blueprint('api', __name__)

@api.route('/process-automata', methods=['POST'])
def process_automata():
    if 'file' not in request.files:
        return jsonify({"error": "No se envió archivo"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nombre de archivo vacío"}), 400

    try:
        data = json.load(file)
    except Exception as e:
        return jsonify({"error": f"Error al leer JSON: {str(e)}"}), 400

    if not isinstance(data, list):
        return jsonify({"error": "El JSON debe ser una lista de autómatas"}), 400

    results = []  

    for automaton_data in data:
        if not isinstance(automaton_data, dict):
            return jsonify({"error": "Cada autómata debe ser un diccionario"}), 400

        automaton = Automata(automaton_data)

        is_valid = automaton.validate()

        result = {"id": automaton.id}

        if not is_valid:
            result["success"] = False
        else:
            result["success"] = True

        results.append(result)

    return jsonify(results), 200

