"""V1 of Base program
putting all the functions together"""


import easygui


# Functions
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


# Function to output the full catalogue
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

# Stores monster cards in a nested dictionary
exist_cards = {"STONELING":
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

output(exist_cards)
