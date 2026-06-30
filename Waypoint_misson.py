waypoints = ( 
    ("WP1", 23.0225, 72.5714, 50), 
    ("WP2", 23.0312, 72.5801, 80), 
    ("WP3", 23.0401, 72.5900, 100), 
    ("WP4", 23.0225, 72.5714, 0), 
)

# 1. Total number of waypoints
print("Total waypoints:", len(waypoints))

# To do Tuple unpacking to to print each waypoint's details in a formatted line 
for waypoint in waypoints:
    name, latitude, longitude, altitude = waypoint
    print(f"{name}: Latitude={latitude}, Longitude={longitude}, Altitude={altitude}")

# To Find the waypoint with the highest altitude
highest = waypoints[0]
#waypoint[3] is altitude as it is the 4th in tuple.
for waypoint in waypoints:
    if waypoint[3] > highest[3]:
        highest = waypoint

print("Highest altitude waypoint:", highest)

# To check Check if WP2 exists
print(("WP2", 23.0312, 72.5801, 80) in waypoints)

#to modify WP1's altitude
#we use try and except as its a tuple and its values cant be changed
try:
    waypoints[0][3] = 60
except TypeError:
    print("Waypoint data is immutable — mission integrity protected!")
