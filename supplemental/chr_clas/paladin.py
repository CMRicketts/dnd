import math


class Paladin:
    def __init__(self, level, stre, dex, con, cha, inte, wis):
        self.strength = int(stre)
        self.constitution = int(con)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.intelligence = int(inte)
        self.wisdom = int(wis)
        self.hp = 0
        self.hit_dice = ""

        self.level = int(level)

        self.feature = ["Divine Sense", "Lay on Hands"]
        self.proficiency = ["all armor", "shields", "simple weapons", "martial weapons"]
        self.skill = []
        self.saving_throw = ["wisdom", "charisma"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["holy symbol"]
        self.weapon = []
        self.armor = ["chain mail", "16"]

        self.oath = ""
        self.oath_desc = []
        self.divinity_desc = []
        self.fighting_style = ""
        self.fighting_style_desc = []
        self.style = ""

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

        self.init_hit_die()
        self.set_skill()
        self.set_equip()
        self.set_spells()

        if self.level > 1:
            self.feature.append("Fighting Style")
            self.set_style()
            self.feature.append("Divine Smite")
            self.attack.append("Divine Smite")
            self.feature.append("Spellcasting")
            self.feature.append("Spellcasting Focus")
            self.spell_dc = 8 + self.proficiency_bonus + self.charisma_mod()
            self.spell_attack = self.proficiency_bonus + self.charisma_mod()
        if self.level > 2:
            self.feature.append("Divine Health")
            self.resistance.append("immune to disease (Divine Health)")
            self.set_oath()
        if self.level > 4:
            self.feature.append("Extra Attack")
        if self.level > 5:
            self.feature.append("Aura of Protection")
        if self.level > 9:
            self.feature.append("Aura of Courage")
        if self.level > 10:
            self.feature.append("Improved Divine Smite")
            self.attack.append("Improved Divine Smite")
        if self.level > 13:
            self.attack.append("Cleansing Touch")

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
        choice = raw_input("levelling up: do you want to increase 'one' score by two, or 'two' scores by one each?")
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
        self.hit_dice = str(self.level) + "d10"

    def init_hp(self):
        print(str(self.constitution_mod()))
        self.hp = 10 + self.constitution_mod()
        print(self.hp)

    def level_hp(self, level):
        print(self.constitution_mod())
        self.hp = 10 + (self.constitution_mod() * int(level))
        print(self.hp)

    def set_skill(self):
        i = 0
        while i < 2:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Athletics, Insight, Intimidation, Medicine, Persuasion, or Religion. Please input ")
            self.skill.append(skill)
            i += 1

    def set_equip(self):
        pack = raw_input("Initialization: Do you want a 'priest' pack or 'explorer' pack?")
        if pack == "priest":
            self.equipment.append("Priest's pack")
        else:
            self.equipment.append("Explorer's pack")
        throw = raw_input("Initialization: Do you want 5 'javelins' or any other simple melee weapon? Please input")
        if throw != "javelins":
            self.equipment.append(throw)
            self.weapon.append(throw)
        else:
            self.weapon.append("5 javelins")
            self.equipment.append("5 javelins")
        one = raw_input("Initialization: Do you want one martial weapon and a 'shield', or 'two' martial weapons? Please input")
        if one == "shield":
            self.equipment.append("shield")
            wpn = raw_input("Which martial weapon do you want?")
            self.equipment.append(wpn)
            self.weapon.append(wpn)
        else:
            wpns = raw_input("Which two martial weapons do you want? Please input ")
            self.weapon.append(wpns)
            self.equipment.append(wpns)

    def set_spells(self):
        if self.level > 1:
            self.lvl_one[0] = 2
            self.lvl_one[1].append(raw_input("Level up: What other level one spell do you want to learn?"))
        if self.level > 2:
            self.lvl_one[0] = 3
            self.lvl_one[1].append(raw_input("Level up: What final level one spell do you want to learn?"))
        if self.level > 4:
            self.lvl_one[0] = 4
            self.lvl_one[1].append(raw_input("Level up: What final level one spell do you want to learn?"))
            self.lvl_two[0] = 2
            self.lvl_two[1].append(raw_input("What two level two spells do you want to learn?"))
        if self.level > 6:
            self.lvl_two[0] = 3
            self.lvl_two[1].append(raw_input("Level up: What final level two spell do you want to learn?"))
        if self.level > 7:
            self.lvl_four[0] = 2
            self.lvl_four[1].append(raw_input("Level up: What level four spell do you want to learn?"))
        if self.level > 8:
            self.lvl_three[0] = 2
            self.lvl_three[1].append(raw_input("Level up: What two level three spells do you want to learn?"))
            self.lvl_four[0] = 3
            self.lvl_four[1].append(raw_input("Level up: What final level four spell do you want to learn?"))
        if self.level > 10:
            self.lvl_three[0] = 3
            self.lvl_three[1].append(raw_input("Level up: What final level three spells do you want to learn?"))
        if self.level > 12:
            self.lvl_four[0] = 1
            self.lvl_four[1].append(raw_input("Level up: What level four spell do you want to learn?"))
        if self.level > 14:
            self.lvl_four[0] = 2
            self.lvl_four[1].append(raw_input("Level up: What level four spell do you want to learn?"))
            self.lvl_five[0] = 1
            self.lvl_five[1].append(raw_input("What level five spell do you want to learn?"))
        if self.level > 16:
            self.lvl_four[0] = 3
            self.lvl_four[1].append(raw_input("Level up: What final level four spell do you want to learn?"))
        if self.level > 17:
            self.lvl_five[0] = 3
            self.lvl_five[1].append(raw_input("Level up: What final level five spell do you want to learn?"))
        if self.level > 18:
            self.lvl_five[0] = 2
            self.lvl_five[1].append(raw_input("Level up: What level five spell do you want to learn?"))

    def set_oath(self):
        pass

    def set_style(self):
        style = raw_input("Initialization: Which of the following fighting styles do you want to learn? Please input. "
                          "\ndefense, dueling, great 'weapon' fighting, protection, mariner, close quarter 'shooter', or 'tunnel' fighter?")
        if style == "dueling":
            self.style = "dueling"
            self.feature.append("fighting style: " + str(style))
        elif style == "weapon":
            self.style = "great weapon fighting"
            self.feature.append("fighting style: " + "great weapon fighting")
        elif style == "protection":
            self.style = "protection"
            self.feature.append("fighting style: " + str(style))
        elif style == "mariner":
            self.style = "mariner"
            self.feature.append(str(style))
        elif style == "shooter":
            self.style = "close quarters shooter"
            self.feature.append("fighting style: " + "close quarters shooter")
        elif style == "tunnel":
            self.style = "tunnel fighter"
            self.feature.append("fighting style: " + "tunnel fighter")
        else:
            self.style = "Defense"
            self.feature.append("fighting style: " + "Defense")