"""V4 of the welcome screen
put v3 into a function for ease of use"""


import easygui


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


# Main code
home_screen()
