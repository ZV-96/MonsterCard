"""Version 3 of add card,
adding ability to edit card and a preview
of said card"""

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
    card_values = {}
    card_values["Strength"] = easygui.integerbox("Enter the strength of the creature:", "Add",
                                                 lowerbound=1, upperbound=25)
    card_values["Speed"] = easygui.integerbox("Enter the speed of the creature:", "Add",
                                              lowerbound=1, upperbound=25)
    card_values["Stealth"] = easygui.integerbox("Enter the stealth of the creature:", "Add",
                                                lowerbound=1, upperbound=25)
    card_values["Cunning"] = easygui.integerbox("Enter the cunning of the creature:", "Add",
                                                lowerbound=1, upperbound=25)
    existing_cards[card_name] = card_values

    # Display the newly added Card
    message = f"The following Monster Card has been added:" \
              f"\n\nName: {card_name}\nStrength: {card_values['Strength']}\nSpeed:" \
              f" {card_values['Speed']}\nStealth: {card_values['Stealth']}\nCunning:" \
              f" {card_values['Cunning']}"
    while True:
        choice = easygui.ynbox(f"{message}\n\nAre these values correct?", "Confirm Details")
        if choice:
            break
        else:
            field = easygui.buttonbox("Which field would you like to change?", "Edit Field",
                                      choices=["Strength", "Speed", "Stealth", "Cunning"])
            new_value = easygui.integerbox(f"Enter the new value for {field}:"
                                           f"", "Edit Field", lowerbound=1, upperbound=25)
            card_values[field] = new_value
            message = f"The following Monster Card has been updated:" \
                      f"\n\nName: {card_name}\nStrength: {card_values['Strength']}\nSpeed:" \
                      f" {card_values['Speed']}\nStealth: {card_values['Stealth']}\nCunning:" \
                      f" {card_values['Cunning']}"
    return


add_card()
