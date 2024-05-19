# Function definition using "def"
def message() :
    print("I love you Appa")


# Calling the function 
message()

# Function to print a message
def print_input_message(ip_msg):
    print(f'Input message is : {ip_msg}')

# Calling the function 
user_msg = input("Enter the message to be printed: ")
print_input_message(ip_msg = user_msg)


# Function to do elementry mathematical operations

def elementry_math(n1,n2,operation):
    if operation.lower() == 'add' or operation.upper() == 'ADD' or operation.title() == 'Add':
        return n1+n2
    elif operation.lower() == 'subtract' or operation.upper() == 'SUBTRACT' or operation.title() == 'Subtract':
        return n1 - n2
    elif operation.lower() == 'multiply' or operation.upper() == 'MULTIPLY' or operation.title() == 'Multiply':
        return n1*n2
    elif operation.lower() == 'divide' or operation.upper() == 'DIVIDE' or operation.title() == 'Divide':
        return n1/n2 
    else :
        print(" Operation should be either: add, subtract, multiply or divide")

result = elementry_math(20,30,'subtract')
print(result)