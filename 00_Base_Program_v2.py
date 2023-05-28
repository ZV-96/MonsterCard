"""Base Program v2
adding search card function, and re organising
"""

import easygui

# Stores cards in a dictionary
existing_cards = {"STONELING":
                  {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
                  "VEXSCREAM":
                  {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
                  "DAWNMIRAGE":
                  {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
                  "BLAZEGOLELM":
                  {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
                  "WEBSNAKE":
                  {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
                  "MOLDVINE":
                  {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
                  "VORTEXWING":
                  {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
                  "ROTTHING":
                  {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
                  "FROSTSTEP":
                  {"Strength": 14, "Speed": 14, "Stealth": 7, "Cunning": 4},
                  "WHISPGOUL":
                  {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
                  }


# Home screen function - acts as a main menu
def home_screen():

    # Print welcome message
    easygui.msgbox("Welcome to Monster Card Catalogue", "WELCOME")

    choice = easygui.buttonbox("Please pick an option.\n", "Options",
                               choices=["Add card","Search card",
                                        "Delete card","Output Catalogue",
                                        "Exit"])

    # Testing code to make sure it all works as expected
    if choice == "Add card":
        print("Add card")

    elif choice == "Delete card":
        print("Delete card")

    elif choice == "Search card":
        print("Search card")

    elif choice == "Output Catalogue":
        print("Output Catalogue")

    elif choice == "Exit":
        print("Exit")


# Function to find a Card
def search_card():
    card_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")

    if card_name is None:
        return

    # capitalize the first letter of the input
    card_name = card_name.upper()

    # check if the card exists
    if card_name in existing_cards:
        card_values = existing_cards[card_name]

        message = f"Creature: {card_name}\nStrength: {card_values['Strength']}\nSpeed: {card_values['Speed']}" \
                  f"\nStealth: {card_values['Stealth']}\nCunning: {card_values['Cunning']}"

        while True:
            choice = easygui.buttonbox(f"{message}\n\nWhat would you like to do?", "Card Details",
                                       choices=["Return to Homescreen", "Edit Card Values, Search for a Card"])

            if choice == "Return to Homescreen":
                home_screen()  # Return to homescreen

            elif choice == "Edit Card Values":
                field = easygui.buttonbox("Which value would you like to edit?", "Edit Card Value",
                                          choices=["Strength", "Speed", "Stealth", "Cunning"])
                new_value = easygui.integerbox(f"Enter the new value for {field}:", "Edit Card Value",
                                               lowerbound=1, upperbound=25)
                card_values[field] = new_value
                message = f"Card: {card_name}\nStrength: {card_values['Strength']}\nSpeed: {card_values['Speed']}" \
                          f"\nStealth: {card_values['Stealth']}\nCunning: {card_values['Cunning']}"
                easygui.msgbox("Card Value updated!")

            elif choice == "Search for a Card":
                break  # repeats code to search for new card

    else:
        easygui.msgbox("Card not found.")


# Add Card function

# Delete Card Function

# Output Full Catalogue Function
def output(cards):

    catalogue = ""

    # Loop to print full catalogue
    for monster_name, monster_info in cards.items():

        # Print the card name
        catalogue += f"\n{monster_name}\n"

        # Print the card values
        for key, value in monster_info.items():
            catalogue += f"{key}: {value} \n"

    # Output the full menu
    print(f"**** Below is the full catalogue ****\n"
          f"{catalogue}\n\n")


# Main Routine
home_screen()
