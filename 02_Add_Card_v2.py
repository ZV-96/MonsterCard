"""Version 2 of add card, trialling an
alternate way to ask the user for their card.
Asks the user through multiple enter boxes
rather than one big one, adds value limits"""

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


# Function to add a creature
def add_card():
    # Ask the user for the name of the card they want to add
    card_name = easygui.enterbox("Enter the name of the creature you want to add:", "Add")
    if card_name is None:
        return
    card_values = {"Strength": easygui.integerbox("Enter the strength of the creature:", "Add",
                                                  lowerbound=1, upperbound=25),
                   "Speed": easygui.integerbox("Enter the speed of the creature:", "Add",
                                               lowerbound=1, upperbound=25),
                   "Stealth": easygui.integerbox("Enter the stealth of the creature:", "Add",
                                                 lowerbound=1, upperbound=25),
                   "Cunning": easygui.integerbox("Enter the cunning of the creature:", "Add",
                                                 lowerbound=1, upperbound=25)}
    existing_cards[card_name] = card_values
    easygui.msgbox(f"Great! added {card_name} to the catalogue of Monster Cards!")


add_card()
