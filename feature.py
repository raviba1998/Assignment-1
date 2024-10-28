def multiply_numbers(num1, num2):
    return num1 * num2

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the multiplication program!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    result = multiply_numbers(num1, num2)
    print(f"The result of multiplying {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
