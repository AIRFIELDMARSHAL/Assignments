import math
def get_valid_number():
    while True:
        try:
            num = float(input("Enter a positive number: "))
            if num <= 0:
                print("Error: Please enter a number greater than 0 (required for sqrt and log).")
                continue
            return num
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
num = get_valid_number()
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)
print(f"Square root: {square_root}")
print(f"Logarithm: {natural_log}")
print(f"Sine: {sine_value}")