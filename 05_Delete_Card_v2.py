"""Delete Card v2
if the card searched is not in catalogue asks user
to enter again, confirmation text when deleting"""

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


# Function that Deletes Cards
def delete_card():
    while True:
        # asks user what cards name is
        card_name = easygui.enterbox("Enter the name of the creature you want to delete (IN CAPS):",
                                     "Delete")
        if card_name is None:
            return
        # deletes card
        if card_name in existing_cards:
            choice = easygui.ynbox("Are your sure you want to delete this?", "Confirmation",
                                   choices=("Yes","No"))
            if choice:
                del existing_cards[card_name]
                easygui.msgbox("Monster Card deleted.")
                return existing_cards
            else:
                easygui.msgbox("Deletion Cancelled")
                return None
        else:
            easygui.msgbox(f"There is no Monster Card called {card_name} in the catalogue,"
                           f" Please try again")
            return None


# testing
delete_card()
