class Dragonborn():
    def __init__(self, level):
        color_input = raw_input(
            "what color dragonborn do you want to be? black, blue, brass, bronze, copper, gold, green, "
            "red, silver, or white?")
        self.color = []
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
        self.set_color(color_input)
        self.attack = self.breath_attack(level)
        self.resistance = self.color[0]

    def set_color(self, color):
        if color == "black":
            self.color = ["acid", "dex", "line 5' by 30'"]
        if color == "blue":
            self.color = ["lightning", "dex", "line 5' by 30'"]
        if color == "brass":
            self.color = ["fire", "dex", "line 5' by 30'"]
        if color == "bronze":
            self.color = ["lightning", "dex", "line 5' by 30'"]
        if color == "copper":
            self.color = ["acid", "dex", "line 5' by 30'"]
        if color == "gold":
            self.color = ["fire", "dex", "cone 15'"]
        if color == "green":
            self.color = ["poison", "con", "cone 15'"]
        if color == "red":
            self.color = ["fire", "dex", "cone 15'"]
        if color == "silver":
            self.color = ["cold", "con", "cone 15'"]
        if color == "white":
            self.color = ["cold", "con", "cone 15'"]

    def breath_attack(self, level):
        saving_throw = self.color[1]
        dc_base = 8
        slots = 1
        dmg = "2d6"
        if (level < 11):
            dmg = "4d6"
        elif (level < 16):
            dmg = "5d6"

        return [saving_throw, dc_base, slots, dmg]
