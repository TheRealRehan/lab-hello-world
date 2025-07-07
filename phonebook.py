import json
from datetime import datetime


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: contacts.json is not a valid JSON file.")
        exit()
        
def save_contacts(data):
    with open("contacts.json", "w") as file:
        json.dump(data, file, indent=2)

def main():
    contacts = load_contacts()
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()

    new_contact = {
        "name": name,
        "number": number,
        "metadata": {
            "added_by": "user",
            "source": "manual entry",
            "tags": ["personal"],
            "timestamp": datetime.now().isoformat()
        }
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    print("\nCurrent Contacts:")
    print(json.dumps(contacts, indent=2))

if __name__ == "__main__":
    main()
