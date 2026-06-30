altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0]

# To  find  maximum altitude and the second it occurred
max_altitude = max(altitudes) #we use this to get maximum
second = altitudes.index(max_altitude) # to find in index at which second it occur in altitude list

print("Maximum altitude:", max_altitude)
print("Occurred at second:", second)

# To calculates the average altitude (round to 2 decimal places) 
average = round(sum(altitudes) / len(altitudes), 2)
print("Average altitude:", average)

# To Create climb_rates list where each element = altitudes[i+1] - altitudes[i] 
climb_rates = []

for i in range(len(altitudes) - 1):
    climb = altitudes[i + 1] - altitudes[i]
    climb_rates.append(climb)

print("Climb rates:", climb_rates)

#To find the steepest climb and steepest descent
steepest_climb = max(climb_rates)
steepest_descent = min(climb_rates)

print("Steepest climb:", steepest_climb)
print("Steepest descent:", steepest_descent)

# To Remove all zero-altitude entries
new_path = []  #creating a new list to add all zero altitude entries

for altitude in altitudes:
    if altitude != 0:
        new_path.append(altitude)

print("Trimmed path:", new_path)