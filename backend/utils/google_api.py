import requests #library that makes web requests and intereacts with APIS
import os
from dotenv import load_dotenv #library for loading environment variables from a .env file
import urllib.parse

# Load .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_BASE_URL = "https://places.googleapis.com/v1/places/"

# Function to search for a place and get its place_id
def search_place(name, address):
    """Search using New Places API"""
    query = f"{name} {address}"
    
    url = "https://places.googleapis.com/v1/places:searchText"
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_API_KEY,
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress"
    }
    
    body = {
        "textQuery": query
    }
    
    print(f"Sending query: {query}")
    print(f"Body: {body}")
    
    try:
        response = requests.post(url, json=body, headers=headers)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('places'):
                place_id = data['places'][0]['id']
                return place_id.replace('places/', '')
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")
    
    return None



# Function to get detailed info about a place using its place_id
def get_place_details(place_id):
    """
    Get detailed info about a place
    
    Args:
        place_id: Google's unique place identifier
    
    Returns:
        Dictionary with place details
    """
    # Ensure place_id has correct format
    if not place_id.startswith('places/'):
        place_id = f"places/{place_id}"
    
    url = f"{GOOGLE_BASE_URL}/{place_id}"
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_API_KEY,
        "X-Goog-FieldMask": "displayName,formattedAddress,rating,regularOpeningHours,location"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting details: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")
    
    return None