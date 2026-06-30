telemetry = "DRONE_ID:PX4_001|ALT:120.5m|SPEED:18.3kmph|BATT:67%|STATUS:HOVERING|GPS:23.0225N,72.5714E"

drone_parts = telemetry.split("|")
#we use split("|") to make sure it splits at |
#we use [1] so that it will select the second word as list starts from 0
#we use the replace to remove m,kmph,% so that it can be converted into float and int properly
drone_id = drone_parts[0].split(":")[1]
altitude = float(drone_parts[1].split(":")[1].replace("m", ""))
speed = float(drone_parts[2].split(":")[1].replace("kmph", ""))
battery = int(drone_parts[3].split(":")[1].replace("%", ""))
status = drone_parts[4].split(":")[1]
gps = drone_parts[5].split(":")[1]

#   To check for HOVER and to make it case insesitive we use lower as it will convert all letters to lowercase.
print("hover" in status.lower())  

# To  replace HOVERING with RETURNING_HOME
telemetry = telemetry.replace("HOVERING", "RETURNING_HOME")
print(telemetry)

# To print a formatted summary using f-strings: 
print(f"[{drone_id}] Alt: {altitude}m | Batt: {battery}% | Coords: {gps}")