# TASK 01

# Ask the user for their full name
name = input("Enter your full name: ")

# Ask for favorite color
color = input("Enter your favorite color: ")

# Ask for birth year and convert it into integer
birth_year = int(input("Enter your birth year: "))

# Current year (given in question)
current_year = 2026

# Calculate age
age = current_year - birth_year

# Print messages using f-strings
print(f"\nWelcome, {name}!")
print(f"Your favorite color is {color} – perfect for calm AI thinking.")
print(f"You were born in {birth_year} → you are currently {age} years old (2026).")

# Comments:
# 1. input() is used to take data from the user.
# 2. birth_year is converted to integer using int() so we can calculate age.
# 3. current_year is fixed because the lab specifies 2026.
# 4. age is calculated by subtracting birth year from current year.
# 5. f-strings are used to format output neatly.


# TASK 02

# Take two numbers from the user and convert them to float
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user for the operation
operator = input("Enter operation (+, -, *, /, **, %): ")

# Check if the operator is valid
if operator not in ["+", "-", "*", "/", "**", "%"]:
    print("Invalid operator!")

else:
    # Check division by zero
    if operator == "/" and num2 == 0:
        print("Cannot divide by zero!")

    else:
        # Perform calculations
        if operator == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif operator == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif operator == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif operator == "/":
            result = num1 / num2
            print(f"{num1} / {num2} = {result:.2f}")

        elif operator == "**":
            result = num1 ** num2
            print(f"{num1} ** {num2} = {result:.2f}")

        elif operator == "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")


# TASK 03
# Challenge A – Even/Odd & Multiple Checker

start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

i = start

# Using while loop to go through the range
while i <= end:

    # Skip numbers divisible by 7
    if i % 7 == 0:
        i += 1
        continue

    # Check conditions
    if i % 2 == 0 and i % 5 == 0:
        print(f"{i} → Even & Multiple of 5!!")

    elif i % 2 == 0:
        print(f"{i} → Even")

    elif i % 5 == 0:
        print(f"{i} → Multiple of 5!")

    else:
        print(i)

    i += 1


# TASK 03
# Challenge B – Password Strength Checker

password = input("\nEnter a password: ")

# Check length first
if len(password) < 6:
    print("Too short!")

else:
    # Check if password contains a digit
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True

    # Check if password contains uppercase letter
    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True

    # Conditions
    if not has_digit:
        print("Add at least one number")

    elif not has_upper:
        print("Add at least one capital letter")

    else:
        print("Strong password – good choice!")