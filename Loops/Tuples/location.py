# Version 1
def main():
    coordinates = (42.376, -71.115)
    latitude, longtitude = coordinates
    print(f"Latitude: {coordinates[0]}")
    print(f"Longtitude: {coordinates[1]}")

main()


# Version 2
import sys

def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = (42.376, -71.115)
    print(f"{sys.getsizeof(coordinates_tuple)} bytes") 
    print(f"{sys.getsizeof(coordinates_list)} bytes")

main()
