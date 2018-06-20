import math


class Fighter():
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

        self.archetype = ""
        self.style = ""

        self.feature = ["Second Wind"]
        self.proficiency = ["all armors", "all shields", "all weapons"]
        self.skill = []
        self.saving_throw = ["strength", "constitution"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = []
        self.weapon = []
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

        if self.level > 1:
            self.feature.append("Action Surge")
        if self.level > 4:
            self.feature.append("Extra attack")
        if self.level > 8:
            self.feature.append("Indomitable")

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
        self.set_style()

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
                "Initialization: What skill do you want to be proficient in? Acrobatics, Animal Handling, Athletics, History, Insight, or Intimidation? Please input ")
            self.skill.append(skill)
            i += 1

    def set_equip(self):
        weapon_one = raw_input(
            "Initialization: Which do you want, 'leather' armor, a longbow, and 20 arrows, or 'chain' mail? Please input ")
        if weapon_one != "leather":
            self.armor.append(["chain mail", "16"])
        else:
            self.equipment.append("longbow, 20 arrows")
            self.weapon.append("longbow, 20 arrows")
            self.armor.append(["leather armor", "11"])

        weapon_two = raw_input(
            "Initialization: Which do you want, a 'martial' weapon and a shield, or 'two' martial weapons? Please input ")
        if weapon_two == "martial":
            thing = raw_input("what martial weapon do you want?")
            self.equipment.append(["shield", str(thing)])
            self.weapon.append(thing)
        else:
            thing = raw_input("What two martial weapons do you want? Please input ")
            self.equipment.append(thing)
            self.weapon.append(thing)

        weapon_three = raw_input(
            "Initialization: Which do you want, a light 'crossbow' and 20 bolts, or two 'handaxes'? Please input ")
        if weapon_three == "crossbow":
            self.equipment.append("crossbow and 20 bolts")
            self.weapon.append("crossbow and 20 bolts")
        else:
            self.equipment.append("two handaxes")
            self.weapon.append("two handaxes")

        pack = raw_input("Which pack do you want? 'dungeoneers' pack, or 'explorers' pack?")
        if pack == "dungeoneers":
            self.equipment.append("dungeoneer's pack")
        else:
            self.equipment.append("explorer's pack")

    def set_style(self):
        style = raw_input("Initialization: Which of the following fighting styles do you want to learn? Please input. "
                          "\narchery, defense, dueling, great 'weapon' fighting, protection, 'two' weapon fighting, mariner, close quarter 'shooter', or 'tunnel' fighter?")
        if style == "archery":
            self.style = "archery"
            self.feature.append("fighting style: " + str(style))
        elif style == "dueling":
            self.style = "dueling"
            self.feature.append("fighting style: " + str(style))
        elif style == "weapon":
            self.style = "great weapon fighting"
            self.feature.append("fighting style: " + "great weapon fighting")
        elif style == "protection":
            self.style = "protection"
            self.feature.append("fighting style: " + str(style))
        elif style == "two":
            self.style = "two weapon fighting"
            self.feature.append("fighting style: " + "two weapon fighting")
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

    def set_archetype(self):
        arch = raw_input("Level up: Which archetype do you want to join? arcane, battle, brute, cavalier, champion, eldritch, monster, purple, samurai, scout, or sharpshooter?")
        if arch == "arcane":
            self.archetype = "arcane archer"
            self.arcane()
        elif arch == "battle":
            self.archetype = "battle master"
            self.battle()
        elif arch == "brute":
            self.archetype = str(arch)
            self.brute()
        elif arch == "cavalier":
            self.archetype = str(arch)
            self.cavalier()
        elif arch == "champion":
            self.archetype = str(arch)
            self.champion()
        elif arch == "eldritch":
            self.archetype = "eldritch knight"
            self.eld()
        elif arch == "monster":
            self.archetype = "monster hunter"
            self.monster()
        elif arch == "purple":
            self.archetype = "purple dragon knight"
            self.purple()
        elif arch == "samurai":
            self.archetype = str(arch)
            self.samurai()
        elif arch == "scout":
            self.archetype = str(arch)
            self.scout()
        else:
            self.archetype = "sharpshooter"
            self.sharpshooter()

    def sharpshooter(self):
        pass

    def scout(self):
        pass

    def samurai(self):
        pass

    def purple(self):
        pass

    def monster(self):
        pass

    def eld(self):
        pass

    def champion(self):
        pass

    def cavalier(self):
        pass

    def brute(self):
        pass

    def battle(self):
        pass

    def arcane(self):
        pass
