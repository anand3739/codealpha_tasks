import requests
import folium

# Get user's IP address location
try:
    response = requests.get("http://ip-api.com/json/")
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()

    # Extract latitude and longitude
    if data["status"] == "success":
        latitude = data["lat"]
        longitude = data["lon"]

        # Create a map centered at user's location
        user_map = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup="Your Location").add_to(user_map)

        # Save map as an HTML file
        user_map.save("user_location_map.html")

        print("Map saved as 'user_location_map.html'. Open it in a browser to view.")
    else:
        print("Failed to retrieve location. Ensure your IP is accessible.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching location: {e}")
