import math


class Wizard:
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

        self.tradition = ""
        self.tradition_desc = []

        self.feature = ["Ritual Casting", "Spellcasting Focus", "Arcane Recovery"]
        self.proficiency = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
        self.skill = []
        self.saving_throw = ["intelligence", "wisdom"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["spellbook"]
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

        self.magic = []
        self.magic_throw = "intelligence"
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
        self.spellbook_ct = 6
        self.spells = [self.lvl_one, self.lvl_two, self.lvl_three, self.lvl_four, self.lvl_five, self.lvl_six,
                       self.lvl_seven, self.lvl_eight, self.lvl_nine]
        self.spell_master = []
        self.sig_spells = []

        if self.level > 1:
            self.set_tradition()
        if self.level > 17:
            self.feature.append("Spell Mastery")
            print("Which level one spell do you want to master?")
            for x in range(0, self.lvl_one[0]):
                print x
            print("")
            choice = raw_input("")
            self.spell_master.append(choice)
            print("Which level two spell do you want to master?")
            for x in range(0, self.lvl_two[0]):
                print x
            print("")
            choice = raw_input("")
            self.spell_master.append(choice)
        if self.level > 19:
            self.feature.append("Signature Spells")
            for x in range(0, 2):
                print("Which level three spell do you want to be a signature spell? ")
                for y in range(0, self.lvl_three[0]):
                    print y
                print("")
                choice = raw_input("")
                self.sig_spells.append(choice)
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
                "Initialization: What skill do you want to be proficient in? Arcana, History, Insight, Investigation, Medicine, or Religion? Please input ")
            self.skill.append(skill)
            i += 1
        # V2: have potential skills in an array, pass that in to the inherited function, 'subtract' any already known

    def set_equip(self):
        pack = raw_input(
            "Which pack do you want? a 'explorer' pack, or 'scholar' pack? Please input. ")
        if pack == "explorer":
            self.equipment.append("Explorer's pack")
        else:
            self.equipment.append("Scholar's pack")
        arcana = raw_input("Do you want a component 'pouch' or an 'arcane' focus?")
        if arcana == "pouch":
            self.equipment.append("component pouch")
        else:
            self.equipment.append("an arcane focus")
        wpn = raw_input("Which do you want: a quarterstaff or a dagger?")
        self.weapon.append(wpn)
        self.equipment.append(wpn)

    def set_cantrip(self):
        self.cantrips[0] = 3
        self.cantrips[1].append(raw_input("Initialization: What two cleric cantrips do you want to add?"))
        if self.level > 3:
            self.cantrips[0] = 4
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))
        if self.level > 9:
            self.cantrips[0] = 5
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))

    def set_spells(self):
        self.spell_dc = 8 + self.proficiency_bonus + self.intelligence_mod()
        self.spell_attack = self.proficiency_bonus + self.intelligence_mod()
        self.lvl_one[0] = 6
        for i in range(0, self.spellbook_ct):
            self.lvl_one[1].append(raw_input("What level one spell do you want to learn?"))
        if self.level > 1:
            self.lvl_one[0] += 1
            self.lvl_one[1].append(raw_input("Level up: What other level one spell do you want to learn?"))
        if self.level > 2:
            self.lvl_one[0] += 1
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

    def set_tradition(self):
        circle = raw_input(
            "Level up: Which tradition do you want to join? artificer, bladeslinging, 'lore' master, abjuration, conjuration, "
            "divination, enchantment, evocation, illusion, invention, necromancy, transmutation, technomancy, theurgy, or 'war' magic?\n")
        if circle == "artificer":
            self.tradition = "Artificer"
            self.artifice()
        elif circle == "bladeslinging":
            self.tradition = "Bladeslinging"
            self.blade()
        elif circle == "lore":
            self.tradition = "Lore Mastery"
            self.lore()
        elif circle == "abjuration":
            self.tradition = "School of Abjuration"
            self.abjuration()
        elif circle == "conjuration":
            self.tradition = "School of Conjuration"
            self.conj()
        elif circle == "divination":
            self.tradition = "School of Divination"
            self.divin()
        elif circle == "enchantment":
            self.tradition = "School of Enchantment"
            self.ench()
        elif circle == "evocation":
            self.tradition = "School of Evocation"
            self.evoc()
        elif circle == "illusion":
            self.tradition = "School of Illusion"
            self.illusion()
        elif circle == "invention":
            self.tradition = "School of Invention"
            self.invent()
        elif circle == "necromancy":
            self.tradition = "School of Necromancy"
            self.necromancy()
        elif circle == "transmutation":
            self.tradition = "School of Transmutation"
            self.transmut()
        elif circle == "technomancy":
            self.tradition = "Technomancy"
            self.techno()
        elif circle == "theurgy":
            self.tradition = "Theurgy"
            self.theurgy()
        else:
            self.tradition = "War Magic"
            self.war()

    def theurgy(self):
        self.feature.append("Divine Inspiration")
        self.feature.append("Arcane Initiate")
        self.feature.append("Channel Arcana")
        if self.level > 5:
            self.feature.append("Arcane Acolyte")
        if self.level > 9:
            self.feature.append("Arcane Priest")
        if self.level > 13:
            self.feature.append("Arcane High Priest")

    def war(self):
        self.feature.append("Arcane Deflection")
        self.feature.append("Tactical Wit")
        if self.level > 5:
            self.feature.append("Power Surge")
        if self.level > 9:
            self.feature.append("Durable Magic")
        if self.level > 13:
            self.feature.append("Deflecting Shroud")

    def techno(self):
        self.proficiency.append(str(["sidearms", "hacking tools"]))
        self.feature.append("Technological Savant")
        if self.level > 5:
            self.feature.append("Program Spell")
        if self.level > 9:
            self.feature.append("Online Casting")
        if self.level > 13:
            self.feature.append("Chained Device")

    def transmut(self):
        self.feature.append("Transmutation Savant")
        self.feature.append("Minor Alchemy")
        if self.level > 5:
            self.feature.append("Transmuter's Stone")
        if self.level > 9:
            self.feature.append("Shapechanger")
            self.lvl_four[0] += 1
            self.lvl_four[1].append("Polymorph")
        if self.level > 13:
            self.feature.append("Master Transmuter")

    def necromancy(self):
        self.feature.append("Necromancy Savant")
        self.feature.append("Grim Harvest")
        if self.level > 5:
            self.feature.append("Undead Thralls")
            self.lvl_three[0] += 1
            self.lvl_three[1].append("Animate Dead")
        if self.level > 9:
            self.feature.append("Inured to Undeath")
            self.resistance.append("Necrotic Damage")
        if self.level > 13:
            self.feature.append("Command Undead")

    def invent(self):
        self.proficiency.append(raw_input("What two tools do you want to be proficient in? Please input. "))
        self.proficiency.append("light armor")
        self.equipment.append("Suit of Arcanomechanical Armor")
        self.armor = ["Arcanomechanical Armor", str(12 + self.dexterity_mod())]
        self.feature.append("Arcanomechanical Armor")
        self.feature.append("Reckless Casting")
        if self.level > 5:
            self.feature.append("Alchemical Casting")
        if self.level > 9:
            self.feature.append("Prodigious Inspiration")
        if self.level > 13:
            self.feature.append("Controlled Chaos")

    def illusion(self):
        self.feature.append("Illusion Savant")
        self.feature.append("Improved Minor Illusion")
        self.cantrips[0] += 1
        self.cantrips[1].append("Minor Illusion" if not self.cantrips[1] else raw_input("What cantrip do you want to learn"))
        if self.level > 5:
            self.feature.append("Malleable Illusions")
        if self.level > 9:
            self.feature.append("Illusory Self")
        if self.level > 13:
            self.feature.append("Illusory Reality")

    def evoc(self):
        self.feature.append("Evocation Savant")
        self.feature.append("Sculpt Spells")
        if self.level > 5:
            self.feature.append("Potent Cantrip")
        if self.level > 9:
            self.feature.append("Empowered Evocation")
        if self.level > 13:
            self.feature.append("Overchannel")

    def ench(self):
        self.feature.append("Enchantment Savant")
        self.feature.append("Hypnotic Gaze")
        if self.level > 5:
            self.feature.append("Instinctive Charm")
        if self.level > 9:
            self.feature.append("Split Enchantment")
        if self.level > 13:
            self.feature.append("Alter Memories")

    def divin(self):
        self.feature.append("Divination Savant")
        self.feature.append("Portent")
        if self.level > 5:
            self.feature.append("Expert Divination")
        if self.level > 9:
            self.feature.append("The Third Eye")
        if self.level > 13:
            self.feature.append("Greater Portent")

    def conj(self):
        self.feature.append("Conjuration Savant")
        self.feature.append("Minor Conjuration")
        if self.level > 5:
            self.feature.append("Benign Transposition")
        if self.level > 9:
            self.feature.append("Focused Conjuration")
        if self.level > 13:
            self.feature.append("Durable Summons")

    def abjuration(self):
        self.feature.append("Abjuration Savant")
        self.feature.append("Arcane Ward")
        if self.level > 5:
            self.feature.append("Projected Ward")
        if self.level > 9:
            self.feature.append("Improved Abjuration")
        if self.level > 13:
            self.resistance.append("Spell Damage: Spell Resistance")
            self.feature.append("Spell Resistance")

    def lore(self):
        self.feature.append("Lore Master")
        self.feature.append("Spell Secrets")
        if self.level > 5:
            self.feature.append("Alchemical Casting")
        if self.level > 9:
            self.feature.append("Prodigious Memory")
        if self.level > 13:
            self.feature.append("Master of Magic")

    def blade(self):
        self.proficiency.append("Light armor")
        self.proficiency.append(raw_input("What one-handed melee weapon do you want to be proficient in?"))
        self.skill.append("Performance")
        self.feature.append("Bladesong")
        if self.level > 5:
            self.feature.append("Extra Attack")
        if self.level > 9:
            self.feature.append("Song of Defense")
        if self.level > 13:
            self.feature.append("Song of Victory")

    def artifice(self):
        self.feature.append("Infuse Potions")
        self.feature.append("Infuse Scrolls")
        if self.level > 5:
            self.feature.append("Infuse Weapons and Armor")
        if self.level > 9:
            self.feature.append("Superior Artificer")
        if self.level > 13:
            self.feature.append("Master Artificer")

