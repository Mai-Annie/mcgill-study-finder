from utils.google_api import search_place, get_place_details

print("Testing Google Places API...")

# Test 1: Search for Starbucks
print("\n1. Searching for Starbucks...")
place_id = search_place("Starbucks", "3505 McTavish Montreal")

if place_id:
    print(f"✅ Found place_id: {place_id}")
    
    # Test 2: Get details
    print("\n2. Getting place details...")
    details = get_place_details(place_id)
    
    if details:
        print(f"✅ Place name: {details.get('name')}")
        print(f"✅ Address: {details.get('formatted_address')}")
        print(f"✅ Rating: {details.get('rating')}")
    else:
        print("❌ Failed to get details")
else:
    print("❌ Failed to find place")
