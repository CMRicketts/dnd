import math


class Half_Elf:
    def __init__(self, level):
        self.charisma = 2
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.wisdom = 0
        self.constitution = 0

        ability1 = raw_input("what ability score do you want to increase?")
        if ability1 == "strength":
            self.strength = self.strength + 1
        if ability1 == "dexterity":
            self.dexterity = self.strength + 1
        if ability1 == "intelligence":
            self.intelligence = self.intelligence + 1
        if ability1 == "wisdom":
            self.wisdom = self.wisdom + 1
        if ability1 == "charisma":
            self.charisma = self.charisma + 1
        if ability1 == "constitution":
            self.constitution = self.constitution + 1
        ability2 = raw_input("what other ability score do you want to increase?")
        if ability2 == "strength":
            self.strength = self.strength + 1
        if ability2 == "dexterity":
            self.dexterity = self.strength + 1
        if ability2 == "intelligence":
            self.intelligence = self.intelligence + 1
        if ability2 == "wisdom":
            self.wisdom = self.wisdom + 1
        if ability2 == "charisma":
            self.charisma = self.charisma + 1
        if ability2 == "constitution":
            self.constitution = self.constitution + 1

        self.age_low = 17
        self.age_high = 175
        self.weight_low = 100
        self.weight_high = 140
        self.height_low = 55
        self.height_high = 75
        self.speed = 30
        self.size = "medium"
        self.swim_speed = 0
        self.proficiency = ["darkvision"]
        self.advantage = ["charm", "magic sleep"]

        language = raw_input("what language do you want to add? ")

        self.language = ["common", "elvish", language]
        self.magic = []
        self.magic_throw = ""
        self.spell_dc = 0
        self.spell_attack = 0
        self.cantrips = [0, []]
        self.lvl_one = [0, []]
        self.lvl_two = [0, []]
        self.lvl_three = [0, []]
        self.lvl_four = [0, []]
        self.lvl_five = [0, []]
        self.lvl_six = [0, []]
        self.lvl_seven = [0, []]
        self.lvl_eight = [0, []]
        self.lvl_nine = [0, []]

        self.spell_ct = 0
        self.spells = [self.lvl_one, self.lvl_two, self.lvl_three, self.lvl_four, self.lvl_five, self.lvl_six,
                       self.lvl_seven, self.lvl_eight, self.lvl_nine]

        self.swimming_speed()
        self.set_subrace(level)

    def set_subrace(self, level):
        subrace = raw_input("what extra feature do you want to have? weapon, cantrip, fleet, mask, drow, swim, or versatile? ")

        if(subrace == "weapon"):
            self.proficiency.append(str["longsword", "shortsword", "shortbow", "longbow"])
        if(subrace == "cantrip"):
            spell = raw_input("what extra spell do you want to have?? from wizard ")
            str(self.magic) + spell
            str(self.magic_throw) + "intelligence"
        if(subrace == "fleet"):
            self.speed = 35
        if(subrace == "mask"):
            self.proficiency.append("You can attempt to hide even when you are only lightly obscured"
                                    " by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
        if(subrace == "drow"):
            self.cantrips[0] += 1
            self.cantrips[1].append("Dancing lights")
            self.magic_throw = "charisma"
            if (level > 2):
                self.lvl_one[0] += 1
                self.lvl_two[1].append("faerie fire")
            if (level > 4):
                self.lvl_two[0] += 1
                self.lvl_two.append("darkness")
        if(subrace == "swim"):
            self.swim_speed = 30
        else:
            skill1 = raw_input("what extra skill do you want? ")
            skill2 = raw_input("what other extra skill do you want?")
            self.proficiency.append(str([skill1, skill2]))

    def swimming_speed(self):
        self.swim_speed = math.floor(self.speed / 2)