# import requests
#
# def get_static_map_image(api_key, latitude, longitude, zoom=50, size="600x600"):
#     url = "https://maps.googleapis.com/maps/api/staticmap?"
#     params = {
#         "center": f"{latitude},{longitude}",
#         "zoom": zoom,
#         "size": size,
#         "maptype": "roadmap",
#         "key": api_key
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         with open("static_map_image.png", "wb") as f:
#             f.write(response.content)
#         print("Image saved successfully")
#     else:
#         print("You're cooked")
#         print(response.text)
# api_key = "AIzaSyCDrGL3HSnEwtnox2Q_h19gAtEVYfUlLIE"
# lat = 44.822456
# longitude = -93.47169
# get_static_map_image(api_key, lat, longitude)
import requests
from geopy.geocoders import Nominatim
def street_view(address):
    geolocator = Nominatim(user_agent="storeFrontVisibility")
    location = geolocator.geocode(address)
    lat = location.latitude
    lon = location.longitude
    get_street_view_image("AIzaSyCDrGL3HSnEwtnox2Q_h19gAtEVYfUlLIE", lat, lon)
def get_street_view_image(api_key, latitude, longitude, heading=180, pitch=0, size="400x400"):
    url = "https://maps.googleapis.com/maps/api/streetview?"
    params = {
        "size": size,
        "location": f"{latitude},{longitude}",
        "heading": heading,  # Direction of the camera
        "pitch": pitch,  # Angle of the camera (e.g., 0 is straight ahead)
        "key": api_key
    }

    # Send the request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the street view image to a file
        with open("street_view_image.png", "wb") as f:
            f.write(response.content)
        print("Street view image saved successfully.")
    else:
        print(f"Request failed. Status code: {response.status_code}")
        print(response.text)


# Example coordinates (e.g., San Francisco)
api_key = "AIzaSyCDrGL3HSnEwtnox2Q_h19gAtEVYfUlLIE"
lat = 37.502057  # Georgia TECH
lon = -121.966960  # GATECH
get_street_view_image(api_key, lat, lon)
