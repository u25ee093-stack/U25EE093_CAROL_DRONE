fleet = { 
    "PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2}, 
    "PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0}, 
    "PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8}, 
    "PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5}, 
}
#To Add PX4_005 with battery=95, altitude=0, status="standby", payload_kg=0
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}

# To  Remove PX4_002 using pop (print before removing)
removed_drone = fleet.pop("PX4_002")
print("Removed drone PX4_002:", removed_drone)

# Print active drones and battery levels
print("\nActive drones:")
for drone_id, details in fleet.items():
    if details["status"] == "active":
        print(drone_id, "Battery:", details["battery"])

# To Find lowest battery among drones in air (altitude > 0)
in_air_drones = {k: v for k, v in fleet.items() if v["altitude"] > 0}

lowest_battery_drone = min(in_air_drones, key=lambda x: in_air_drones[x]["battery"])
print("\nLowest battery in air:", lowest_battery_drone, in_air_drones[lowest_battery_drone])

# To Update drones with battery < 30
for drone_id, details in fleet.items():
    if details["battery"] < 30:
        details["status"] = "critical_low_battery"

#To Prints a final formatted fleet summary
print("\nFinal Fleet Summary:")
for drone_id, details in fleet.items():
    print(f"{drone_id}: {details}")