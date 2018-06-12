import math


class Cleric:
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

        self.feature = ["Ritual Casting", "Spellcasting Focus"]
        self.proficiency = ["light armor", "medium armor", "shields", "all simple weapons"]
        self.skill = []
        self.saving_throw = ["wisdom", "charisma"]

        self.domain = ""

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
        self.spells = [self.cantrips, self.lvl_one, self.lvl_two, self.lvl_three, self.lvl_four, self.lvl_five,
                       self.lvl_six,
                       self.lvl_seven, self.lvl_eight, self.lvl_nine]

        self.attack = []
        self.equipment = []
        self.weapon = []
        self.armor = []

        self.equip()
        self.skills()

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

    def count_spells(self):
        for number in self.spells:
            self.spell_ct += number[0]

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
        self.hit_dice = str(self.level) + "d8"

    def init_hp(self):
        print(str(self.constitution_mod()))
        self.hp = 8 + self.constitution_mod()
        print(self.hp)

    def level_hp(self, level):
        print(self.constitution_mod())
        self.hp = 8 + (self.constitution_mod() * int(level))
        print(self.hp)

    def set_dc(self):
        self.spell_dc = 8 + self.proficiency_bonus + self.wisdom_mod()

    def set_mg_attack(self):
        self.spell_attack = self.proficiency_bonus + self.wisdom_mod()

    def skills(self):
        i = 0
        while i < 2:
            self.skill.append(raw_input("Initialization: what skill do you want to be proficient in? History, "
                                        "Insight, Medicine, Persuasion, or Relaigion?"))
            i += 1

    def equip(self):
        item = raw_input("do you want a Mace or Warhammer?")
        self.weapon.append(item)
        pack = raw_input("what pack do you want? Priest's pack or Explorer's pack?")
        self.equipment.append(pack)
        ranged = raw_input("Which do you prefer: a light 'crossbow' and 20 bolts, or any simple weapon (please input)")
        if ranged != "crossbow":
            self.equipment.append(ranged)
            self.weapon.append(ranged)
        else:
            self.equipment.append("Crossbow with 20 bolts")
            self.weapon.append("Crossbow with 20 bolts")
        armor = raw_input("Which armor do you want: 'scale' mail, 'leather' armor, or 'chain' mail (if proficient)?")
        if armor == "scale":
            self.armor.append(["scale mail", "14"])
        elif armor == "leather":
            self.armor.append(["leather armor", "11"])
        else:
            self.armor.append(["Chain Mail", "16"])
        self.equipment.append("Shield")
        symbol = raw_input("What holy symbol do you want to use?")
        self.equipment.append(str(symbol))

    def set_domain(self):
        domain = raw_input("What domain do you want to enter? There's a lot, so take your time.\n\tarcana, ambition, "
                           "city, death, forge, grave, knowledge, life, light,\n\tnature, order, protection, "
                           "solidarity, strength, tempest, trickery, war, or zeal?")
        if domain == "arcana":
            self.domain = "Arcana Domain"
            self.arcana()
        elif domain == "ambition":
            self.domain = "Ambition Domain"
            self.ambition()
        elif domain == "city":
            self.domain = "City Domain"
            self.city()
        elif domain == "death":
            self.domain = "Death Domain"
            self.death()
        elif domain == "forge":
            self.domain = "Forge Domain"
            self.forge()
        elif domain == "grave":
            self.domain = "Grave Domain"
            self.grave()
        elif domain == "knowledge":
            self.domain = "Knowledge Domain"
            self.knowledge()
        elif domain == "zeal":
            self.domain = "Zeal Domain"
            self.zeal()
        elif domain == "light":
            self.domain = "Light Domain"
            self.light()
        elif domain == "nature":
            self.domain = "Nature Domain"
            self.nature()
        elif domain == "order":
            self.domain = "Order Domain"
            self.order()
        elif domain == "protection":
            self.domain = "Protection Domain"
            self.protection()
        elif domain == "solidarity":
            self.domain = "Solidarity Domain"
            self.solidarity()
        elif domain == "strength":
            self.domain = "Strength Domain"
            self.strength_domain()
        elif domain == "tempest":
            self.domain = "Tempest Domain"
            self.tempest()
        elif domain == "trickery":
            self.domain = "Trickery Domain"
            self.trickery()
        elif domain == "war":
            self.domain = "War Domain"
            self.war()
        else:
            self.domain = "Zeal Domain"
            self.zeal()

    def zeal(self):
        pass

    def war(self):
        pass

    def trickery(self):
        pass

    def tempest(self):
        pass

    def strength_domain(self):
        pass

    def solidarity(self):
        pass

    def protection(self):
        pass

    def order(self):
        pass

    def nature(self):
        pass

    def light(self):
        pass

    def zeal(self):
        pass

    def knowledge(self):
        pass

    def grave(self):
        pass

    def forge(self):
        pass

    def death(self):
        pass

    def city(self):
        pass

    def ambition(self):
        pass

    def arcana(self):
        pass

