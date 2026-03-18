# Task 1
def welcome_message():
    print("Welcome to Python Programming Lab")

welcome_message()


# Task 2
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("The sum is:", result)


# Task 3
def functionB():
    print("Inside Function B")

def functionA():
    print("Inside Function A")
    functionB()

functionA()


# Task 4
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Waris Ali Khan")


# Task 5
x = 10  

def show_variables():
    print("Inside function, x =", x)
    y = 20
    print("Inside function, y =", y)

show_variables()

print("Outside function, x =", x)



# Task 6
def total_numbers(*numbers):
    return sum(numbers)

print("Total =", total_numbers(2, 3, 4, 5))


# Task 7
def student_info(**data):
    print("Student Information:")
    for key, value in data.items():
        print(f"{key}: {value}")

student_info(name="Waris Ali Khan", age=10, grade="A")


# Task 8
square = lambda x: x ** 2
print("Square of 10:", square(10))


# Task 9
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


# Task 10
marks = [45, 67, 82, 30, 90, 55]
above_50 = list(filter(lambda x: x > 50, marks))
print("Marks above 50:", above_50)