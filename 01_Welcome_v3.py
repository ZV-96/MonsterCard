"""V3 of the welcome screen v2 put in a loop for easier testing"""

import easygui


# Print welcome message
easygui.msgbox("Welcome to Monster Card Catalogue", "WELCOME")

while True:
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