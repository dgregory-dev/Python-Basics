# Prompt the user for movie preferences
action = input("Do you like action movies? (yes/no): ").lower() == "yes"
comedy = input("Do you like comedy movies? (yes/no): ").lower() == "yes"
drama = input("Do you like drama movies? (yes/no): ").lower() == "yes"
scifi = input("Do you like science fiction movies? (yes/no): ").lower() == "yes"
horror = input("Do you like horror movies? (yes/no): ").lower() == "yes"
romance = input("Do you like romance movies? (yes/no): ").lower() == "yes"

# Combine booleans using logical operators
if action and comedy and not drama and not scifi and not horror and not romance:
    genre = "Action-Comedy"
elif action and drama and not comedy and not scifi and not horror and not romance:
    genre = "Action-Drama"
elif comedy and drama and not action and not scifi and not horror and not romance:
    genre = "Comedy-Drama"
elif action and scifi and not comedy and not drama and not horror and not romance:
    genre = "Action-Sci-Fi"
elif horror and comedy and not action and not drama and not scifi and not romance:
    genre = "Horror-Comedy"
elif romance and comedy and not action and not drama and not scifi and not horror:
    genre = "Romantic-Comedy"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif drama:
    genre = "Drama"
elif scifi:
    genre = "Science Fiction"
elif horror:
    genre = "Horror"
elif romance:
    genre = "Romance"
else:
    genre = "Unknown"

# Recommend movies based on the genre using conditional statements
if genre == "Action-Comedy":
    print("Recommended movies: 'Rush Hour', 'Bad Boys', 'The Nice Guys'")
elif genre == "Action-Drama":
    print("Recommended movies: 'The Dark Knight', 'Inception', 'John Wick'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'The Big Sick', 'Little Miss Sunshine', 'The Intouchables'")
elif genre == "Action-Sci-Fi":
    print("Recommended movies: 'The Terminator', 'Edge of Tomorrow', 'Minority Report'")
elif genre == "Horror-Comedy":
    print("Recommended movies: 'Shaun of the Dead', 'Zombieland', 'The Cabin in the Woods'")
elif genre == "Romantic-Comedy":
    print("Recommended movies: 'When Harry Met Sally', '(500) Days of Summer', 'Crazy Rich Asians'")
elif genre == "Action":
    print("Recommended movies: 'Die Hard', 'The Matrix', 'Mission: Impossible'")
elif genre == "Comedy":
    print("Recommended movies: 'The Hangover', 'Superbad', 'Bridesmaids'")
elif genre == "Drama":
    print("Recommended movies: 'The Shawshank Redemption', 'Forrest Gump', 'The Green Mile'")
elif genre == "Science Fiction":
    print("Recommended movies: 'Blade Runner', 'Interstellar', 'Arrival'")
elif genre == "Horror":
    print("Recommended movies: 'The Exorcist', 'Get Out', 'A Quiet Place'")
elif genre == "Romance":
    print("Recommended movies: 'The Notebook', 'Pride and Prejudice', 'Before Sunrise'")
else:
    print("Sorry, we couldn't determine your movie preferences.")