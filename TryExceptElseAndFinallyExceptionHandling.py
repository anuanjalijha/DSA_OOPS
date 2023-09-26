def divide(x,y):
    try:
        result = x//y 
        
    except ZeroDivisionError:
        print("sorry! you are dividing by zero")
        
    else:
        print("yeah! your answer is :", result)
        
    finally:
        print("this is always executed")
        
divide(3,2)
print()
divide(3,0)