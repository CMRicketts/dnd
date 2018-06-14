import math


class Druid():
    def __init__(self, level, stre, dex, wis, inte, cha, con):
        self.strength = int(stre)
        self.constitution = int(con)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.intelligence = int(inte)
        self.wisdom = int(wis)
        self.hp = 0
        self.hit_dice = ""

        self.level = int(level)

        self.circle = ""
        self.circle_desc = []

        self.feature = ["Ritual Casting", "Spellcasting Focus (Druid)"]
        self.proficiency = ["light armor", "medium armor", "shields", "clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles", "slings", "spears", "herbalism kit"]
        self.skill = []
        self.saving_throw = ["intelligence", "wisdom"]
        self.resistance = []
        self.language = ["Druidic"]

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
        self.equipment = ["explorer's pack", "druidic focus"]
        self.weapon = []
        self.armor = ["Leather Armor", "11"]

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
            
        self.set_skill()
        self.set_equip()
        self.set_dc()
        self.set_mg_attack()
        self.set_cantrip()
        self.set_spells()
        
        if self.level > 1:
            self.feature.append("Wild Shape")
        if self.level > 17:
            self.feature.append("Timeless Body")
            self.feature.append("Beast Spells")
        if self.level > 19:
            self.feature.append("Archdruid")

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
        
    def set_equip(self):
        weapon_one = raw_input("Initialization: Which do you want, a wooden shield, or any simple weapon? Please input ")
        if weapon_one != "wooden shield":
            self.equipment.append(weapon_one)
        else: 
            self.equipment.append("wooden shield")
        weapon_two = raw_input("Initialization: Which do you want, a scimitar, or any simple melee weapon? Please input ")
        if weapon_two != "scimitar":
            self.equipment.append(weapon_two)
        else: 
            self.equipment.append(weapon_two)
        self.weapon.append([weapon_one, weapon_two])
        
    def set_skill(self):
        i = 0
        while i < 2:
            skill = raw_input("Initialization: What skill do you want to be proficient in? Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, or Survival? Please input ")
            self.skill.append(skill)
            i += 1
    
    def set_cantrip(self):
        self.cantrips[0] = 2
        self.cantrips[1].append(raw_input("Initialization: What two cleric cantrips do you want to add?"))
        if self.level > 3:
            self.cantrips[0] = 3
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))
        if self.level > 9:
            self.cantrips[0] = 4
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

    def set_circle(self):
        circle = raw_input("Level up: Which circle do you want to join? dreams, land, moon, shepherd, spores, or twilight?")
        if circle == "dreams":
            self.circle = "Circle of Dreams"
            self.dream()
        elif circle == "land":
            self.circle = "Circle of the Land"
            self.land()
        elif circle == "moon":
            self.circle = "Circle of the Moon"
            self.moon()
        elif circle == "shepherd":
            self.circle = "Circle of the Shepherd"
            self.shepherd()
        elif circle == "spores":
            self.circle = "Circle of Spores"
            self.spore()
        else:
            self.circle = "Circle of Twilight"
            self.twilight()

    def twilight(self):
        pass

    def spore(self):
        pass

    def shepherd(self):
        pass

    def land(self):
        pass

    def moon(self):
        pass

    def dream(self):
        self.feature.append("Balm of the Summer Court")
        pass
