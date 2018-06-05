class Tiefling:
    def __init__(self, level):
        self.intelligence = 1
        ability = raw_input("do you want to increase charisma or dexterity? default is dexterity")
        if(ability == "charisma"):
            self.charisma = 2
        else:
            self.dexterity = 2
        self.age_low = 16
        self.age_high = 80
        self.weight_low = 80
        self.weight_high = 200
        self.height_low = 54
        self.height_high = 76
        self.size = "medium"
        self.speed = 30
        self.speed_flying = 0
        self.proficiency = ["darkvision"]
        self.resistance = ["fire"]
        self.language = ["common", "infernal"]
        self.magic = ""
        self.magic_throw = ""

        self.set_subrace(level)

    def set_subrace(self, level):
        subrace = raw_input("what feature do you want to have? devil, hellfire, winged, or infernal?")
        if(subrace == "devil"):
            str(self.magic) + "vicious mockery"
            if(level > 2):
                str(self.magic) + " charm person"
            if(level > 4):
                str(self.magic) + " enthrall"
            self.magic_throw = "charisma"
        if(subrace == "hellfire"):
            str(self.magic) + "thaumaturgy"
            if (level > 2):
                str(self.magic) + " enthrall"
            if (level > 4):
                str(self.magic) + " darkness"
            self.magic_throw = "charisma"
        if(subrace == "winged"):
            self.proficiency.append("You have wings now")
            self.speed_flying = 30
        else:
            str(self.magic) + "thaumaturgy"
            if (level > 2):
                str(self.magic) + " hellish rebuke"
            if (level > 4):
                str(self.magic) + " darkness"
            self.magic_throw = "charisma"