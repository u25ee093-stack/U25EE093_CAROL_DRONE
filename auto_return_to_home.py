drone_state = { 
    "battery": 18, 
    "altitude": 95, 
    "signal_strength": 40,  # percent 
    "distance_from_home": 850,  # metres 
    "wind_speed": 38,        # km/h 
    "obstacle_detected": True 
}
# to check RTH
triggered = False

if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered — Low Battery")
    triggered = True

if drone_state["signal_strength"] < 30:
    print("WARNING: RTH triggered — Signal Lost")
    triggered = True

if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered — High Wind")
    triggered = True

if drone_state["obstacle_detected"] == True:
    print("CAUTION: Obstacle detected — Rerouting")
    triggered = True

if not triggered:
    print("All systems nominal")


# While loop: descent simulation and battery drain by 1%
altitude = drone_state["altitude"]
battery = drone_state["battery"]

while altitude > 0:
    altitude -= 15
    if altitude < 0:
        altitude = 0

    battery -= 1
    if battery < 0:
        battery = 0

    print("Altitude:", altitude, "; Battery:", battery)