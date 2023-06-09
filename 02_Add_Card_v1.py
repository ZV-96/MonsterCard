"""Add card version 1
This code will be using an enterbox with multiple
fields to get the user's monster card"""

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

new_card = {}

# Get the values from the cards

text = "Enter the following values of your card"  # Prompt for user to type
title = "Enter card"  # Title shown

# Fields to fill in
input_list = ["Monster name", "Strength", "Speed", "Stealth", "Cunning"]

# User's inputs are added to a list
values = easygui.multenterbox(text, title, input_list)

# Add the user's card to a new dictionary

new_card[values[0]] = {}  # Adds key with monster name and empty dictionary
new_card[values[0]]["Strength"] = values[1]  # Adds strength
new_card[values[0]]["Speed"] = values[2]  # Adds speed
new_card[values[0]]["Stealth"] = values[3]  # Adds stealth
new_card[values[0]]["Cunning"] = values[4]  # Adds cunning

# Print the card and check with user that it is correct
card = ""
for card_name, card_info in new_card.items():

    for category in card_info:
        card += f"{category}: {card_info[category]}\n"

easygui.buttonbox(f"Is the following card correct?\n\n"
                  f"{card_name}\n\n"
                  f"{card}",
                  choices=["Yes", "No"])
