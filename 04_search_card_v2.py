"""search card v2, adds code used for tesing and shows
values of card when searched
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

# Function to search for a cre
def search_card():
# Asks user what card to search for
    card_name = easygui.enterbox("Enter the card name you want to search for:", "Search")
    if card_name is None:
         return
    if card_name in existing_cards:
                     card_values = existing_cards[card_name]
                     easygui.msgbox("Card: {}\nStrength: {}\nSpeed: {}\nStealth: {}\nCunning: {}".format(card_name,
                                   card_values["Strength"],card_values["Speed"],card_values["Stealth"],
                                   card_values["Cunning"]))
    else:
      easygui.msgbox("Card not found.")
      pass

# Testing
search_card()