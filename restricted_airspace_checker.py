planned_zones   = {"Z1", "Z2", "Z3", "Z5", "Z7"} 
restricted_zones = {"Z3", "Z5", "Z6", "Z8"} 
cleared_zones   = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

# Planned zones that are restricted (intersection)
restricted_planned = planned_zones & restricted_zones
print("Restricted planned zones:", restricted_planned)

#Planned but NOT restricted (safe zones)
safe_zones = planned_zones - restricted_zones
print("Safe zones:", safe_zones)

# planned or restricted, but NOT both (symmetric difference)
exclusive_zones = planned_zones ^ restricted_zones
print("Exclusive zones:", exclusive_zones)

#  Check subset
print("Is planned subset of cleared?", planned_zones.issubset(cleared_zones))

# Add and remove zones
planned_zones.add("Z9")
planned_zones.discard("Z7")  # discard avoids error if item not found

print("Updated planned zones:", planned_zones)

#Count unique zones across all three sets
all_unique_zones = planned_zones | restricted_zones | cleared_zones
print("Total unique zones:", len(all_unique_zones))