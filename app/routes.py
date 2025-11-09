from flask import Blueprint, jsonify, request

# Create a "Blueprint" to group routes (Flask best practice)
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "ACEest Fitness API running"}), 200

@bp.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@bp.route('/echo', methods=['POST'])
def echo():
    """
    Accept JSON body and return it back under 'you_sent'.
    This matches the pytest test which posts {"name": "Neha"}.
    """
    data = request.get_json(silent=True)
    # If no JSON was provided, return a helpful error and 400 status
    if data is None:
        return jsonify({"error": "Invalid or missing JSON in request body"}), 400
    return jsonify({"you_sent": data}), 200
