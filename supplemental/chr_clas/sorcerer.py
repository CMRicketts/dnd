import math


class Sorcerer:
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

        self.origin = ""
        self.metamagic_desc = []
        self.sorcery_pts = 0

        self.feature = ["Spellcasting Focus"]
        self.proficiency = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
        self.skill = []
        self.saving_throw = ["constitution", "charisma"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["two daggers"]
        self.weapon = ["two daggers"]
        self.armor = []

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
        self.magic_throw = "charisma"
        self.spell_dc = 8 + self.charisma_mod() + self.proficiency_bonus
        self.spell_attack = self.charisma_mod() + self.proficiency_bonus
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

        if self.level > 1:
            self.sorcery_pts = self.level
            self.feature.append("Sorcery Points")
            self.feature.append("Flexible Casting")
        if self.level > 2:
            self.feature.append("Metamagic")
            self.set_metamagic()
        if self.level > 9:
            self.set_metamagic()
        if self.level > 16:
            self.set_metamagic()
        if self.level > 19:
            self.feature.append("Sorcerous Restoration")

        self.init_hit_die()
        self.set_skill()
        self.set_equip()
        self.set_cantrip()
        self.set_spells()

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

    def set_cantrip(self):
        self.cantrips[0] = 4
        self.cantrips[1].append(raw_input("Initialization: What two cleric cantrips do you want to add?"))
        if self.level > 3:
            self.cantrips[0] = 5
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))
        if self.level > 9:
            self.cantrips[0] = 6
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))

    def set_spells(self):
        self.lvl_one[0] = 2
        self.lvl_one[1].append(raw_input("What two level one spells do you want to learn?"))
        if self.level > 1:
            self.lvl_one[0] = 3
            self.lvl_one[1].append(raw_input("Level up: What other level one spell do you want to learn?"))
        if self.level > 2:
            self.lvl_one[0] = 4
            self.lvl_one[1].append(raw_input("Level up: What final level one spell do you want to learn?"))
            self.lvl_two[0] = 2
            self.lvl_two[1].append(raw_input("What two level two spells do you want to learn?"))
        if self.level > 3:
            self.lvl_two[0] = 3
            self.lvl_two[1].append(raw_input("Level up: What final level two spell do you want to learn?"))
        if self.level > 4:
            self.lvl_three[0] = 2
            self.lvl_three[1].append(raw_input("Level up: What two level three spells do you want to learn?"))
        if self.level > 5:
            self.lvl_three[0] = 3
            self.lvl_three[1].append(raw_input("Level up: What final level three spells do you want to learn?"))
        if self.level > 6:
            self.lvl_four[0] = 1
            self.lvl_four[1].append(raw_input("Level up: What level four spell do you want to learn?"))
        if self.level > 7:
            self.lvl_four[0] = 2
            self.lvl_four[1].append(raw_input("Level up: What level four spell do you want to learn?"))
        if self.level > 8:
            self.lvl_four[0] = 3
            self.lvl_four[1].append(raw_input("Level up: What final level four spell do you want to learn?"))
            self.lvl_five[0] = 1
            self.lvl_five[1].append(raw_input("What level five spell do you want to learn?"))
        if self.level > 9:
            self.lvl_five[0] = 2
            self.lvl_five[1].append(raw_input("Level up: What level five spell do you want to learn?"))
        if self.level > 10:
            self.lvl_six[0] = 1
            self.lvl_six[1].append(raw_input("Level up: What level six spell do you want to learn?"))
        if self.level > 12:
            self.lvl_seven[0] = 2
            self.lvl_seven[1].append(raw_input("Level up: What level seven spell do you want to learn?"))
        if self.level > 14:
            self.lvl_eight[0] = 1
            self.lvl_eight[1].append(raw_input("Level up: What final level eight spell do you want to learn?"))
        if self.level > 16:
            self.lvl_nine[0] = 1
            self.lvl_nine[1].append(raw_input("Level up: What final level nine spell do you want to learn?"))
        if self.level > 17:
            self.lvl_five[0] = 3
            self.lvl_five[1].append(raw_input("Level up: What final level five spell do you want to learn?"))
        if self.level > 18:
            self.lvl_six[0] = 2
            self.lvl_six[1].append(raw_input("Level up: What final level six spell do you want to learn?"))
        if self.level > 19:
            self.lvl_seven[0] = 2
            self.lvl_seven[1].append(raw_input("Level up: What final level seven spell do you want to learn?"))

    def init_hit_die(self):
        self.hit_dice = str(self.level) + "d6"

    def init_hp(self):
        print(str(self.constitution_mod()))
        self.hp = 6 + self.constitution_mod()
        print(self.hp)

    def level_hp(self, level):
        print(self.constitution_mod())
        self.hp = 6 + (self.constitution_mod() * int(level))
        print(self.hp)

    def set_skill(self):
        i = 0
        while i < 2:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Arcana, Deception, Insight, Persuasion, or Religion? Please input ")
            self.skill.append(skill)
            i += 1

    def set_equip(self):
        weapon_one = raw_input(
            "Initialization: Which do you want, a light 'crossbow' and 20 bolts, or any simple weapon? Please input ")
        if weapon_one != "crossbow":
            self.equipment.append(weapon_one)
            self.weapon.append(weapon_one)
        else:
            self.equipment.append("A light crossbow with 20 bolts")
            self.weapon.append("A light crossbow with 20 bolts")
        pack = raw_input(
            "Which pack do you want? a 'dungeoneer' pack, or 'explorer' pack? Please input. ")
        if pack == "dungeoneer":
            self.equipment.append("Dungeoneer's pack")
        else:
            self.equipment.append("Explorer's pack")
        arcana = raw_input("Do you want a component 'pouch' or an 'arcane' focus?")
        if arcana == "pouch":
            self.equipment.append("component pouch")
        else:
            self.equipment.append("an arcane focus")

    def set_metamagic(self):
        pass
