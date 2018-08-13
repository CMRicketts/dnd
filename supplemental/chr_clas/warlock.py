import math


class Warlock:
    def __init__(self, level, stre, dex, con, cha, inte, wis):
        self.strength = int(stre)
        self.constitution = int(con)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.intelligence = int(inte)
        self.wisdom = int(wis)
        self.hp = 0
        self.hit_dice = ""

        self.patron = ""
        self.pact = ""
        self.pact_desc = []

        self.level = int(level)

        self.feature = []
        self.proficiency = ["light armor", "simple weapons"]
        self.skill = []
        self.saving_throw = ["wisdom", "charisma"]
        self.resistance = []
        self.language = []
        self.attack = []
        self.equipment = ["two daggers", "any simple weapon"]
        self.weapon = ["two daggers", "any simple weapon"]
        self.armor = ["leather armor", "11"]

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
        self.spell_slots = 0
        self.slot_lvl = 0
        self.invocation_ct = 0
        self.invocations = []
        self.spells = [self.lvl_one, self.lvl_two, self.lvl_three, self.lvl_four, self.lvl_five, self.lvl_six,
                       self.lvl_seven, self.lvl_eight, self.lvl_nine]

        if self.level > 1:
            self.set_pact()
        if self.level > 10:
            self.feature.append("Mystic Arcanum")
        if self.level > 19:
            self.feature.append("Eldritch Master")

        self.init_hit_die()
        self.set_skill()
        self.set_equip()
        self.set_patron()
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
        self.hit_dice = str(self.level) + "d8"

    def init_hp(self):
        self.hp = 8 + self.constitution_mod()

    def level_hp(self, level):
        self.hp = 8 + (self.constitution_mod() * int(level))

    def set_skill(self):
        i = 0
        while i < 2:
            skill = raw_input(
                "Initialization: What skill do you want to be proficient in? Arcana, Deception, History, Intimidation, Nature, or Religion? Please input ")
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
            "Which pack do you want? a 'dungeoneer' pack, or 'scholar' pack? Please input. ")
        if pack == "dungeoneer":
            self.equipment.append("Dungeoneer's pack")
        else:
            self.equipment.append("Scholar's pack")
        arcana = raw_input("Do you want a component 'pouch' or an 'arcane' focus?")
        if arcana == "pouch":
            self.equipment.append("component pouch")
        else:
            self.equipment.append("an arcane focus")

    def set_spells(self):
        self.cantrips[0] = 2
        self.spell_ct = 2
        if self.level > 3:
            self.cantrips[0] = 3
        elif self.level > 9:
            self.cantrips[0] = 4

        if 0 < self.level < 10:
            self.spell_ct = self.level + 1
        elif 9 < self.level:
            self.spell_ct = (int(math.ceil(self.level - 10)/2) + 10)
        if 0 < self.level < 9:
            self.slot_lvl = int(math.ceil(self.level / 2))
        elif self.level > 8:
            self.slot_lvl = 5
        if 1 < self.level < 11:
            self.spell_slots = 2
        elif self.level > 10:
            self.spell_slots = 3
        elif self.level > 16:
            self.spell_slots = 4
        if self.level == 1:
            self.invocation_ct = 2
        elif 2 < self.level < 11:
            self.invocation_ct = int(math.ceil(self.level / 2))
        elif self.level > 10:
            self.invocation_ct = 5
        elif self.level > 11:
            self.invocation_ct = 6
        elif self.level > 14:
            self.invocation_ct = 7
        elif self.level > 17:
            self.invocation_ct = 8

        for i in range(0, self.cantrips[0]):
            self.cantrips[1].append(raw_input("What warlock cantrip do you want to learn?"))
        for i in range(0, self.spell_ct):
            if self.slot_lvl == 1:
                self.lvl_one[0] += 1
                self.lvl_one[1].append(raw_input("What level one warlock spell do you want to learn?"))
            elif self.slot_lvl == 2:
                self.lvl_two[0] += 1
                self.lvl_two[1].append(raw_input("What level two warlock spell do you want to learn?"))
            elif self.slot_lvl == 3:
                self.lvl_three[0] += 1
                self.lvl_three[1].append(raw_input("What level three warlock spell do you want to learn?"))
            elif self.slot_lvl == 4:
                self.lvl_four[0] += 1
                self.lvl_four[1].append(raw_input("What level four warlock spell do you want to learn?"))
            elif self.slot_lvl == 5:
                self.lvl_five[0] += 1
                self.lvl_five[1].append(raw_input("Level Up: What level five warlock spell do you want to learn?"))
        for i in range(0, int(self.invocation_ct)):
            self.choose_inv()

    def choose_inv(self):
        base_inv = ["Armor of Shadows", "Beast Speech", "Beguiling Influence", "Devil's Sight", "Eyes of the Rune Keeper",
                    "Fiendish Vigor", "Gaze of Two Minds", "Mask of Many Faces", "Misty Visions", "Thief of Five Fates"]
        prereq_inv = []
        if self.level > 4:
            prereq_inv.append("Cloak of Flies")
            prereq_inv.append("Gift of the Depths")
            prereq_inv.append("Mire the Mind")
            prereq_inv.append("One with Shadows")
            prereq_inv.append("Sign of Ill Omen")
            prereq_inv.append("Tomb of Levistus")
        if self.level > 6:
            prereq_inv.append("Bewitching Whispers")
            prereq_inv.append("Dreadful Word")
            prereq_inv.append("Ghostly Gaze")
            prereq_inv.append("Sculptor of Flesh")
            prereq_inv.append("Trickster's Escape")
        if self.level > 8:
            prereq_inv.append("Ascendant Step")
            prereq_inv.append("Minions of Chaos")
            prereq_inv.append("Otherworldly Leap")
            prereq_inv.append("Whispers of the Grave")
        if self.level > 14:
            prereq_inv.append("Master of Myriad Forms")
            prereq_inv.append("Shroud of Shadow")
            prereq_inv.append("Visions od Distant Realms")
            prereq_inv.append("Witch Sight")
        if "eldritch blast" in self.cantrips[1]:
            prereq_inv.append("Agonizing Blast")
            prereq_inv.append("Eldritch Spear")
            prereq_inv.append("Grasp of Hadar")
            prereq_inv.append("Lance of Lethargy")
            prereq_inv.append("Repelling Blast")
            if self.level > 4 and self.patron == "Fiend":
                prereq_inv.append("Kiss of Mephistopheles")
            if self.patron == "Raven Queen":
                prereq_inv.append("Raven Queen's Blessing")
        if self.pact == "Pact of the Blade":
            prereq_inv.append("Arcane Gunslinger")
            prereq_inv.append("Improved Pact Bringer")
            if self.level > 4:
                prereq_inv.append("Eldritch Smite")
                prereq_inv.append("Thirsting Blade")
            if self.level > 8:
                prereq_inv.append("Superior Pact Weapon")
            if self.level > 11:
                prereq_inv.append("Lifedrinker")
            if self.level > 14:
                prereq_inv.append("Ultimate Pact Weapon")
            if self.patron == "Great Old One":
                prereq_inv.append("Claw of Acamar")
            if self.patron == "Hexblade":
                prereq_inv.append("Curse Bringer")
            if self.patron == "Fiend":
                prereq_inv.append("Mace of Dispater")
            if self.patron == "Archfey":
                prereq_inv.append("Moon Bow")
        if self.pact == "Pact of the Tome":
            prereq_inv.append("Aspect of the Moon")
            prereq_inv.append("Book of Ancient Secrets")
            if self.patron == "Raven Queen":
                prereq_inv.append("Chronicle of the Raven Queen")
        if self.pact == "Pact of the Chain":
            prereq_inv.append("Gift of the Ever-Living Ones")
            prereq_inv.append("Voice of the Chain Master")
            if self.level > 14:
                prereq_inv.append("Chains of Carceri")
        if self.patron == "Hexblade":
            prereq_inv.append("Burning Hex")
            prereq_inv.append("Chilling Hex")
        if self.patron == "Great Old One":
            prereq_inv.append("Caiphon's Beacon")
            if self.level > 6:
                prereq_inv.append("Gaze of Khirad")
            if self.level > 17:
                prereq_inv.append("Shroud of Ulban")
        if self.patron == "Fiend":
            prereq_inv.append("Cloak of Baalzebul")
        if self.patron == "Archfey":
            prereq_inv.append("Green Lord's Gift")
            prereq_inv.append("Sea Twins' Gift")
        if self.patron == "Seeker":
            prereq_inv.append("Path of the Seeker")
            prereq_inv.append("Seeker's Speech")
        if self.level > 6 and (any("hex" in feat for feat in self.feature) or any("hex" in spell for spell in self.magic)):
            prereq_inv.append("Relentless Hex")

        base = set(base_inv)
        pre = set(prereq_inv)
        invs = set(self.invocations)
        inv_set = (base.union(pre)) - invs
        inv = list(inv_set)
        print("Which invocation do you want to learn? All invocations you can learn are listed below.")
        for item in inv:
            print(item)
        print("")
        choice = raw_input("")
        self.invocations.append(choice)

    def set_pact(self):
        pact = raw_input("Which pact to do you want to join? Pact of the 'chain', Pact of the 'blade', or pact of the 'tome'? ")
        if pact == "chain":
            self.pact = "Pact of the Chain"
            self.pact_desc.append("You learn the Find Familiar spell and can cast it as a ritual. The spell doesn't count against your number of spells known. When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit or sprite. Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to make one attack of its own with its reaction.")
            self.lvl_one[0] += 1
            self.lvl_one[1].append("Find Familiar")
        elif pact == "tome":
            self.pact = "Pact of the Tome"
            self.pact_desc.append("Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list (the three needn't be from the same list). While the book is on your person, you can cast those cantrips at will. They don't count against your number of cantrips known. If they don't appear on the warlock spell list, they are nonetheless warlock spells for you. If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.")
            i = 0
            while i < 3:
                self.cantrips[0] += 1
                self.cantrips[1].append(raw_input("Pact of the Tome: What cantrip do you want to learn? "))
        else:
            self.pact = "Pact of the Blade"
            self.pact_desc.append("You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to non-magical attacks and damage. Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.\nYou can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extra-dimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extra-dimensional space when the bond breaks.")

    def set_patron(self):
        arch = raw_input(
            "Level up: Which patron do you want to join? the 'archfey', celestial, fiend, 'ghost' in the (shell) machine, 'great' old one, 'hexblade', 'raven' queen, 'seeker', or 'undying'? ")
        if arch == "archfey":
            self.patron = "Archfey"
            self.archfey()
        elif arch == "celestial":
            self.patron = "Celestial"
            self.celeste()
        elif arch == "fiend":
            self.patron = "Fiend"
            self.fiend()
        elif arch == "ghost":
            self.patron = "Ghost in the Machine"
            self.ghost()
        elif arch == "great":
            self.patron = "Great Old One"
            self.goo()
        elif arch == "hexblade":
            self.patron = "Hexblade"
            self.hex()
        elif arch == "raven":
            self.patron = "Raven Queen"
            self.raven()
        elif arch == "seeker":
            self.patron = "Seeker"
            self.seeker()
        else:
            self.patron = "Undying"
            self.undyne()  # if you find this, you're rad.

    def undyne(self):
        self.feature.append("Expanded Spell List (undying)")
        self.cantrips[0] += 1
        self.cantrips[1].append("Spare the dying")
        self.feature.append("Among the Dead")
        if self.level > 5:
            self.feature.append("Defy Death")
        if self.level > 9:
            self.feature.append("Undying Nature")
        if self.level > 13:
            self.feature.append("Indestructible Life")

    def seeker(self):
        self.feature.append("Expanded Spell List (seeker)")
        self.feature.append("Shielding Aurora")
        if self.level > 2:
            self.feature.append("Pact of the Star Chain")
        if self.level > 5:
            self.feature.append("Astral Refuge")
        if self.level > 9:
            self.resistance.append(str(["fire damage", "cold damage"]))
            self.feature.append("Far Wanderer")
        if self.level > 13:
            self.feature.append("Astral Sequestration")

    def raven(self):
        self.feature.append("Expanded Spell List (raven)")
        self.feature.append("Sentinel Raven")
        if self.level > 5:
            self.feature.append("Soul of the Raven")
        if self.level > 9:
            self.resistance.append("necrotic damage")
            self.resistance.append("immunity to being frightened")
            self.proficiency.append("death saving throws")
            self.feature.append("Raven's Shield")
        if self.level > 13:
            self.feature.append("Queen's Right Hand")

    def hex(self):
        self.feature.append("Expanded Spell List (hexblade)")
        self.proficiency.append(str(["medium armor", "shields", "martial weapons"]))
        self.feature.append("Hex Warrior")
        self.feature.append("Hexblade's Curse")
        if self.level > 5:
            self.feature.append("Accursed Specter")
        if self.level > 9:
            self.feature.append("Armor of Hexes")
        if self.level > 13:
            self.feature.append("Master of Hexes")

    def goo(self):
        self.feature.append("Expanded Spell List (great old one)")
        self.feature.append("Awakened Mind")
        if self.level > 5:
            self.feature.append("Entropic Ward")
        if self.level > 9:
            self.resistance.append("psychic damage")
            self.feature.append("Thought Shield")
        if self.level > 13:
            self.feature.append("Create Thrall")

    def ghost(self):
        self.feature.append("Expanded Spell List (ghost)")
        self.cantrips[0] += 1
        self.cantrips[1].append("On/Off")
        self.proficiency.append("Hacking Tools")
        self.feature.append("Information Surge")
        if self.level > 5:
            self.feature.append("Wire Walk")
        if self.level > 9:
            self.feature.append("Personal Encryption")
        if self.level > 13:
            self.feature.append("Technovirus")

    def fiend(self):
        self.feature.append("Expanded Spell List (fiend)")
        self.feature.append("Dark One's Blessing")
        if self.level > 5:
            self.feature.append("Dark One's Own Luck")
        if self.level > 9:
            self.feature.append("Fiendish Resilience")
        if self.level > 13:
            self.feature.append("Hurl Through Hell")

    def celeste(self):
        self.feature.append("Expanded Spell List (celestial)")
        self.cantrips[0] += 2
        self.cantrips[1].append(str(["sacred flame", "light"]))
        self.feature.append("Healing Light")
        if self.level > 5:
            self.resistance.append("radiant damage")
            self.feature.append("Radiant Soul")
        if self.level > 9:
            self.feature.append("Celestial Resilience")
        if self.level > 13:
            self.feature.append("Searing Vengeance")

    def archfey(self):
        self.feature.append("Expanded Spell List (archfey)")
        self.feature.append("Fey Presence")
        if self.level > 5:
            self.feature.append("Misty Escape")
        if self.level > 9:
            self.feature.append("Beguiling Defenses")
            self.resistance.append("immunity to being charmed")
        if self.level > 13:
            self.feature.append("Dark Delirium")
