class Human:
    def __init__(self):
        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.charisma = 1
        self.intelligence = 1
        self.wisdom = 1
        self.age_low = 16
        self.age_high = 70
        self.weight_low = 80
        self.weight_high = 200
        self.height_low = 54
        self.height_high = 76
        self.size = "medium"
        self.speed = 30
        language1 = raw_input("what extra language do you want to have?")
        self.language = ["common", language1]