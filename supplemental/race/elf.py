class Elf:
    def __init__(self, level):
        self.dexterity = 2
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.age_low = 80
        self.age_high = 700
        self.weight_low = 100
        self.weight_high = 180
        self.height_low = 54
        self.height_high = 75
        self.speed = 30
        self.size = "medium"
        self.magic = []
        self.magic_throw = "charisma"
        self.disadvantage = ""
        self.proficiency = ["perception", "charm", "magic", self.trance()]
        self.feature = ["darkvision"]
        self.language = ["common", "elvish"]
        self.subrace = ""

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

        self.set_racee(level)

    def set_racee(self, level):
        race = raw_input("what race are you? high, wood, or dark?")
        race = race.lower()
        if race == "high":
            self.subrace = "High Elf"
            self.intelligence = 1
            self.proficiency.append(str(["longsword", "shortsword", "shortbow", "longbow"]))
            spell = raw_input("what spell do you want to add? ")
            self.magic = spell
            new_language = raw_input("what language do you want to add? ")
            self.language.append(str(new_language))

        elif race == "wood":
            self.subrace = "Wood Elf"
            self.wisdom = 1
            self.proficiency.append(str(["longsword", "shortsword", "shortbow", "longbow"]))
            self.speed = 35
            self.proficiency.append(str(self.mask()))

        elif race == "dark":
            self.subrace = "Dark Elf"
            self.charisma = 1
            self.proficiency.remove("darkvision")
            self.proficiency.append("superior darkvision")
            self.proficiency.append(str(["rapier", "shortsword", "hand crossbow"]))
            self.disadvantage = "wisdom"
            self.cantrips[0] += 1
            self.cantrips[1].append("Dancing lights")
            if level > 2:
                self.lvl_one[0] += 1
                self.lvl_one[1].append("faerie fire")
            if level > 4:
                self.lvl_two[0] += 1
                self.lvl_two[1].append("darkness")

    def trance(self):
        return "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. " \
               "The Common word for this meditation is 'trance'. While meditating, you dream after a fashion; " \
               "such dreams are actually mental exercises that have become reflexive after years of practice." \
               "After resting in this way, you gain the same benefit a human would from 8 hours of sleep."

    def mask(self):
        return "You can attempt to hide even when you are only lightly obscured by" \
               " foliage, heavy rain, falling snow, mist, and other natural phenomena."
