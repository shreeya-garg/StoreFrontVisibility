import requests
from geopy.geocoders import Nominatim

def get_nearby_streets(address):
    geolocator = Nominatim(user_agent = "storeFrontVisibility")
    location = geolocator.geocode(address)
    if location:
        lat = location.latitude
        lon = location.longitude
        print(f"lat: {lat}, long: {lon}")
        overpass_url = "https://overpass-api.de/api/interpreter"

        overpass_query = f"""
        [out:json];
        (
          node(around:100, {lat}, {lon})[highway];
          way(around:100, {lat}, {lon})[highway];
          relation(around:100, {lat}, {lon})[highway];
        );
        out body;
        """
        response = requests.get(overpass_url, params={'data': overpass_query})
        if response.status_code == 200:
            data = response.json()
            streets = set()
            for element in data['elements']:
                if 'tags' in element and 'name' in element['tags']:
                    streets.add(element['tags']['name'])
            if streets:
                print("Nearby streets:")
                for street in streets:
                    print(street)
            else:
                print("No nearby streets found.")
        else:
            print(f"Error {response.status_code}: {response.text}")
    else:
        print("Address not found.")

# Example usage
address = "1600 Pennsylvania Ave NW, Washington, DC 20500, USA"
get_nearby_streets(address)

# import requests
# from geopy.geocoders import Nominatim
# import certifi
#
#
# def get_nearby_streets(address):
#     geolocator = Nominatim(user_agent="storeFrontVisibility")
#
#     # Force requests to use certifi certificates
#     session = requests.Session()
#     session.verify = certifi.where()  # Use certifi's certificate bundle
#
#     location = geolocator.geocode(address)
#     if location:
#         lat = location.latitude
#         lon = location.longitude
#         print(f"lat: {lat}, long: {lon}")
#         overpass_url = "http://overpass-api.de/api/interpreter"
#         overpass_query = f"""
#         [out:json];
#         (
#             node(around: 500, {lat}, {lon})[highway]
#             way(around: 500, {lat}, {lon})[highway]
#             relation(around: 500, {lat}, {lon})[highway]
#         );
#         out body;
#         """
#         response = session.get(overpass_url, params={'data': overpass_query})  # Use session with certifi
#         if response.status_code == 200:
#             data = response.json()
#             streets = set()
#             for element in data['elements']:
#                 if 'tags' in element and 'name' in element['tags']:
#                     streets.add(element['tags']['name'])
#             if streets:
#                 print("Nearby streets:")
#                 for street in streets:
#                     print(street)
#             else:
#                 print("No nearby streets found.")
#         else:
#             print("Error retrieving data from Overpass API.")
#     else:
#         print("Address not found.")
#
#
# # Example usage
# address = "1600 Pennsylvania Ave NW, Washington, DC 20500, USA"
# get_nearby_streets(address)
