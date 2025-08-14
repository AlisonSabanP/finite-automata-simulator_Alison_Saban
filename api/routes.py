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
        print(data)
    except Exception as e:
        return jsonify({"error": f"Error al leer JSON: {str(e)}"}), 400

    if not isinstance(data, list):
        return jsonify({"error": "El JSON debe ser una lista de autómatas"}), 400

    results = []
    required_fields = ["id","name","initial_state","acceptance_states","alphabet","states","transitions","test_strings"]

    for automaton_data in data:
        if not isinstance(automaton_data, dict):
            return jsonify({"error": "Cada autómata debe ser un diccionario"}), 400

        missing_fields = [field for field in required_fields if field not in automaton_data]
        if missing_fields:
            results.append({
                "id": automaton_data.get("id", None),
                "success": False,
                "error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"
            })
            continue

        automaton = Automata(automaton_data)
        is_valid = automaton.validate()

        result = {"id": automaton.id}

        if not is_valid:
            result["success"] = False
            result["error"] = automaton.error
        else:
            result["success"] = True
            result["inputs_validation"] = automaton.validate_inputs()
        
        results.append(result)


    return jsonify(results), 200
