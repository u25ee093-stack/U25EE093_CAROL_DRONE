body_weight=float(input("Enter body weight in g: "))    #taking body weight input
payload_weight=float(input("Enter payload weight in g: "))  #taking payload wight input 

total_weight=(body_weight+payload_weight)/1000   #to calculate total weight in kgs

print(f"The total weight in kg is {total_weight} kg: ",) #to display total weight

#to check if total weight is greater than 2kg
if total_weight>2:                            
    print("Total weight is greater than 2 kg")
else:
    print("The total weight is lesser than 2kg")

