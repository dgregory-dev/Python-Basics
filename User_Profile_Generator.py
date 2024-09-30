def get_article(word):
    return 'an' if word.lower()[0] in 'aeiou' else 'a'

def title_case(s):
    return ' '.join(word.capitalize() for word in s.split())

# Input collection with proper capitalization
first_name = title_case(input("Enter your first name: "))
last_name = title_case(input("Enter your last name: "))
age = input("Enter your age: ")
city = title_case(input("Enter your city: "))
occupation = title_case(input("Enter your occupation: "))

# Concatenate first name and last name
full_name = f"{first_name} {last_name}"

# Create profile description using string formatting
profile_desc = f"{full_name} is {age} years old, lives in {city}, and works as {get_article(occupation)} {occupation}."

# Add escape characters to include quotation marks and a new line
profile_info = "\"Profile Information:\"\n" + profile_desc

# Use string methods to modify the full name
modified_name = full_name.upper()

# Display the user profile
width = max(len(line) for line in [
    "===== User Profile =====",
    modified_name,
    "\"Profile Information:\"",
    profile_desc,
    "=" * 25
]) + 4  # Add 4 for some extra padding

# Output the details
print("=" * width)
print("User Profile".center(width))
print("=" * width)
print(modified_name.center(width))
print(profile_info.center(width))
print("=" * width)