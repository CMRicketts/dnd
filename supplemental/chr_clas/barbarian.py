import math


class Barbarian:

    def __init__(self, level, race, stre, dex, con, cha, inte, wis):

        self.feature = ["Rage", "Unarmored Defense"]
        self.proficiency = ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"]
        self.saving_throw = ["strength", "constitution"]
        self.resistance = []
        self.skill = []
        self.equipment = []
        self.weapon = []
        self.path = ""

        self.rage_description = []

        self.level = int(level)
        level = self.level
        self.strength = int(stre)
        self.wisdom = int(wis)
        self.intelligence = int(inte)
        self.dexterity = int(dex)
        self.charisma = int(cha)
        self.constitution = int(con)
        self.hit_dice = ""

        self.hp = 0

        self.swim_speed = 0

        self.attack = []
        self.archetype = ""

        self.proficiency_bonus = 2
        if level > 4:
            self.proficiency_bonus = 3
        if level > 8:
            self.proficiency_bonus = 4
        if level > 12:
            self.proficiency_bonus = 5
        if level > 16:
            self.proficiency_bonus = 6

        if level > 1:
            self.feature.append(["Reckless Attack", "Danger Sense"])
            self.proficiency.append("Dexterity saving throws against effects you can see")

        if level > 2 and self.path == "":
            path = raw_input("what path do you want to take? "
                             "cannibal, ancestor, berserker, storm, totem, or zealot?")
            if race == "dwarf":
                str(path) + " or battlerager (dwarf only)?"
            if path == "cannibal":
                self.archetype = "Cannibal"
                self.path = self.cannibal(level)
            if path == "ancestor":
                self.archetype = "Ancestor"
                self.path = self.ancestor(level)
            if path == "battlerager":
                self.archetype = "Battlerager"
                self.path = self.battlerager(level)
            if path == "beserker":
                self.archetype = "Beserker"
                self.path = self.beserker(level)
            if path == "storm":
                self.archetype = "Storm"
                self.path = self.storm(level)
            if path == "totem":
                self.archetype = "Totem"
                self.path = self.totem(level)
            if path == "zealot":
                self.archetype = "Zealot"
                self.path = self.zealot(level)

        if level > 4:
            self.feature.append("Extra attack")
            self.feature.append("Fast movement")

        if level > 6:
            self.proficiency.append("initiative rolls (feral instinct)")

        if level > 8:
            self.brutal_crit(level)

        if level > 10:
            self.rage_description.append("Relentless Rage")

        if level > 14:
            self.rage_description.append("Persistant Rage")

        if level > 17:
            self.feature.append("Indomitable Might")

        if level == 20:
            self.feature.append("Primal Champion")
            self.strength = self.strength + 4
            self.constitution = self.constitution + 4

        if level > 3:
            self.ability()
        if level > 7:
            self.ability()
        if level > 11:
            self.ability()
        if level > 15:
            self.ability()
        if level > 18:
            self.ability()

        self.rage_count = 2
        if level > 2:
            self.rage_count = 3
        if level > 5:
            self.rage_count = 4
        if level > 11:
            self.rage_count = 5
        if level > 16:
            self.rage_count = 6
        if level > 19:
            self.rage_count = 999

        self.rage_dmg = 2
        if level > 8:
            self.rage_dmg = 3
        if level > 15:
            self.rage_dmg = 4

        self.equipments()
        self.skills()
        self.init_hit_die()

        if level == 1:
            self.init_hp()
        else:
            self.level_hp(level)

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

    def init_hit_die(self):
        self.hit_dice = str(self.level) + "d12"

    def init_hp(self):
        self.hp = 12 + self.constitution_mod()

    def level_hp(self, level):
        self.hp = 12 + (self.constitution_mod() * int(level))

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

    def skills(self):
        i = 0
        while i < 2:
            choice = raw_input(
                "which skill do you want to increase? animal handling, athletics, intimidation, nature, perception, or survival")
            self.skill.append(choice)
            i += 1

    def equipments(self):
        weapon = raw_input("which weapon do you want? greataxe, or any other martial melee weapon (input please)")
        self.equipment.append(weapon)
        self.weapon.append(weapon)
        other = raw_input("which other weapon do you want? two handaxes, or any other simple weapon (input please)?")
        self.equipment.append(other)
        self.weapon.append(other)
        self.equipment.append("explorer's pack")
        self.equipment.append("javelin x4")
        self.weapon.append("javelin x4")

    def brutal_crit(self, level):
        beg = "you can roll "
        dice = "one "
        if level > 12:
            dice = "two "
        if level > 16:
            dice = "three "
        end = "additional weapon damage die when determining the extra damage for a critical hit with a melee attack."
        self.feature.append(beg + dice + end)

    def cannibal(self, level):

        def biting():
            dmg = "1d4 + " + str(self.strength)
            save = "wisdom"
            dc = "16"
            description = "At 6th level, while in rage you can make a bite attack" \
                          " as a reaction when struck in melee by an opponent." \
                          " This attack deals 1d4 + Strength modifier damage, " \
                          "and on a hit the opponent must succeed on a wisdom save DC 16 or be frightened," \
                          " they may retest at the beginning of their next turn to overcome the frightened condition."
            bite = {
                dmg,
                save,
                dc,
                description
            }
            self.attack.append(str(bite))
            return bite

        self.rage_description.append("All Consuming Rage")

        if level > 5:
            self.attack.append("Biting Rebuke")
            biting()
        if level > 9:
            self.feature.append("Heart of Enemies")
        if level > 13:
            self.feature.append("Spirit of the Slain")

        return "cannibal"

    def ancestor(self, level):

        self.rage_description.append("Ancestral Protectors")

        if level > 5:
            self.rage_description.append("Spirit Shield")
        if level > 9:
            self.feature.append("Consult the Spirit")
        if level > 13:
            self.feature.append("Vengeful Ancestors")

        return "ancestral guardian"

    def battlerager(self, level):

        self.feature.append("Battlerager Armor")

        if level > 5:
            self.feature.append("Reckless Abandon")
        if level > 9:
            self.feature.append("Battlerager Charge")
        if level > 13:
            self.feature.append("Spiked Retribution")

        return "battlerager"

    def beserker(self, level):
        def mindless():
            self.resistance.append(["charm (while raging)", "frighten (while raging)"])

        self.feature.append("Frenzy")
        if level > 5:
            mindless()
        if level > 9:
            self.feature.append("Intimidating Presence")
        if level > 13:
            self.feature.append("Retaliation")

        return "beserker"

    def storm(self, level):
        element = raw_input("which aura do you want to have? desert, sea, or tundra?")

        def aura():
            end = ""
            beginning = "Starting at 3rd level, you emanate a stormy, magical aura while you rage. The aura extends " \
                        "10 feet from you in every direction, but not through total cover. Your aura has an effect " \
                        "that activates when you enter your rage, and you can activate the effect again on each of " \
                        "your turns as a bonus action. Choose desert, sea, or tundra. Your aura's effect depends on " \
                        "that chosen environment, as detailed below. You can change your environment choice whenever " \
                        "you gain a level in this cla. Your aura's effects require a saving throw, the DC equals "
            dc = 8 + self.proficiency_bonus + self.constitution
            if element == "desert":
                end = "When this effect is activated, all other creatures in your aura take 2 fire damage each. The " \
                      "damage increases when you reach certain levels in this class, increasing to 3 at 5th level, " \
                      "4 at 10th level, 5 at 15th level, and 6 at 20th level. "
            if element == "sea":
                end = "When this effect is activated, you can choose one other creature you can see in your aura. The " \
                      "target must make a Dexterity saving throw. The target takes 1d6 lightning damage on a failed " \
                      "save, or half as much damage on a successful one. The damage increases when you reach certain " \
                      "levels in this class, increasing to 2d6 at 10th level, 3d6 at 15th level, and 4d6 at 20th " \
                      "level. "
            if element == "tundra":
                end = "When this effect is activated, each creature of your choice in your aura gains 2 temporary hit " \
                      "points, as icy spirits inure it to suffering. The temporary hit points increase when you reach " \
                      "certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, " \
                      "and 6 at 20th level. "
            return beginning + str(dc) + end

        def soul():
            if element == "desert":
                self.resistance.append("fire")
                self.feature.append("As an action, you can touch a flammable object that isn't being worn or carried "
                                    "by anyone else and set it on fire.")
            if element == "sea":
                self.resistance.append("lightning")
                self.feature.append("underwater breathing")
                self.swim_speed = 30
            if element == "tundra":
                self.resistance.append("cold")
                self.feature.append("as an action, you can touch water and turn a 5-foot cube Of it into ice, "
                                    "which melts after 1 minute. This action fails if a creature is in the cube.")

        def shield():
            return "you learn to use your mastery of the storm to protect others. Each creature of your choice has " \
                   "the damage resistance you gained from the Storm Soul feature while the creature is in your Storm " \
                   "Aura."

        def raging_storm():
            if element == "desert":
                self.feature.append("Immediately after a creature in your aura hits you with an attack, you can use "
                                    "your reaction to force that creature to make a Dexterity saving throw. On a "
                                    "failed save, the creature takes fire damage equal to half your barbarian level.")
            if element == "sea":
                self.feature.append("When you hit a creature in your aura with an attack, you can use your reaction "
                                    "to force that creature to make a Strength saving throw. On a failed save, "
                                    "the creature is knocked prone, as if struck by a wave.")
            if element == "tundra":
                self.feature.append("Whenever the effect of your Storm Aura is activated, you can choose one creature "
                                    "you can see in the aura. That creature must succeed on a Strength saving throw, "
                                    "or its speed is reduced to 0 until the start of your next turn, as magical frost "
                                    "covers it.")

        self.feature.append(aura())
        if level > 5:
            soul()
        if level > 9:
            self.feature.append(shield())
        if level > 13:
            raging_storm()

        return "Storm Herald"

    def totem(self, level):

        def spirit():
            animal = raw_input("which totem spirit do you want for the first level? bear, eagle, wolf, elk, or tiger?")
            if animal == "bear":
                self.resistance.append("all damage except psychic (during rage) (bear totem)")
            if animal == "eagle":
                self.feature.append("While you're raging and aren't wearing heavy armor, other creatures have "
                                    "disadvantage on opportunity attack rolls against you, and you can use the Dash "
                                    "action as a bonus action on your turn. The spirit of the eagle makes you into a "
                                    "predator who can weave through the fray with ease.")
            if animal == "wolf":
                self.feature.append("While you're raging, your friends have advantage on melee attack rolls against "
                                    "any creature within 5 feet of you that is hostile to you. ")
            if animal == "elk":
                self.feature.append("While you're raging and aren't wearing heavy armor, your walking speed increases "
                                    "by 15 feet.")
            if animal == "tiger":
                self.feature.append("While raging, you can add 10 feet to your long jump distance and 3 feet to your "
                                    "high jump distance.")

        def aspect():
            animal = raw_input("which totem spirit do you want for the second level? You can choose the same if you'd "
                               "like. bear, eagle, wolf, elk, or tiger")
            if animal == "bear":
                self.feature.append("Your carrying capacity (including maximum load and maximum lift) is doubled, "
                                    "and you have advantage on Strength checks made to push, pull, lift, "
                                    "or break objects.")
            if animal == "eagle":
                self.feature.append("You can see up to 1 mile away with no difficulty, able to discern even fine "
                                    "details as though looking at something no more than 100 feet away from you. "
                                    "Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) "
                                    "checks.")
            if animal == "wolf":
                self.feature.append("You can track other creatures while traveling at a fast pace, and you can move "
                                    "stealthily while traveling at a normal pace")
            if animal == "elk":
                self.feature.append("Whether mounted or on foot, your travel pace is doubled, as is the pace of up to "
                                    "ten companions while they're within 60 feet of you and your aren't "
                                    "incapacitated.")
            if animal == "tiger":
                prof = raw_input("which first skill do you want to be proficient in? athletics, acrobatics, stealth, "
                                 "or survival?")
                prof_two = raw_input("which second skill, different from the first, do you want to be proficient in? "
                                     "athletics, acrobatics, stealth, or survival?")
                self.skill.append(prof)
                self.skill.append(prof_two)

        def walker():
            self.feature.append("you can cast the commune with nature spell, but only as a ritual. When you do so, "
                                "a spiritual version of one of the animals you chose for Totem Spirit or Aspect of "
                                "the Beast appears to you to convey the information you seek.")

        def attune():
            animal = raw_input("which animal do you want to have attributes of? you can choose the same one as before. "
                               "bear, eagle, wolf, elk, or tiger")
            if animal == "bear":
                self.feature.append("While you're raging, any creature within 5 feet of you that's hostile to you has "
                                    "disadvantage on attack rolls against targets other than you or another character "
                                    "with this feature. An enemy is immune to this effect if it can't see or hear you "
                                    "or if it can't be frightened.")
            if animal == "eagle":
                self.feature.append("While raging, you have a flying speed equal to your current walking speed. This "
                                    "benefit works only in short bursts; you fall if you end your turn in the air and "
                                    "nothing else is holding you aloft.")
            if animal == "wolf":
                self.feature.append("While you're raging, you can use a bonus action on your turn to knock a Large or "
                                    "smaller creature prone when you hit it with melee weapon attack.")
            if animal == "elk":
                beg = 'While raging, you can use a bonus action during your move to pass through the space of a Large ' \
                      'of smaller creature. That creature must succeed on a Strength saving throw '
                dc = 8 + self.strength + self.proficiency_bonus
                end = "or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier."
                self.feature.append(beg + " DC: " + str(dc) + end)
            if animal == "tiger":
                self.feature.append("While you're raging, if you move at least 20 feet in a straight line toward a "
                                    "Large or smaller target right before making a melee weapon attack against it, "
                                    "you can use a bonus action to make an additional melee weapon attack against it.")

        spirit()
        if level > 6:
            aspect()
        if level > 9:
            walker()
        if level > 13:
            attune()

        return "totem warrior"

    def zealot(self, level):

        self.feature.append("Divine Fury")
        self.feature.append("Warrior of the Gods")
        if level > 5:
            self.feature.append("Fanatical Focus")
        if level > 9:
            self.feature.append("Zealous Presence")
        if level > 13:
            self.feature.append("Rage Beyond Death")

        return "zealot"
