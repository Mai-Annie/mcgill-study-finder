from flask import Flask, jsonify #allows me to create a web swerver
from flask_cors import CORS 
import json #library for reading/writing json files
import os 
from dotenv import load_dotenv #library for loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# helper function to read locations from a JSON file
def load_locations():
    with open('locations.json', 'r') as f:
        return json.load(f)
    
# function to check if API is running
@app.route('/')
def home():
    return jsonify({
        "message": "McGill Study Finder API",
        "status": "running",
        "version": "0.1.0"
    })

# endpoint to get locations data
@app.route('/api/locations')
def get_locations():
    locations = load_locations()
    return jsonify({
        "success": True,
        "count": len(locations),
        "data": locations
    })

# function to find a specific location by its ID
@app.route('/api/locations/<int:location_id>')
def get_location(location_id):
    locations = load_locations()
    location = next((loc for loc in locations if loc['id'] == location_id), None)
    if location:
        return jsonify({
            "success": True,
            "data": location
        })
    else:
        return jsonify({
            "success": False,
            "message": "Location not found"
        }), 404 

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
