from flask import jsonify
import logging

def handle_404_error(error):
    return jsonify({"message": "Resource not found"}), 404

def handle_500_error(error):
    logging.error(f"Internal Server Error: {error}", exc_info=True)
    return jsonify({"message": "Internal server error"}), 500

def handle_all_exceptions(error):
    logging.error(f"An unexpected error occurred: {error}", exc_info=True)
    return jsonify({"message": "An unexpected error occurred"}), 500