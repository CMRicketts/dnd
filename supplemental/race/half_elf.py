class Half_Elf:
    def __init__(self, level):
        self.charisma = 2

        ability1 = raw_input("what ability score do you want to increase?")
        self.ability1 = 1
        ability2 = raw_input("what other ability score do you want to increase?")
        self.ability2 = 1

        self.age_low = 17
        self.age_high = 175
        self.weight_low = 100
        self.weight_high = 140
        self.height_low = 55
        self.height_high = 75
        self.speed = 30
        self.swim_speed = 0
        self.proficiency = ["darkvision"]
        self.advantage = ["charm", "magic sleep"]

        language = raw_input("what language do you want to add? ")

        self.language = ["common", "elvish", language]
        self.magic = ""
        self.magic_throw = ""
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
            self.magic = " dancing lights"
            self.magic_throw = "charisma"
            if (level > 2):
                str(self.magic) + " faerie fire"
            if (level > 4):
                str(self.magic) + " darkness"
        if(subrace == "swim"):
            self.swim_speed = 30
        else:
            skill1 = raw_input("what extra skill do you want? ")
            skill2 = raw_input("what other extra skill do you want?")
            self.proficiency.append(str([skill1, skill2]))