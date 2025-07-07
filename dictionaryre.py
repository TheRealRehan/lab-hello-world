
def display_favorites(favorites):
    print("\nYour favorite things:")
    if not favorites:
        print("  (No favorites to show.)")
    else:
        for category, value in favorites.items():
            print(f"  {category}: {value}")


def lookup_favorite(favorites):
    category = input("Enter the category you'd like to look up: ")
    if category in favorites:
        print(f"My favorite {category} is: {favorites[category]}")
    else:
        print("Sorry, that category is not available.")


def add_favorite(favorites):
    new_category = input("Enter the new category name: ")
    if new_category in favorites:
        print("That category already exists. Try updating it instead.")
    else:
        new_value = input(f"What is your favorite {new_category}? ")
        favorites[new_category] = new_value
        print(f"Added: {new_category} -> {new_value}")


def update_favorite(favorites):
    category = input("Enter the category you'd like to update: ")
    if category in favorites:
        new_value = input(f"Enter your new favorite {category}: ")
        favorites[category] = new_value
        print(f"Updated: {category} -> {new_value}")
    else:
        print("That category doesn't exist yet. Try adding it.")

def delete_favorite(favorites):
    category = input("Enter the category you'd like to delete: ")
    if category in favorites:
        del favorites[category]
        print(f"Deleted: {category}")
    else:
        print("That category doesn't exist.")


def main():
    favorites = {
        "color": "blue",
        "food": "sushi",
        "movie": "Inception"
    }

    while True:
        print("\nWhat would you like to do?")
        print("1. Display all favorites")
        print("2. Look up a favorite")
        print("3. Add a new favorite")
        print("4. Update an existing favorite")
        print("5. Delete a favorite")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            display_favorites(favorites)
        elif choice == "2":
            lookup_favorite(favorites)
        elif choice == "3":
            add_favorite(favorites)
        elif choice == "4":
            update_favorite(favorites)
        elif choice == "5":
            delete_favorite(favorites)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




