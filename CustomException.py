class InvalidAgeException(Exception):
    # raised when input value is less than 18 
    pass 

number = 18 

try:
    input_num = int(input("enter a number: "))
    if input_num<number:
        raise InvalidAgeException
    else:
        print("valid for vote")
        
except InvalidAgeException:
    print("Exception occurred:Invalid Age")