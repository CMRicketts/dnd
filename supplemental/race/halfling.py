class Halfling:
    def __init__(self):
        self.dexterity = 2
        self.charisma = 0
        self.constitution = 0
        self.age_low = 18
        self.age_high = 225
        self.height_low = 34
        self.height_high = 40
        self.weight_low = 35
        self.weight_high = 45
        self.size = "small"
        self.speed = 25
        self.proficiency = [self.lucky(), self.brave(), self.nimble()]
        self.resistance = []
        self.language = ["common", "halfling"]
        self.subrace = ""
        self.set_subrace()

    def set_subrace(self):
        subrace = raw_input("what subrace do you want to be? lightfoot or stout")
        if(subrace == "lightfoot"):
            self.subrace = "Lightfoot Halfling"
            self.charisma = 1
            self.proficiency.append(str(self.natural()))

        if(subrace == "stout"):
            self.subrace = "Stout Halfling"
            self.constitution = 1
            self.resistance.append("poison")
            self.proficiency.append("poison")

    def lucky(self):
        return "When you roll a 1 on an attack roll, ability check, or saving throw, " \
               "you can reroll the die. You must use the new result, even if it is a 1."

    def brave(self):
        return "You have advantage on saving throws against being frightened."

    def nimble(self):
        return "You can move through the space of any creature that is of a size larger than yours."

    def natural(self):
        return "You can attempt to hide even when you are only obscured" \
               " by a creature that is at least one size larger than you."