# Defining a class (Blue print)
class Rocket():
    
    # Initialization of the class attributes - Initial coordinates
    def __init__(self,x= 0,y= 0,z= 0) :
        self.x = x
        self.y = y
        self.z = z
        

    # To displace the initial coordinates by 0 unit default
    def move (self, x_inc= 0, y_inc = 0, z_inc = 0):
        self.x += x_inc
        self.y += y_inc
        self.z += z_inc


        
VSK_rocket = Rocket(0,0,0)

# Type of VSK_rocket
print(type(VSK_rocket))

# Printing the starting coordinates of VSK_rocket
print(f"The initial x coordinate of the rocket is {VSK_rocket.x} ")
print(f"The initial y coordinate of the rocket is {VSK_rocket.y} ")
print(f"The initial z coordinate of the rocket is {VSK_rocket.z} ")

# Move the initial coordinates of VSK_rocket as you like 
VSK_rocket.move(1,3,4)

# Printing the updated coordinates of VSK_rocket
print(f"The updated x coordinate of the rocket is {VSK_rocket.x} ")
print(f"The updated y coordinate of the rocket is {VSK_rocket.y} ")
print(f"The updated z coordinate of the rocket is {VSK_rocket.z} ")

# Build new rockets ; alter their positions and print the answers

rkt_num = int(input("Enter the number of rockets you want to build (1 to 5): "))

while rkt_num > 5:
    print("Please enter a number between 1 and 5")
    rkt_num = int(input("Enter the number of rockets you want to build (1 to 5): "))
    

rkt_name = [];  # To store the rocket name 
rkt_obj = [];  # To store the rocket object

for i in range(1,rkt_num+1,1):
    
    # User input for the rocket name and their inital coordinate
    user_rkt_name = input(f'Enter the name for rocket {i}: ')
    user_rkt_coodx = int(input(f'Enter the initial x coordinate of rocket {user_rkt_name}: '))
    user_rkt_coody = int(input(f'Enter the initial y coordinate of rocket {user_rkt_name}: '))
    user_rkt_coodz = int(input(f'Enter the initial z coordinate of rocket {user_rkt_name}: '))
    
    # Creating a temporary object with the new rocket details
    rocket  = Rocket(user_rkt_coodx, user_rkt_coody, user_rkt_coodz)
    
    # Asking the user if they wish to move the rocket in [x,y,z] coordinates
    user_rkt_wish = input(f'Do you want to move rocket {user_rkt_name} to a new position? [y/n]: ')
    
    while user_rkt_wish != 'y' and  user_rkt_wish != 'Y' and  user_rkt_wish != 'n' and  user_rkt_wish != 'N':
        print("The input must be either y or n (not case sensitive)") 
        user_rkt_wish = input(f'Do you want to move rocket {user_rkt_name} to a new position? [y/n]: ')
        
   
    if user_rkt_wish == 'y' or user_rkt_wish == 'Y':
        user_rkt_xinc = int(input(f'Please input the x coordinate increment you wish to have: '))
        user_rkt_yinc = int(input(f'Please input the y coordinate increment you wish to have: '))
        user_rkt_zinc = int(input(f'Please input the z coordinate increment you wish to have: '))
        
        # Updating the position of x y z coordinate
        rocket.move(user_rkt_xinc,user_rkt_yinc,user_rkt_zinc)
        
    rkt_obj.append(rocket)                         # Appending the rocket object
    rkt_name.append(user_rkt_name)                 # Appending the rocket name 
    

# Print the rocket names and their objects
print("THE ROCKETS AND THEIR COORDINATES ARE CREATED AND STORED IN RESPECTIVE OBJECTS")

for name, rocket in zip(rkt_name, rkt_obj):
    print(f"Rocket name: {name}, Coordinates: ({rocket.x}, {rocket.y}, {rocket.z})")
    
# Calculate the distance between a rocket and all other rockets 
rkt_choice = input(""" Enter the name of the rocket for which you wish to calculate the relative distance of other rockets : """ )

# Function to calculate the relative distance
def calc_dist(obj,rem_obj,obj_name,rem_name):
    for other_obj,other_name in zip (rem_obj,rem_name):
        x_dist = obj.x - other_obj.x
        y_dist = obj.y - other_obj.y
        z_dist = obj.z - other_obj.z
        
        rel_dist = (x_dist**2 + y_dist**2 + z_dist**2)**0.5
        print(f"The relative distance between rocket {obj_name} and rocket {other_name} is {rel_dist} units")
        

def segregate_rocket(rkt_name,rkt_obj,rkt_choice):
     
    # Preallocation for appending the remaining rocket name and object 
     rem_name = []
     rem_obj = []
     obj = None
     obj_name = None 
     check = 0;
     for name, rocket_obj in zip(rkt_name, rkt_obj) :
         if name == rkt_choice:
             obj = rocket_obj
             obj_name = rkt_choice
             check += 1
         else:
             rem_name.append(name)
             rem_obj.append(rocket_obj)
             
     return check, obj, obj_name, rem_obj, rem_name 

# Calling the segregate rocket function 
check, obj, obj_name, rem_obj, rem_name = segregate_rocket(rkt_name,rkt_obj,rkt_choice)

while check == 0:
    print("These are the existing rocket names:")
    
    for name in rkt_name:
        print(name)
    rkt_choice = input(""" Enter the correct name of the rocket for which you wish to calculate the relative distance of other rockets : """)
    check, obj, obj_name, rem_obj, rem_name = segregate_rocket(rkt_name,rkt_obj,rkt_choice)
    
    
            
# Calling the function to calculate the relative distance 
calc_dist(obj,rem_obj,obj_name,rem_name)
        
        
        
        