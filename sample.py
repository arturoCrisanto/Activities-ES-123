def calculate_bmi(weight_kg, height_cm):
    bmi = (weight_kg * 10000) / (height_cm ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Test the functions
weight = 45      # in kilograms
height = 153     # in centimeters

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print(f"Your BMI is: {bmi}")
print(f"Health Category: {category}")
