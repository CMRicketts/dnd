class Half_Orc:
    def __init__(self):
        self.strength = 2
        self.constitution = 1
        self.age_low = 13
        self.age_high = 70
        self.weight_low = 100
        self.weight_high = 300
        self.height_low = 58
        self.height_high = 86
        self.speed = 30
        self.size = "medium"
        self.proficiency = ["darkvision", "intimidation", self.endurance(), self.savage()]
        self.language = ["common", "orcish"]

    def endurance(self):
        return "When you are reduced to 0 hit points but not killed outright, " \
               "you can drop to 1 hit point instead. " \
               "You can't use this feature again until you finish a long rest."

    def savage(self):
        return "When you score a critical hit with a melee weapon attack," \
               " you can roll one of the weapon's damage dice one additional time" \
               " and add it lo the extra damage of lhe critical hit."
