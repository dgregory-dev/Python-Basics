# Create variables to be input by the user
name = input("Please type your full name: ")
age = input("Please type your age: ")
city = input("Please type your city of residence: ")
hobby = input("Please type in your hobby: ")

# Calculate the width for centering (use the maximum line length + some padding)
width = max(len(line) for line in [
    "******************************************",
    "*          Personal Information          *",
    name, age, city, hobby
]) + 4  # Add 4 for some extra padding

# Output the details that have been added from above
print("*" * width)
print("*          Personal Information          *".center(width))
print("*" * width)
print(name.title().center(width))
print(age.center(width))
print(city.title().center(width))
print(hobby.title().center(width))
print("*" * width)