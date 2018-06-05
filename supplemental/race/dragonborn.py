class Dragonborn():
    def __init__(self, level):
        color_input = raw_input(
            "what color dragonborn do you want to be? black, blue, brass, bronze, copper, gold, green, "
            "red, silver, or white?")
        self.color = self.set_color(color_input)
        self.level = level
        self.strength = 2
        self.charisma = 1
        self.age_low = 3
        self.age_high = 80
        self.weight_low = 200
        self.weight_high = 400
        self.height_low = 65
        self.height_high = 85
        self.speed = 30
        self.size = "medium"
        self.languages = ["common", "draconic"]
        self.color = breath_attack(color_input, level)
        self.resistance = breath_attack(color_input, level)

    def set_color(self, color):
        if color == "black":
            return ["acid", "dex", "line 5' by 30'"]
        if color == "blue":
            return ["lightning", "dex", "line 5' by 30'"]
        if color == "brass":
            return ["fire", "dex", "line 5' by 30'"]
        if color == "bronze":
            return ["lightning", "dex", "line 5' by 30'"]
        if color == "copper":
            return ["acid", "dex", "line 5' by 30'"]
        if color == "gold":
            return ["fire", "dex", "cone 15'"]
        if color == "green":
            return ["poison", "con", "cone 15'"]
        if color == "red":
            return ["fire", "dex", "cone 15'"]
        if color == "silver":
            return ["cold", "con", "cone 15'"]
        if color == "white":
            return ["cold", "con", "cone 15'"]


def breath_attack(color, level):
    saving_throw = color[1]
    dc_base = 8
    slots = 1
    dmg = "2d6"
    if (level < 11):
        dmg = "4d6"
    elif (level < 16):
        dmg = "5d6"

    return [saving_throw, dc_base, slots, dmg]
