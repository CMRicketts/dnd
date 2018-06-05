class Elf:
    def __init__(self, level):
        self.dexterity = 2
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.age_low = 80
        self.age_high = 700
        self.height_low = 54
        self.height_high = 75
        self.speed = 30
        self.size = "medium"
        self.magic = ""
        self.magic_throw = "charisma"
        self.disadvantage = ""
        self.proficiency = ["darkvision", "perception", "charm", "magic", self.trance()]
        self.language = ["common", "elvish"]
        self.set_racee(level)

    def set_racee(self, level):
        race = raw_input("what race are you? high, wood, or dark?")
        race = race.lower()
        if (race == "high"):
            self.intelligence = 1
            self.proficiency.append(str(["longsword", "shortsword", "shortbow", "longbow"]))
            spell = raw_input("what spell do you want to add? ")
            self.magic = spell
            new_language = raw_input("what language do you want to add? ")
            self.language.append(str(new_language))

        elif (race == "wood"):
            self.wisdom = 1
            self.proficiency.append(str(["longsword", "shortsword", "shortbow", "longbow"]))
            self.speed = 35
            self.proficiency.append(str(self.mask()))

        elif (race == "dark"):
            self.charisma = 1
            self.proficiency.remove("darkvision")
            self.proficiency.append("superior darkvision")
            self.proficiency.append(str(["rapier", "shortsword", "hand crossbow"]))
            self.disadvantage = "wisdom"
            self.magic = " dancing lights"
            if (level > 2):
                str(self.magic) + " faerie fire"
            if (level > 4):
                str(self.magic) + " darkness"

    def trance(self):
        return "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. " \
               "The Common word for this meditation is 'trance'. While meditating, you dream after a fashion; " \
               "such dreams are actually mental exercises that have become reflexive after years of practice." \
               "After resting in this way, you gain the same benefit a human would from 8 hours of sleep."

    def mask(self):
        return "You can attempt to hide even when you are only lightly obscured by" \
               " foliage, heavy rain, falling snow, mist, and other natural phenomena."
