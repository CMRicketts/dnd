class Tiefling:
    def __init__(self, level):
        self.intelligence = 1
        self.charisma = 0
        self.dexterity = 0
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
        self.feature = []
        self.resistance = ["fire"]
        self.language = ["common", "infernal"]
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
        self.subrace = ""

        self.set_subrace(level)

    def set_subrace(self, level):
        subrace = raw_input("what feature do you want to have? devil, hellfire, winged, or infernal?")
        if(subrace == "devil"):
            self.subrace = "Devil's Tongue"
            self.cantrips[0] += 1
            self.cantrips[1].append("Vicious Mockery")
            if(level > 2):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Charm Person")
            if(level > 4):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Enthrall")
            self.magic_throw = "charisma"
        elif(subrace == "hellfire"):
            self.subrace = "Hellfire Tiefling"
            self.cantrips[0] += 1
            self.cantrips[1].append("Thaumaturgy")
            if (level > 2):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Burning Hands")
            if (level > 4):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Darkness")
            self.magic_throw = "charisma"
        elif(subrace == "winged"):
            self.subrace = "Winged Tiefling"
            self.feature.append("You have wings now")
            self.speed_flying = 30
        else:
            self.subrace = "Infernal Tiefling"
            self.cantrips[0] += 1
            self.cantrips[1].append("Thaumaturgy")
            if (level > 2):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Hellish Rebuke")
            if (level > 4):
                self.lvl_two[0] += 1
                self.lvl_two[1].append("Darkness")
            self.magic_throw = "charisma"