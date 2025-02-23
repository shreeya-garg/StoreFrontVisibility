from getNearbyStreets import get_nearby_streets_with_osm_id
from mapStaticImage import get_street_view_image
from traffic_reader import traffic_for_osm

def main():
    address = input("Enter address: ")
    output = get_nearby_streets_with_osm_id(address)
    for (street, osm_id, lat, long) in output:
        get_street_view_image("AIzaSyCDrGL3HSnEwtnox2Q_h19gAtEVYfUlLIE", lat, long)
        traffic = (traffic_for_osm(osm_id))

main()