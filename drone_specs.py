max_takeoff_weight = 4.5    # kg, float 
frame_weight = 1.2           # kg, float 
battery_weight = 0.8         # kg, float 
num_propellers = 4         # int 
motor_weight = 0.075         # kg per motor, float 
is_gps_enabled = True        # bool 
gps_module_weight = 0.05    # kg, float 

#To calculate the maximum payload
total_drone_weight = frame_weight + battery_weight + (num_propellers * motor_weight) 
if is_gps_enabled:
    total_drone_weight=total_drone_weight+gps_module_weight

maximum_payload=max_takeoff_weight-total_drone_weight

print(f"The maximum payload is: {maximum_payload} kg",)

#To print the type of each variable
print(type(max_takeoff_weight))
print(type(frame_weight))
print(type(battery_weight))
print(type(num_propellers))
print(type(motor_weight))
print(type(is_gps_enabled))
print(type(gps_module_weight))
print(type(maximum_payload))

#To check whether payload is enough to carry a 1.8 kg camera (print a bool) 
camera=1.8 #kg
print(maximum_payload>=camera)

#To converts max_takeoff_weight to grams and stores it as an int
max_takeoff_weight_g = int(max_takeoff_weight * 1000)

print("Maximum takeoff weight in grams:", max_takeoff_weight_g)
