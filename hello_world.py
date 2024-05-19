print ("Hello World")

# TO COMMENT MULTIPLE LINES IN ONE GO - CTRL + /
# this is my first comment 
# this is my second comment 

# Variables 
x = 3 
y = 5
z = x+y

print(z)

z = 9 
print(z)

# STRINGS
person_name = "DEEPIKA"
person_status = """Soon to get a the job she loves and gonna be filthy rich"""
person_confidence = 1000000000000000000000000000000000000000000000000000.00000
print(person_name)
print(person_status)
print(person_confidence)



# To orint the type of the variable 
print(type(person_name))
print(type(person_status))
print(type(person_confidence))


# f-Strings or Format string 
str1 = "Deepika is gonna get a job soon "
str2 = """ Soon she will receive an interview. 
           She is gonna be amazing in the interview"""

print(str1 + str2)
print(f'{str1} {str2}')

salary = 3000;
print(f' Deepika is gonna get {salary} euros as her starting pay')


# User input 
user_name = input("Enter your name: ")
user_salary = input("Enter your salary expectations: ")

print(type(user_name))
print(type(user_salary))  # Note: Input stopres the values as strings only

# Datatype conversion 
str2int = int(user_salary)  # String to Integer
print(str2int)
print(type(str2int))

str2float = float(user_salary) # String to float
print(str2float)
print(type(str2float))

int2str = str(str2int) # Integer to string
print(int2str)
print(type(int2str))

float2str= str(str2float) # Float to string 
print(float2str)
print(type(float2str))

# Convert user inputs to specific data types for operations 
num1 = int(input('Enter an integer number: '))
num2 = float(input ('Enter an floating point numnber: '))
print(f'The addition of number 1 and number 2 is {num1+num2}')


# While loop 
ctrl = 0

while ctrl < 100 :
   print(f'Loop number: {ctrl+1}')
   ctrl += 1
   if ctrl == 9 :
      print("One more to go..")
   elif ctrl == 8:
      print("Two more to go....")


# For loop 
p = 0;
for i in range(0,10,2) :
      p += 1
      print(f'For loop iteration:{p}')
      print(f'The value of i is: {i+2}\n')
    
      




   

  