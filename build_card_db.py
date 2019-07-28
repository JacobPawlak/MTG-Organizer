#author: jacob pawlak
#date: July 28th, 2019
#file: build_card_db.py
#goooo blue team!

######################### IMPORTS #########################

#importing json for file output
import json
#importing pandas for csv output
#import pandas
#importing os and glob to look for the json file working as a db
import os
import glob

######################### GLOBALS #########################


######################### HELPERS #########################

#this is a helper function to print different menues (they get passed in as a string variable) and then return the user's menu option
def print_menu_get_choice(menu_to_show):

    #init a string for the user's option
    choice = ""
    #check which menu we were passed in, and then print the corresponding menu
    #for main menu, options are [add, view, remove]
    if(menu_to_show == 'main-menu'):
        valid_opts = ['1','2','3']
        print()
        print("===== Main Menu =====")
        print("(1) Add new cards")
        print("(2) View current DB")
        print("(3) Remove cards from DB")
        print()

        #just to keep from wasting someone's time, you have 10 tries to pick one of the menu items
        failed_attempts = 0
        #get their choice
        choice = input("Please choose an item from the menu: ")
        #if it is not in the list of valid options, shame on it, try again
        while choice not in valid_opts:
            failed_attempts += 1
            #if they reach 10 failed attempts, break the loop
            if(failed_attempts >= 10):
                print("You have entered too many incorrect options, exiting")
                choice = ''
                break
            print("That choice is not on the menu, please try again")
            choice = input("Please choose an item from the menu: ")

    #return the choice (or an empty string if they failed 10 times)
    return choice
    

def add_new_cards(card_list):

    updated_card_list = card_list
    card_names = []
    for card in updated_card_list:
        card_names.append(card['card_name'])
    print("You will now begin to add cards to your DB. Please fill in the fields for each card")
    print("Note: for converted mana cost, use the following formula: {# of uncolored}{for every: black 'B', blue 'U', white 'W', red 'R', green 'G'}")
    print("\tExample: '3B' for 3 uncolored mana and 1 black mana, '2GG' for 2 uncolored mana and 2 green mana, 'RRR' for 3 red mana, etc.")
    print("At any time to quit, just enter 'quit'.")
    print()

    print(updated_card_list)

    user_entry = input("Name of the card: ")

    while user_entry is not "quit":
        new_card = {}
        new_card['card_name'] = user_entry
        user_entry = input("Converted Mana Cost: ")
        new_card['converted_mana_cost'] = user_entry
        user_entry = input("Card type (ex. 'Creature - Human Cleric', 'Sorcery', 'Enchantment - Aura'): ")
        new_card['card_type'] = user_entry
        user_entry = input("Power (if applicable, '*' for special creatures, leave empty for non-creatures)")
        new_card['power'] = user_entry
        user_entry = input("Toughness (if applicable, '*' for special creatures, leave empty for non-creatures)")
        new_card['toughness'] = user_entry
        user_entry = input("Rarity of card ('common', 'uncommon', 'rare', 'mythic'): ")
        new_card['rarity'] = user_entry
        print()
        print("Adding card to DB.")
        print()
        


    return updated_card_list

######################### MAIN () #########################

def main():

    print("Starting the build_card_db.py program...")
    print()

    #set up a dictionary for output, and a list to hold card objects (to be inserted as a dictionary item 'cards' in DB_DICT)
    DB_DICT = {}
    my_mtg_db_list = []
    
    file_list = glob.glob('./*.json')
    if("./mtg_card_db.json" in file_list):
        with open('mtg_card_db.json', 'r') as db_file:
            for line in db_file:
                my_mtg_db_list.append(line)

    print("To begin, please select one of the menu items listed below.")
    user_choice = print_menu_get_choice('main-menu')

    if(user_choice == ''):
        print("You did not pick a menu option, terminating program")
        return
    elif(user_choice == "1"):
        print()
        print("=== Add new cards ===")

        my_mtg_db_list = add_new_cards(my_mtg_db_list)

    elif(user_choice == "2"):
        print()
        print("=== View current DB ===")
    elif(user_choice == "3"):
        print()
        print("=== Remove cards from DB ===")

main()