import os 
import json
import difflib
from this import d
import pyttsx3
from difflib import get_close_matches

engine = pyttsx3.init()
engine.setProperty('rate', 125)

data = json.load(open('D:\projects\data.json'))

c = 'y'

def extract(word):
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("\nDid you mean %s instead ? \n\n Enter 'y' if yes.\n Enter 'n' for no." %get_close_matches(word,data.keys())[0])
        if choice == 'y':
            return data[get_close_matches(word,data.keys())[0]]

        elif choice == 'n':
            print("\nPlease check yor search input. ")
            engine.say("Please check yor search input.")
            engine.runAndWait()
            engine.stop()

        
        else:
            print("\nSorry, unfortunately we don't have the meaning of the word ")
            engine.say("Sorry, unfortunately we don't have the meaning of the word please try again")
            engine.runAndWait()
            engine.stop()

    else:
        print("\nThis word doesn't exist in the dictionary. Please try again")
        engine.say("\nThis word doesn't exist in the dictionary. Please try again")
        engine.runAndWait()
        engine.stop()

while c == 'y':
    to_search = input("Enter the word you want to search ?\n").lower()

    result_str = ""
    result = extract(to_search)
    if result == None:
        c = input("Do you want to continue search for meanings?(y/n)")
        if c == 'y':
            pass
        else:
            exit()
    
    else:
        for i in range(len(result)):
            result_str += result[i]
            result_str += " "
        x = result_str.split(".")
        for i in x:
            print("\n", i)

    engine.say(result_str)
    engine.runAndWait()
    engine.stop()

    c = input("Do you want to continue searching for meanings?(y/n)")
    if c == 'y':
        pass
    
    else:
        exit()

