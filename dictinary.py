favorites = {
    "color" : "green",
    "food" : "chicken burger",
    "sport" : "basketball"
}
    
print("Available categories:")
for category in favorites.keys():
    print("-", category)

user_choice = input("Type a category to see my favorite: ")

if user_choice in favorites:
    print(f"My favorite {user_choice} is: {favorites[user_choice]}")
else:
    print("Sorry, that category is not available.")

add_new = input("Would you like to add a new favorite? (yes/no): ")

if add_new.lower() == "yes":
    new_category = input("Enter the new category name: ")
    new_value = input(f"What is your favorite {new_category}?: ")
    favorites[new_category] = new_value
    print(f"Added: {new_category} -> {new_value}")
else:
    print("No new category added.")

print("\nUpdated favorites dictionary:")
for key, value in favorites.items():
    print(f"{key}: {value}")