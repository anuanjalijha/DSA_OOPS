def evaluate_bmi(bmi):
    if 18.5<=bmi<=24.9:
        return 'healthy'
        
    if bmi>=25:
        return 'overweight'
        
    return 'underweight'

def caluculat_bmi(height,weight):
    return weight/height**2 
    
def main():
    try:
        height= float(input("Enter your height(meters):"))
        weight = float(input("Enter your weight(kilograms):"))
        
    except ValueError as error:
        print("Error!please enter a valid number")
        
    else:
        bmi = round(caluculat_bmi(height,weight),1)
        evaluation = evaluate_bmi(bmi)
        
        print(f'your body mas index is {bmi}')
        print(f'this is considered {evaluation}')
        
main()        
        
    