# Calculate BMI from weight and height

def get_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


weight = 68
height = 1.75
bmi = get_bmi(weight, height)

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))
print("Category:", get_category(bmi))
