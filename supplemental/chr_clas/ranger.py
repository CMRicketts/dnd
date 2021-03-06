import math


class Ranger:
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

        self.feature = ["Favored Enemy", "Natural Explorer"]
        self.proficiency = ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"]
        self.skill = []
        self.saving_throw = ["strength", "dexterity"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["longbow and quiver of 20 arrows"]
        self.weapon = ["longbow and quiver of 20 arrows"]
        self.armor = []

        self.master = ""
        self.master_desc = []
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

        if self.level > 1:
            self.feature.append("Spellcasting")
            self.magic_throw = "wisdom"
            self.spell_attack = self.proficiency_bonus + self.wisdom_mod()
            self.spell_dc = self.proficiency_bonus + self.wisdom_mod() + 8
            self.set_style()
        if self.level > 2:
            self.set_master()
            self.feature.append("Primeval Awareness")
        if self.level > 4:
            self.feature.append("Extra Attack")
        if self.level > 7:
            self.feature.append("Land's Stride")
        if self.level > 9:
            self.feature.append("Hide in Plain Sight")
        if self.level > 13:
            self.feature.append("Vanish")
        if self.level > 17:
            self.feature.append("Feral Senses")
        if self.level > 19:
            self.feature.append("Foe Slayer")

        self.init_hit_die()
        self.set_skill()
        self.set_equip()

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
        choice = raw_input("leveling up: do you want to increase 'one' score by two, or 'two' scores by one each?")
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
        while i < 3:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival? Please input ")
            self.skill.append(skill)
            i += 1

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

    def set_equip(self):
        armor = raw_input("Which armor do you want? 'scale' mail or 'leather' armor? Please input ")
        if armor == "scale":
            self.armor.append(["scale mail", "14"])
        else:
            self.armor.append(["leather", "11"])
        weapons = raw_input("Which weapons do you want: two 'shortswords' or two 'simple' martial weapons? Please input ")
        if weapons == "shortswords":
            self.equipment.append("two shortswords")
            self.weapon.append("two shortswords")
        else:
            two = raw_input("Which two weapons do you want? Please input ")
            self.equipment.append(two)
            self.weapon.append(two)
        pack = raw_input("which pack do you want: 'dungeoneer' or 'explorer'? ")
        self.equipment.append(pack)

    def set_style(self):
        style = raw_input("Initialization: Which of the following fighting styles do you want to learn? Please input. "
                          "\narchery, defense, dueling, 'two' weapon fighting, mariner, close quarter 'shooter', or 'tunnel' fighter?")
        if style == "archery":
            self.style = "archery"
            self.feature.append("fighting style: " + str(style))
        elif style == "dueling":
            self.style = "dueling"
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

    def set_master(self):
        circle = raw_input(
            "Level up: Which archetype do you want to join? beast, gloom, horizon, hunter, monster, or primeval?")
        if circle == "beast":
            self.master = "Beast Master"
            self.beast()
        elif circle == "gloom":
            self.master = "Gloom Stalker"
            self.gloom()
        elif circle == "horizon":
            self.master = "Horizon Walker"
            self.hzn()
        elif circle == "hunter":
            self.master = "Hunter"
            self.hunter()
        elif circle == "monster":
            self.master = "Monster Slayer"
            self.monster()
        else:
            self.master = "Primeval Guardian"
            self.prim()

    def prim(self):
        self.lvl_one[0] += 1
        self.lvl_one[1].append("Entangle")
        if self.level > 4:
            self.lvl_two[0] += 1
            self.lvl_two[1].append(
                "Enhance Ability")  # V2 - make a 'add spell' function, takes in its level and name, automatically adds to character
        if self.level > 8:
            self.lvl_three[0] += 1
            self.lvl_three[1].append("Conjure Animals")
        if self.level > 12:
            self.lvl_four[0] += 1
            self.lvl_four[1].append("Giant Insect")
        if self.level > 16:
            self.lvl_five[0] += 1
            self.lvl_five[1].append("Insect Plague")
        self.feature.append("Guardian Soul")
        self.feature.append("Piercing Thorns")
        if self.level > 6:
            self.feature.append("Ancient Fortitude")
        if self.level > 10:
            self.feature.append("Rooted Defense")
        if self.level > 14:
            self.feature.append("Guardian Aura")

    def monster(self):
        self.lvl_one[0] += 1
        self.lvl_one[1].append("Protection from Good and Evil")
        if self.level > 4:
            self.lvl_two[0] += 1
            self.lvl_two[1].append(
                "Zone of Truth")  # V2 - make a 'add spell' function, takes in its level and name, automatically adds to character
        if self.level > 8:
            self.lvl_three[0] += 1
            self.lvl_three[1].append("Magic circle")
        if self.level > 12:
            self.lvl_four[0] += 1
            self.lvl_four[1].append("Banishment")
        if self.level > 16:
            self.lvl_five[0] += 1
            self.lvl_five[1].append("hold monster")
        self.feature.append("Hunter's Sense")
        self.feature.append("Slayer's Prey")
        if self.level > 6:
            self.feature.append("Supernatural Defense")
        if self.level > 10:
            self.feature.append("Magic-User's Nemesis")
        if self.level > 14:
            self.feature.append("Slayer's Counter")

    def hunter(self):
        choice = raw_input("Which feature do you want? colossus 'slayer', giant 'killer', or horde 'breaker? ")
        if choice == "slayer":
            self.feature.append("Colossus Slayer")
        elif choice == "killer":
            self.feature.append("Giant Killer")
        else:
            self.feature.append("Horde Breaker")
        if self.level > 6:
            choice = raw_input("Which feature do you want? escape the 'horde', multiattack 'defense', or steel 'will'? ")
            if choice == "horde":
                self.feature.append("Escape the Horde")
            elif choice == "defense":
                self.feature.append("Multiattack Defense")
            else:
                self.feature.append("Steel Will")
        if self.level > 10:
            choice = raw_input("Which feature do you want? 'volley', or whirlwind 'attack'? ")
            if choice == "volley":
                self.feature.append("Volley")
            else:
                self.feature.append("Whirlwind Attack")
        if self.level > 14:
            choice = raw_input("Which feature do you want? 'evasion', 'stand' against the tide, or uncanny 'dodge'? ")
            if choice == "evasion":
                self.feature.append("Evasion")
            elif choice == "stand":
                self.feature.append("Stand Against the Tide")
            else:
                self.feature.append("Uncanny Dodge")

    def hzn(self):
        self.lvl_one[0] += 1
        self.lvl_one[1].append("Protection from Good and Evil")
        if self.level > 4:
            self.lvl_two[0] += 1
            self.lvl_two[1].append("Misty Step")  # V2 - make a 'add spell' function, takes in its level and name, automatically adds to character
        if self.level > 8:
            self.lvl_three[0] += 1
            self.lvl_three[1].append("Haste")
        if self.level > 12:
            self.lvl_four[0] += 1
            self.lvl_four[1].append("Banishment")
        if self.level > 16:
            self.lvl_five[0] += 1
            self.lvl_five[1].append("Teleportation Circle")
        self.feature.append("Detect Portal")
        self.feature.append("Planar Warrior")
        if self.level > 6:
            self.feature.append("Ethereal Step")
        if self.level > 10:
            self.feature.append("Distant Strike")
        if self.level > 14:
            self.feature.append("Spectral Defense")

    def gloom(self):
        self.lvl_one[0] += 1
        self.lvl_one[1].append("Disguise Self")
        if self.level > 4:
            self.lvl_two[0] += 1
            self.lvl_two[1].append("Rope Trick") #V2 - make a 'add spell' function, takes in its level and name, automatically adds to character
        if self.level > 8:
            self.lvl_three[0] += 1
            self.lvl_three[1].append("Fear")
        if self.level > 12:
            self.lvl_four[0] += 1
            self.lvl_four[1].append("Greater Invisibility")
        if self.level > 16:
            self.lvl_five[0] += 1
            self.lvl_five[1].append("Seeming")
        self.feature.append("Dread Ambusher")
        self.feature.append("Umbral Sight")
        if self.level > 6:
            if "wisdom" in self.saving_throw:
                self.saving_throw.append(raw_input("Do you want advantage on charisma or intelligence saving throws?"))
            else:
                self.saving_throw.append("wisdom")
        if self.level > 10:
            self.feature.append("Stalker's Flurry")
        if self.level > 14:
            self.feature.append("Shadowy Dodge")

    def beast(self):
        self.feature.append("Ranger's Companion")
        if self.level > 6:
            self.feature.append("Exceptional Training")
        if self.level > 10:
            self.feature.append("Bestial Fury")
        if self.level > 14:
            self.feature.append("Share Spells")
