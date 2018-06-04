import math


class Barbarian:

    def __init__(self, level, race):

        self.feature = [self.rage_details(), self.unarmored()]
        self.proficiency = []
        self.resistance = []
        self.path = ""

        self.proficiency_bonus = 2
        if (level > 4):
            self.proficiency_bonus = 3
        if (level > 8):
            self.proficiency_bonus = 4
        if (level > 12):
            self.proficiency_bonus = 5
        if (level > 16):
            self.proficiency_bonus = 6

        if level > 1 and not self.feature.__contains__(self.reckless()):
            self.feature.append([self.reckless(), self.danger_sense()])
            self.proficiency.append("Dexterity saving throws against effects you can see")

        if level > 2 and self.path == "":
            path = input("what path do you want to take? "
                         "cannibal, ancestor, berserker, storm, totem, or zealot?")
            if race == "dwarf":
                str(path) + " or battlerager (dwarf only)?"
            if path == "cannibal":
                self.path = self.cannibal(level)
            if path == "ancestor":
                self.path = self.ancestor(level)
            if path == "battlerager":
                self.path = self.battlerager(level)
            if path == "beserker":
                self.path = self.beserker(level)
            if path == "storm":
                self.path = self.storm(level)
            if path == "totem":
                self.path = self.totem(level)
            if path == "zealot":
                self.path = self.zealot(level)

        self.rage_count = 0
        self.rage_dmg = 0
        self.rage_description = []

        self.strength = 0
        self.wisdom = 0
        self.intelligence = 0
        self.dexterity = 0
        self.charisma = 0
        self.constitution = 0

        self.swim_speed = 0

        self.attack = []

        self.rage(level)

    def rage(self, level):

        return "rage"

    def rage_details(self):
        return "in battle, you fight with a primal ferocity. On your turn, you can enter a rage as a bonus action. " \
               "While raging, you gain the following benefits, as long as you aren't wearing heavy armor." \
               "\n\tYou have advantage on Strength check and Strength saves." \
               "\n\tWhen you make a melee weapon attack using Strength, you gain a +2 to the damage roll. This bonus " \
               "increase to +3 at 9th level, and +4 at 16th level." \
               "\n\tYou have resistance to bludgeoning, piercing, and physical damage." \
               "\nIf you can cast spells, you can't cast them or concentrate on them while raging." \
               "\nYour rage lasts 1 minute. It ends early if you are knocked unconscious " \
               "or if your turn ends without you having attacked a hostile creature or taken any damage since your " \
               "last turn. " \
               "You can also end your rage on your turn as a bonus action." \
               "\nOnce you have raged a number of time shown for your barbarian level on the table above," \
               " you must finish a long rest before you can rage again."

    def unarmored(self):
        return "When you aren't wearing any armor, " \
               "your Armor Class is 10 + your Dexterity modifier + your Constitution modifier. " \
               "You can use a shield and still gain this benefit."

    def reckless(self):
        return "At 2nd level, you can throw aside all concern for defense to attack with fierce desperation. " \
               "When you make your first attack on your turn, you can decide to attack recklessly. " \
               "Doing so gives you advantage on melee weapon attack rolls using Strength during this turn," \
               " but attack rolls against you have advantage until your next turn."

    def danger_sense(self):
        return "You have advantage on Dexterity saving throws against effects that you can see," \
               " such as traps and spells. " \
               "To gain this benefit, you can't be blinded, deafened, or incapacitated."

    def cannibal(self, level):

        def all_consuming():
            return "Starting at 3rd level, during rage, when you reduce a hostile opponent to 0 hit points," \
                   " you gain temporary hit points equal your Constitution modifier + your barbarian level " \
                   "(minimum of 1)."

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
            return bite

        def heart():
            return "by consuming a heart of a humanoid you have participated in slaying within the past hour," \
                   " you regain your full hit points as if finishing a long rest. " \
                   "You must finish a long rest to regain use of this feature."

        def spirit():
            return "At 14th level, by channeling the spirits of those you have eaten," \
                   " you have advantage on your next attack. " \
                   "You can only do this a number of times each day equal to your proficiency bonus, " \
                   "and only once per turn."

        self.rage_description.append(all_consuming())

        if level > 5:
            self.attack.append(biting())
        if level > 9:
            self.feature.append(heart())
        if level > 13:
            self.feature.append(spirit())

        return "cannibal"

    def ancestor(self, level):

        def protector():
            return "Starting when you choose this path at 3rd level, " \
                   "spectral warriors appear when you enter your rage. " \
                   "While you're raging, the first creature you hit with an attack on your turn becomes" \
                   " the target of the warriors, which hinder its attacks. " \
                   "Until the start of your next turn, that target has disadvantage on any attack roll " \
                   "that isn't against you, and when the target hits a creature other than you with an attack, " \
                   "that creature has resistance to the damage dealt by the attack. " \
                   "The effect on the target ends early if your rage ends."

        def spirit():
            desc = "If you are raging and another creature you can see within 30 feet of you takes damage, " \
                   "you can use your reaction to reduce that damage by "
            if 5 < level < 10:
                str(desc) + "2d6"
            if 9 < level < 14:
                str(desc) + "3d6"
            if 13 < level:
                str(desc) + "4d6"

            return desc

        def consult():
            return "At 10th level, you gain the ability to consult with your ancestral spirits. " \
                   "When you do so, you cast the augury or clairvoyance spell, " \
                   "without using a spell slot or material components. " \
                   "Rather than creating a spherical sensor, " \
                   "this use of clairvoyance invisibly summons one Of your ancestral spirits" \
                   " to the chosen location. Wisdom is your spellcasting ability for these spells. " \
                   "After you cast either spell in this way, you can't use this feature again until you " \
                   "finish a short or long rest."

        def venge():
            return "At 14th level, your ancestral spirits grow powerful enough to retaliate. " \
                   "When you use your Spirit Shield to reduce the damage of an attack, " \
                   "the attacker takes an amount of force damage equal to the damage" \
                   " that your Spirit Shield prevents."

        self.rage_description.append(protector())

        if level > 5:
            self.rage_description.append(spirit())
        if level > 9:
            self.feature.append(consult())
        if level > 13:
            self.feature.append(venge())

        return "ancestral guardian"

    def battlerager(self, level):

        def spike():
            return "When you choose this path at 3rd level, you gain the ability to use spiked armor (see the 'Spiked " \
                   "Armor' sidebar) as a weapon. While you are wearing spiked armor and are raging, you can use a " \
                   "bonus action to make one melee weapon attack with your armor spikes against a target within 5 " \
                   "feet of you. If the attack hits, the spikes deal ld4 piercing damage. You use your Strength " \
                   "modifier for the attack and damage rolls. Additionally, when you use the Attack action to grapple " \
                   "a creature, the target takes 3 piercing damage if your grapple check succeeds. "

        def reckless():
            return "Beginning at 6th level, when you use Reckless Attack while raging, you also gain temporary hit " \
                   "points equal to your Constitution modifier (minimum of 1). They vanish if any of them are left " \
                   "when your rage ends. "

        self.feature.append(spike())

        if level > 5:
            self.feature.append(reckless())
        if level > 9:
            self.feature.append("You can take a dash action as a bonus action while you are raging")
        if level > 13:
            self.feature.append("when a creature within 5 feet of you hits you with a melee attack,"
                                " the attacker takes 3 piercing damage if you are raging, "
                                "aren't incapacitated, and are wearing spiked armor.")

        return "battlerager"

    def beserker(self, level):

        def rage():
            return "Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you " \
                   "do so, for the duration of your rage you can make a single melee weapon attack as a bonus action " \
                   "on each of your turns after this one. When your rage ends, you suffer one level of exhaustion. "

        def mindless():
            self.resistance.append(["charm (while raging)", "frighten (while raging)"])

        def intimidate():
            beginning = "Beginning at 10th level, you can use your action to frighten someone with your menacing " \
                        "presence. When you do so, choose one creature that you can see within 30 feet of you. If the " \
                        "creature can see or hear you, it must succeed on a Wisdom saving throw "
            dc = 8 + self.proficiency_bonus + self.charisma
            end = "or be frightened of you until the end of your next turn. On subsequent turns, you can use your " \
                  "action to extend the duration of this effect on the frightened creature until the end of your next " \
                  "turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet " \
                  "away from you. "

            return beginning + str(dc) + end

        def retaliate():
            return "when you take damage from a creature that is within 5 feet of you, you can use your reaction to " \
                   "make a melee weapon attack against that creature. "

        self.feature.append(rage())
        if level > 5:
            mindless()
        if level > 9:
            self.feature.append(intimidate())
        if level > 13:
            self.feature.append(retaliate())

        return "beserker"

    def storm(self, level):
        element = input("which aura do you want to have? desert, sea, or tundra?")

        def aura():
            end = ""
            beginning = "Starting at 3rd level, you emanate a stormy, magical aura while you rage. The aura extends " \
                        "10 feet from you in every direction, but not through total cover. Your aura has an effect " \
                        "that activates when you enter your rage, and you can activate the effect again on each of " \
                        "your turns as a bonus action. Choose desert, sea, or tundra. Your aura's effect depends on " \
                        "that chosen environment, as detailed below. You can change your environment choice whenever " \
                        "you gain a level in this class. Your aura's effects require a saving throw, the DC equals "
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
                self.feature.append("as an action, you can touch a flammable object that isn't being worn or carried "
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
            animal = input("which totem spirit do you want for the first level? bear, eagle, wolf, elk, or tiger?")
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
            animal = input("which totem spirit do you want for the second level? You can choose the same if you'd "
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
                prof = input("which first skill do you want to be proficient in? athletics, acrobatics, stealth, "
                             "or survival?")
                prof_two = input("which second skill, different from the first, do you want to be proficient in? "
                                "athletics, acrobatics, stealth, or survival?")
                self.proficiency.append(prof)
                self.proficiency.append(prof_two)

        def walker():
            self.feature.append("you can cast the commune with nature spell, but only as a ritual. When you do so, "
                                "a spiritual version of one of the animals you chose for Totem Spirit or Aspect of "
                                "the Beast appears to you to convey the information you seek.")

        def attune():
            animal = input("which animal do you want to have attributes of? you can choose the same one as before. "
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

        def divine():
            beg = "you can channel divine fury into your weapon strikes. While you're raging, the first creature you " \
                  "hit on each of your turns with a weapon attack takes extra damage equal to "
            dice = math.floor(4 + level / 2)
            end = "The extra damage is necrotic or radiant; you choose the type of damage when you gain this feature."
            return beg + str(dice) + end

        def warrior():
            return "If a spell, such as raise dead, has the sole effect of restoring you to life (but not uncleath), " \
                   "the caster doesn't need material components to cast the spell on you. "

        def focus():
            return "the divine power that fuels your rage can protect you. If you fail a saving throw while you're " \
                   "raging, you can reroll it, and you must use the new roll. You can use this ability only once per " \
                   "rage. "

        def presence():
            return "you learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a " \
                   "battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of " \
                   "you that can hear you gain advantage on attack rolls and saving throws until the start of your " \
                   "next turn. Once you use this feature, you can't use it again until you finish a long rest. "

        def death():
            return "the divine power that fuels your rage allows you to shrug off fatal blows. While you're raging, " \
                   "having 0 hit points doesn't knock you unconscious. You still must make death saving throws, " \
                   "and you suffer the normal effects of taking damage while at 0 hit points. However, if you would " \
                   "die due to failing death saving throws, you don't die until your rage ends, and you die then only " \
                   "if you still have 0 hit points. "

        self.feature.append(divine())
        self.feature.append(warrior())
        if level > 5:
            self.feature.append(focus())
        if level > 9:
            self.feature.append(presence())
        if level > 13:
            self.feature.append(death())

        return "zealot"
