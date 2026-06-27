# to display main title
print("Drone movement")  
 #to display the options given for drone movement
print("1.Roll")         
print("2.Pitch")
print("3.Yaw")
 
 #to take input from user
choice=int(input("Enter your choice(1-3)"))
if choice==1:              
     #if user selects 1. Roll
    print("Slow down left motors left roll or right motors for right roll ")  #display drones movement during roll
elif choice==2:   
     #if user selects 2.Pitch         
    print("Slow down front motors and speed up back motors for pitch forward ")  #display drone movement during pitch
    print("Slow down back motors and speed up front motors for pitch backward")
    
elif choice ==3:     
     #if user selects 3.Yaw       
    print("CW motors slow down and CCW motors speed up for yaw left")          # CW=clockwise CCW=counter clockwise
    print("CW motors speed up and CCW motors slow down for yaw right")         #dispplay dronw movement during yaw
else:
     #if user did not select 1,2 or 3
    print("Error!") 


