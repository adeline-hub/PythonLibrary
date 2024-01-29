#Create a program to find the largest among three numbers.

def find_largest_number(num1, num2, num3):
    # Compare the numbers to find the largest
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest_number = find_largest_number(num1, num2, num3)

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")
