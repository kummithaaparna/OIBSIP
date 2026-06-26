print("=== BMI Calculator ===")

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than 0.")
    else:
        bmi = weight / (height * height)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal Weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values.")