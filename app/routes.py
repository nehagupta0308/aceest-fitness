from flask import Blueprint, jsonify

# Create a "Blueprint" to group routes (Flask best practice)
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "ACEest Fitness API running"}), 200

@bp.route('/health')
def health():
    return jsonify({"status": "ok"}), 200