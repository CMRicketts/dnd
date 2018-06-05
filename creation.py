#!/usr/bin/env python
# -*- coding: utf-8 -*-

from supplemental.character import Character

def main():
    while True:
        command = raw_input("what do you want to do? 'create' character, 'view', 'help', or 'exit'? \n")
        if command == "create":
            print("creation of character")
            chr = Character()
            lvl = raw_input("what level is your character? ")
            chr.level = lvl
            chr.set_race()
            chr.set_class()

            chr.armor = "Leather Armor"

            print(chr.to_string())

        elif command == "help":
            print("Type in: "
                  "\ncreate: \tcreate a new character"
                  "\nview: \t\tview created characters"
                  "\nhelp: \t\tdisplay this menu"
                  "\nexit: \t\texit the program")

        elif command == "view":
            print("viewing all characters")

        elif command == "exit":
            print("thank you!")
            break

        else:
            print(command + " is not recognized as a command. please try again!")


if __name__ == '__main__':
    main()
