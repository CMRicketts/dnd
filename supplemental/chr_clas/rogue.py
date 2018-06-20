import math


class Rogue:
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

        self.feature = ["Thieves' Cant"]
        self.proficiency = ["light armor", "simple weapons", "hand crossbow", "longswords", "rapiers", "shortswords", "thieves' tools"]
        self.skill = []
        self.saving_throw = ["dexterity", "intelligence"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["two daggers", "thieves' tools"]
        self.weapon = ["two daggers"]
        self.armor = ["leather armor", "11"]

        self.archetype = ""

        self.sneak_attack_desc = ["Sneak Attack"]
        self.sneak_attack_dmg = ""
        self.expert_skills = []

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
            self.feature.append("Cunning Action")
        if self.level > 2:
            self.set_archetype()
        if self.level > 4:
            self.feature.append("Uncanny Dodge")
        if self.level > 6:
            self.feature.append("Evasion")
        if self.level > 10:
            self.feature.append("Reliable Talent")
        if self.level > 13:
            self.feature.append("Blindsense")
        if self.level > 15:
            self.saving_throw.append("wisdom")
        if self.level > 17:
            self.feature.append("Elusive")
        if self.level > 19:
            self.feature.append("Stroke of Luck")

        self.init_hit_die()
        self.set_skill()
        self.set_equip()
        self.set_sneak_attack_dmg()
        if self.level > 0:
            self.set_expertise()
        if self.level > 5:
            self.set_expertise()

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

    def set_sneak_attack_dmg(self):
        self.sneak_attack_dmg = str(math.ceil(self.level / 2)) + " d6"

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

    def set_skill(self):
        i = 0
        while i < 4:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, or Stealth? Please input ")
            self.skill.append(skill)
            i += 1

    def set_equip(self):
        pack = raw_input("Which pack do you want? 'burglar' pack, 'dungeoneer' pack, or 'explorer' pack? Please input. ")
        if pack == "burglar":
            self.equipment.append("Burglar's pack")
        elif pack == "dungeoneer":
            self.equipment.append("Dungeoneer's pack")
        else:
            self.equipment.append("Explorer's pack")
        swood = raw_input("Which weapon do you want? a 'shortbow' and a quiver of 20 arrows, or a 'shortsword'? ")
        if swood == "shortbow":
            self.equipment.append("Shortbow and a quiver of 20 arrows")
            self.weapon.append("Shortbow and a quiver of 20 arrows")
        else:
            self.equipment.append("Shortsword")
            self.weapon.append("Shortsword")
        weapon = raw_input("Which other weapon do you want? a 'shortsword' or a 'rapier'? ")
        if weapon == "shortsword":
            self.equipment.append("shortsword")
            self.weapon.append("shortsword")
        else:
            self.weapon.append("rapier")
            self.equipment.append("rapier")

    def set_expertise(self):
        pass

    def set_archetype(self):
        pass
