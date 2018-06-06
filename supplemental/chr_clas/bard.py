import math


class Bard:
    def __init__(self, level, stre, dex, con, cha, inte, wis):
        self.level = int(level)
        self.strength = int(stre)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.constitution = int(con)
        self.intelligence = int(inte)
        self.wisdom = int(wis)
        self.hp = 0
        self.hit_dice = ""

        self.feature = ["Ritual Casting", "Spellcasting Focus", "Bardic Inspiration"]
        self.proficiency = ["light armor", "simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"]
        self.skill = []
        self.saving_throw = ["dexterity", "charisma"]

        self.college = ""

        self.magic = []
        self.magic_throw = "charisma"
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
        self.spells = [self.cantrips, self.lvl_one, self.lvl_two, self.lvl_three, self.lvl_four, self.lvl_five, self.lvl_six,
                       self.lvl_seven, self.lvl_eight, self.lvl_nine]

        self.jack_bonus = 1 # see jack of all trades feature
        self.proficiency_bonus = 2
        if self.level > 4:
            self.proficiency_bonus = 3
        if self.level > 8:
            self.jack_bonus = 2
            self.proficiency_bonus = 4
        if self.level > 12:
            self.proficiency_bonus = 5
        if self.level > 16:
            self.jack_bonus = 3
            self.proficiency_bonus = 6

        self.attack = []
        self.equipment = []
        self.weapon = []
        self.armor = []

        self.skills()
        self.music()
        self.equip()
        self.cantrip()
        self.set_spells()
        self.init_hit_die()

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
            self.feature.append("Jack of all Trades")
            self.feature.append("Song of Rest")
        if self.level > 2:
            self.set_college()
            self.feature.append("Expertise")
            good_skill = raw_input("What first skill do you want to double the proficiency bonus?")
            good_two = raw_input("What second skill do you want to double the proficiency bonus?")
            self.proficiency.append([good_skill, good_two, "doubled"])
        if self.level > 4:
            self.feature.append("Font of Inspiration")
        if self.level > 5:
            self.feature.append("Countercharm")
        if self.level > 9:
            self.feature.append("Magical Secrets")
            good_skill = raw_input("What first skill do you want to double the proficiency bonus?")
            good_two = raw_input("What second skill do you want to double the proficiency bonus?")
            self.proficiency.append([good_skill, good_two, "doubled"])
        if self.level > 13:
            self.feature.append("Magical Secrets x2")
        if self.level > 17:
            self.feature.append("Magical Secrets x3")
        if self.level > 19:
            self.feature.append("Superior Inspiration")

        if self.level == 1:
            self.init_hp()
        else:
            self.level_hp(self.level)

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

    def skills(self):
        i = 0
        while i < 3:
            self.skill.append(raw_input("Initialization: what skill do you want to be proficient in?"))
            i += 1

    def music(self):
        i = 0
        while i < 3:
            inst = raw_input("Initialization: what instrument do you want to be proficient in?")
            self.equipment.append(inst)
            self.proficiency.append(inst)
            i += 1

    def equip(self):
        item = raw_input("do you want a rapier, a longsword, or any simple weapon?")
        self.weapon.append(item)
        pack = raw_input("what pack do you want? Diplomat's pack or Entertainer's pack?")
        self.equipment.append(pack)
        music = raw_input("what extra instrument do you want to be proficient in?")
        self.equipment.append(music)
        self.equipment.append("dagger")
        self.armor.append(["leather armor", "11"])

    def cantrip(self):
        self.cantrips[0] = 2
        self.cantrips[1].append(raw_input("What two cantrips do you want to add?"))
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

    def set_dc(self):
        self.spell_dc = 8 + self.proficiency_bonus + self.charisma_mod()

    def set_mg_attack(self):
        self.spell_attack = self.proficiency_bonus + self.charisma_mod()

    def set_college(self):
        college = raw_input("What college do you want to enter? glamour, lore, satire, swords, valor, or whispers?")
        if college == "glamour":
            self.college = "College of Glamour"
            self.glamour()
        if college == "lore":
            self.college = "College of Lore"
            self.lore()
        if college == "satire":
            self.college = "College of Satire"
            self.satire()
        if college == "swords":
            self.college = "College of Swords"
            self.sword()
        if college == "valor":
            self.college = "College of Valor"
            self.valor()
        if college == "whispers":
            self.college = "College of Whisphers"
            self.whisper()

    def glamour(self):
        self.feature.append("Mantle of Inspiration")
        self.feature.append("Enthralling Performance")
        if self.level > 5:
            self.feature.append("Mantle of Majesty")
        if self.level > 13:
            self.feature.append("Unbreakable Majesty")
            self.magic_throw += "charisma"
        return "glamour"

    def lore(self):
        skill_one = raw_input("College of Lore: What skill do you want to be proficient in?")
        skill_two = raw_input("College of Lore: What other skill do you want to be proficient in?")
        skill_three = raw_input("College of Lore: What final skill do you want to be proficient in?")
        self.skill.append(str([skill_one, skill_two, skill_three]))
        self.feature.append("Cutting Words")
        if self.level > 5:
            self.feature.append("Additional Magic Secrets")
            spell_one = raw_input("Level up: What spell do you want to learn (up to level three?")
            spell_two = raw_input("Level up: What other spell do you want to learn (up to level three)?")
            self.magic.append(str([spell_one, spell_two]))
        if self.level > 13:
            self.feature.append("Peerless Skill")
        return "lore"

    def satire(self):
        self.proficiency.append("Thieves' Tools")
        self.skill.append("Sleight of Hand")
        skill = raw_input("College of Satire: What skill do you want to be proficient in?")
        self.skill.append(skill)
        self.feature.append("Tumbling Fool")
        if self.level > 5:
            self.lvl_two[0] += 1
            self.lvl_two[1].append("Detect Thoughts")
            self.feature.append("Fool's Insight")
        if self.level > 13:
            self.feature.append("Fool's Luck")
        return "satire"

    def sword(self):
        self.proficiency.append("Medium Armor")
        self.proficiency.append("Scimitar")
        style = raw_input("College of Swords: Which fighting style do you want to take? 'dueling' or 'two weapon' fighting?")
        if style == "dueling":
            self.feature.append("Dueling (Bard)")
        if style == "two weapon":
            self.feature.append("Two-Weapon Fighting (Bard)")
        self.feature.append("Blade Flourish")
        if self.level > 5:
            self.feature.append("Extra Attack")
        if self.level > 13:
            self.feature.append("Master's Flourish")
        return "sword"

    def valor(self):
        self.proficiency.append("medium armor")
        self.proficiency.append("shields")
        self.proficiency.append("martial weapons")
        self.feature.append("Combat Inspiration")
        if self.level > 5:
            self.feature.append("Extra Attack")
        if self.level > 13:
            self.feature.append("Battle Magic")
        return "valor"

    def whisper(self):
        self.feature.append("Psychic Blades")
        self.feature.append("Words of Terror")
        if self.level > 5:
            self.feature.append("Mantle of Whispers")
        if self.level > 13:
            self.feature.append("Shadow Lore")
        return "whisper"