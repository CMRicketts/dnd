#!/usr/bin/env python
# -*- coding: utf-8 -*-


from supplemental.character import Character
from supplemental.dictionary import dictionary as search

import random


def roll_stats(chr):
    flag = False
    stats = []
    while flag == False:
        stats = []
        i = 0
        while i < 6:
            d1 = random.randint(1, 7)
            d2 = random.randint(1, 7)
            d3 = random.randint(1, 7)
            d4 = random.randint(1, 7)
            total = d1 + d2 + d3 + d4
            minimum = min(d1, d2, d3, d4)
            if len([minimum]) != 1:
                total -= minimum[0]
            else:
                total -= minimum
            stats.append(total)
            i += 1
        if sum(stats) < 70:
            pass
        else:
            flag = True
    return stats


def main():
    while True:
        command = raw_input("what do you want to do? 'create' character, 'search' for any feature or proficiency, "
                            "'help', or 'exit'? \n")
        command = command.strip()
        if command == "create":
            print("creation of character")
            chr = Character()

            '''name = raw_input("What is the name of your character?")
            chr.name = name
            plr = raw_input("What is your name (the player)")
            chr.player = plr
            sex = raw_input("What is the gender (or sex) of your character?")
            chr.sex = sex'''

            #lvl = raw_input("what level is your character? ")
            #chr.level = lvl

            '''print("\n")
            print("Let's talk about some of your stats.")
            choice = raw_input("Do you want to do a dice 'roll' for your stats, or the standard 'array'?")
            stats = []
            if choice == "roll":
                stats = roll_stats(chr)
            else:
                stats = [15, 14, 13, 12, 10, 8]
            print("6 Stats to assign:")
            i = 0
            while i < 6:
                for stat in stats:
                    print(stat)
                choice = raw_input("which ability do you want to input")
                if choice == "strength":
                    if chr.strength == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            print("stats: " + str(stats) + str(num))
                            stats.remove(int(num))
                            chr.strength = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("strength has already been accounted for")
                elif choice == "dexterity":
                    if chr.dexterity == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            stats.remove(int(num))
                            chr.dexterity = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("dexterity has already been accounted for")
                elif choice == "constitution":
                    if chr.constitution == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            stats.remove(int(num))
                            chr.constitution = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("constitution has already been accounted for")
                elif choice == "wisdom":
                    if chr.wisdom == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            stats.remove(int(num))
                            chr.wisdom = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("wisdom has already been accounted for")
                elif choice == "intelligence":
                    if chr.intelligence == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            stats.remove(int(num))
                            chr.intelligence = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("intelligence has already been accounted for")
                else:
                    if chr.charisma == 0:
                        num = raw_input("what score from the list do you want to assign to this?")
                        if int(num) in stats:
                            stats.remove(int(num))
                            chr.charisma = int(num)
                            i += 1
                        else:
                            print("this number isn't in the stats list")
                    else:
                        print("charisma has already been accounted for")'''

            #chr.set_race()
            #chr.set_class()
            #chr.count_spells()

            '''bg = raw_input("Tell me a bit about your character's personality")
            chr.personality_trait = bg
            ideal = raw_input("What are your character's ideals?")
            chr.ideal = ideal
            flaw = raw_input("What are your character's flaws?")
            chr.flaw = flaw
            bond = raw_input("What are your character's bonds?")
            chr.bond = bond
            agn = raw_input("What is your alignment?")
            chr.alignment = agn'''

            print(chr.to_string())

        elif command == "help":
            print("Type in: "
                  "\ncreate: \tcreate a new character"
                  "\nsearch: \tsearch for any feature, skill, or proficiency."
                  "\nhelp: \t\tdisplay this menu"
                  "\nexit: \t\texit the program")

        elif command == "search":
            flag = True
            while flag:
                print("This will allow you to search for any feature (for now). \n"
                      "Please type in the word or phrase you are searching for.\n"
                      "Type 'exit' to exit searching")
                word = raw_input("What feature are you looking for?\n")
                srch = word.strip().lower()
                if srch == "exit":
                    flag = False
                comp = dict((k.lower(), v.lower()) for k, v in search.iteritems())
                try:
                    result = comp[srch]
                except KeyError:
                    print srch + " was not found"
                else:
                    response = "\n" + srch + ": "
                    line = " "
                    for word in result.split(" "):
                        line = line + word + " "
                        if len(line) > 120:
                            response += "\n" + line
                            line = ""
                    print(response)
                print("\n")

        elif command == "exit":
            print("thank you!")
            break

        else:
            print(command + " is not recognized as a command. please try again!")


if __name__ == '__main__':
    main()
