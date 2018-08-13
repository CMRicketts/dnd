import math


class Monk:
    def __init__(self, level, stre, dex, con, cha, inte, wis):
        self.strength = int(stre)
        self.constitution = int(con)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.intelligence = int(inte)
        self.wisdom = int(wis)
        self.hp = 0
        self.hit_dice = ""

        self.ki_ct = 0
        self.ki_dc = 0
        self.ki_features = []

        self.elem_feat = []

        self.level = int(level)

        self.feature = ["Unarmored Defense", "Martial Arts"]
        self.proficiency = ["simple weapons", "shortswords"]
        self.skill = []
        self.saving_throw = ["strength", "dexterity"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = []
        self.weapon = []
        self.armor = []

        self.way = ""

        if self.level == 1:
            self.init_hp()
        else:
            self.level_hp(self.level)

        self.proficiency_bonus = 2
        if 4 < self.level < 9:
            self.proficiency_bonus = 3
        if 8 < self.level < 13:
            self.proficiency_bonus = 4
        if 12 < self.level < 17:
            self.proficiency_bonus = 5
        if 16 < self.level:
            self.proficiency_bonus = 6

        if self.level > 3:
            self.ability()
        if self.level > 7:
            self.ability()
        if self.level > 11:
            self.ability()
        if self.level > 15:
            self.ability()
        if self.level > 18:
            self.ability()

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

        if self.level != 1:
            self.ki_ct = self.level
        self.unarmored_mvmt = 0
        if 1 < self.level < 6:
            self.unarmored_mvmt = 10
        if 5 < self.level < 10:
            self.unarmored_mvmt = 15
        if 9 < self.level < 14:
            self.unarmored_mvmt = 20
        if 13 < self.level < 18:
            self.unarmored_mvmt = 25
        if 17 < self.level:
            self.unarmored_mvmt = 30

        self.set_skill()
        self.set_equip()

        if self.level > 1:
            self.feature.append("Ki")
            self.ki_dc = 8 + self.proficiency_bonus + self.wisdom_mod()
            self.ki_features.append(str(["Flurry of Blows", "Patient Defense", "Step of the Wild"]))
            self.feature.append("Unarmored Movement")
        if self.level > 2:
            self.set_way()
            self.feature.append("Deflect Missiles")
        if self.level > 3:
            self.feature.append("Slow Fall")
        if self.level > 4:
            self.feature.append("Extra Attack")
            self.ki_features.append("Stunning Strike")
        if self.level > 5:
            self.feature.append("Ki-Empowered Strikes")
        if self.level > 6:
            self.feature.append("Evasion")
            self.feature.append("Stillness of Mind")
        if self.level > 9:
            self.resistance.append(str(["Disease", "Poison"]))
        if self.level > 12:
            self.language.append("all of them (Monk: Tongue of the Sun and Moon")
            self.feature.append("Tongue of the Sun and Moon")
        if self.level > 13:
            self.saving_throw = ["strength", "wisdom", "dexterity", "intelligence", "charisma", "constitution"]
            self.feature.append("Diamond Soul")
            self.ki_features.append("Diamond Soul")
        if self.level > 14:
            self.feature.append("Timeless Body")
        if self.level > 17:
            self.ki_features.append("Empty Body")
        if self.level > 19:
            self.ki_features.append("Perfect Self")

        self.init_hit_die()
        self.set_ac()

    def strength_mod(self):
        return math.floor((self.strength - 10) / 2)

    def dexterity_mod(self):
        return math.floor((self.dexterity - 10) / 2)

    def wisdom_mod(self):
        return math.floor((self.wisdom - 10) / 2)

    def constitution_mod(self):
        return math.floor((self.constitution - 10) / 2)

    def charisma_mod(self):
        return math.floor((self.charisma - 10) / 2)

    def intelligence_mod(self):
        return math.floor((self.intelligence - 10) / 2)

    def ability(self):
        print("Strength: " + str(self.strength) +
              "\nDexterity: " + str(self.dexterity) +
              "\nIntelligence: " + str(self.intelligence) +
              "\nWisdom: " + str(self.wisdom) +
              "\nCharisma: " + str(self.charisma) +
              "\nConstitution: " + str(self.constitution))
        choice = raw_input("levelling up: do you want to increase 'one' score by two, or 'two' scores by one each?"
                           "\nAbove are your scores")

        if choice == "one":
            score = raw_input("which ability do you want to increase by two?")
            if score == "strength":
                self.strength = self.strength + 2
            elif score == "dexterity":
                self.dexterity = self.dexterity + 2
            elif score == "intelligence":
                self.intelligence = self.intelligence + 2
            elif score == "wisdom":
                self.wisdom = self.wisdom + 2
            elif score == "charisma":
                self.charisma = self.charisma + 2
            else:
                self.constitution = self.constitution + 2
        else:
            score = raw_input("which ability do you want to increase by one?")
            if score == "strength":
                self.strength = self.strength + 1
            elif score == "dexterity":
                self.dexterity = self.dexterity + 1
            elif score == "intelligence":
                self.intelligence = self.intelligence + 1
            elif score == "wisdom":
                self.wisdom = self.wisdom + 1
            elif score == "charisma":
                self.charisma = self.charisma + 1
            else:
                self.constitution = self.constitution + 1
            score_two = raw_input("which second ability do you want to increase?")
            if score_two == "strength":
                self.strength = self.strength + 1
            elif score_two == "dexterity":
                self.dexterity = self.dexterity + 1
            elif score_two == "intelligence":
                self.intelligence = self.intelligence + 1
            elif score_two == "wisdom":
                self.wisdom = self.wisdom + 1
            elif score_two == "charisma":
                self.charisma = self.charisma + 1
            else:
                self.constitution = self.constitution + 1

    def init_hit_die(self):
        self.hit_dice = str(self.level) + "d8"

    def init_hp(self):
        print(str(self.constitution_mod()))
        self.hp = 10 + self.constitution_mod()

    def level_hp(self, level):
        print(self.constitution_mod())
        self.hp = 10 + (self.constitution_mod() * int(level))

    def set_skill(self):
        i = 0
        while i < 2:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Acrobatics, Athletics, History, Insight, Religion, Or Stealth? Please input ")
            self.skill.append(skill)
            i += 1

    def set_equip(self):
        weapon = raw_input("Initialization: Which do you want to have? a 'shortsword', or any simple weapon? Please input.")
        if weapon != "shortsword":
            self.weapon.append(weapon)
            self.equipment.append(weapon)
        else:
            self.weapon.append("shortsword")
            self.equipment.append("shortsword")
        pack = raw_input("which pack do you want: 'dungeoneer' or 'explorer'? ")
        if pack == "explorer":
            self.equipment.append("explorer's pack")
        else:
            self.equipment.append("dungeoneer's pack")
        self.weapon.append("10 darts")
        self.equipment.append("10 darts")

    def set_prof(self):
        tools = raw_input("Initialization: which do you want to be proficient in? Artisan's tools or one musical instrument? Please input specifically ")
        self.proficiency.append(tools)

    def set_ac(self):
        if not self.armor:
            self.armor = ["Unarmored", str(10 + self.dexterity_mod() + self.wisdom_mod())]

    def set_way(self):
        choice = raw_input("Which monastic tradition do you want to join? 'Drunken' Master, 'Four' Elements, 'Kensei', 'Long' Death, 'Open' Hand, 'Shadow', 'Sun' Soul, or 'Tranquility'?")
        choice = choice.lower()
        if choice == "drunken":
            self.drunk()
            self.way = "Way of the Drunken Master"
        elif choice == "four":
            self.four()
            self.way = "Way of the Four Elements"
        elif choice == "Kensei":
            self.ken()
            self.way = "Way of the Kensei"
        elif choice == "long":
            self.long()
            self.way = "Way of the Long Death"
        elif choice == "open":
            self.open()
            self.way = "Way of the Open Hand"
        elif choice == "shadow":
            self.shadow()
            self.way = "Way of the Shadow"
        elif choice == "sun":
            self.sun()
            self.way = "Way of the Sun Soul"
        else:
            self.tran()
            self.way = "Way of Tranquility"

    def tran(self):
        self.feature.append("Path of Tranquility")
        self.feature.append("Healing Hands")
        if self.level > 5:
            self.feature.append("Emissary of Peace")
            self.skill.append(raw_input("Which do you want to become proficient in: Performance or Persuasion?"))
        if self.level > 10:
            self.feature.append("Douse the Flames of War")
        if self.level > 16:
            self.feature.append("Anger of a Gentle Soul")

    def sun(self):
        self.feature.append("Radiant Sun Bolt")
        self.attack.append("Radiant Sun Bolt")
        if self.level > 5:
            self.feature.append("Searing Arc Strike")
            self.ki_features.append("Searing Arc Strike")
        if self.level > 10:
            self.feature.append("Searing Sunburst")
            self.attack.append("Searing Sunburst")
        if self.level > 16:
            self.feature.append("Sun Shield")

    def shadow(self):
        self.ki_features.append("Shadow Arts")
        self.cantrips[0] += 1
        self.cantrips[1].append("Minor Illusion")
        if self.level > 5:
            self.feature.append("Shadow Step")
        if self.level > 10:
            self.feature.append("Cloak of Shadows")
        if self.level > 16:
            self.feature.append("Opportunist")

    def open(self):
        self.feature.append("Open Hand Technique")
        if self.level > 5:
            self.feature.append("Wholeness of Body")
        if self.level > 10:
            self.feature.append("Tranquility")
        if self.level > 16:
            self.feature.append("Quivering Palm")
        #V2: generic 'archetype' class for each character class, to input features to not repeat code

    def long(self):
        self.feature.append("Touch of Death")
        if self.level > 5:
            self.feature.append("Hour of Reaping")
        if self.level > 10:
            self.feature.append("Mastery of Death")
        if self.level > 16:
            self.feature.append("Touch of the Long Death")

    def ken(self):
        self.feature.append("Path of the Kensei")
        if self.level > 5:
            self.feature.append("One with the Blade")
        if self.level > 10:
            self.ki_features.append("Sharpen the Blade")
        if self.level > 16:
            self.feature.append("Unerring Accuracy")

    def four(self):
        self.elem_feat.append("Elemental Attunement")
        self.set_elem()
        if self.level > 5:
            self.set_elem()
        if self.level > 10:
            self.set_elem()
        if self.level > 16:
            self.set_elem()

    def drunk(self):
        self.skill.append("Performance")
        self.proficiency.append("Brewer's Supplies")
        self.feature.append("Drunken Technique")
        if self.level > 5:
            self.feature.append("Leap to Your Feet")
            self.feature.append("Redirect Attack")
        if self.level > 10:
            self.ki_features.append("Drunkard's Luck")
        if self.level > 16:
            self.feature.append("Intoxicated Frenzy")

    def set_elem(self):
        base_elem = ["Fangs of the Fire Snake", "Fist of Four Thunders", "Fist of Unbroken Air", "Rush of the Gale Spirits",
                     "Shape the Flowing River", "Sweeping Cinder Strike", "Water Whip"]
        if self.level > 5:
            base_elem.append(["Clench of the North Wind", "Gong of the Summit"])
        if self.level > 10:
            base_elem.append(["Flames of the Phoenix", "Mist Stance", "Ride the Wind"])
        if self.level > 16:
            base_elem.append(["River of Hungry Flame", "Breath of Winter", "Eternal Mountain Defense"])
        elem = list(set(base_elem)-set(self.elem_feat))
        print("Which elemental discipline do you want to learn? They are printed below")
        for item in elem:
            print item
        self.elem_feat.append(raw_input(""))
