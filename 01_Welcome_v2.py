"""V2 of the welcome screen trailling using easyGUI"""

import easygui


# Print welcome message
easygui.msgbox("Welcome to Monster Card Catalogue", "WELCOME")

# Ask user to make a choice
choice = easygui.buttonbox("Please pick an option.\n", "Options",
                           choices=["Add card","Search card",
                                    "Delete card","Output Catalogue",
                                    "Exit"])

# Testing the code to make sure it corresponds to the correct option
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