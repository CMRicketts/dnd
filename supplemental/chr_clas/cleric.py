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
        self.resistance = []
        self.language = []

        self.domain = ""
        self.channel_divine_desc = []
        self.channel_divine_ct = 1
        if self.level > 5:
            self.channel_divine_ct = 2
        if self.level > 17:
            self.channel_divine_ct = 3

        self.magic = []
        self.magic_throw = "wisdom"
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
        self.set_cantrip()
        self.set_spells()
        self.set_domain()

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
            self.feature.append("Turn Undead")
        if self.level > 4:
            self.feature.append("Destroy Undead")
        if self.level > 9:
            self.feature.append("Divine Intervention")

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
                                        "Insight, Medicine, Persuasion, or Religion?"))
            i += 1

    def equip(self):
        item = raw_input("do you want a Mace or Warhammer?")
        if item.lower() == "mace":
            self.weapon.append("mace")
        else:
            self.weapon.append("warhammer")
        pack = raw_input("what pack do you want? Priest's pack or Explorer's pack?")
        if pack.lower() == "priest":
            self.equipment.append("Priest's Pack")
        else:
            self.equipment.append("Explorer's Pack")
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

    def set_cantrip(self):
        self.cantrips[0] = 3
        self.cantrips[1].append(raw_input("Initialization: What three cleric cantrips do you want to add?"))
        if self.level > 3:
            self.cantrips[0] = 4
            self.cantrips[1].append(raw_input("Level up: what other cantrip do you want to add?"))
        if self.level > 9:
            self.cantrips[0] = 5
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

    def set_domain(self):
        domain = raw_input("What domain do you want to enter? There's a lot, so take your time.\n\tarcana, ambition, "
                           "city, death, forge, grave, knowledge, life, light,\n\tnature, order, protection, "
                           "solidarity, strength, tempest, trickery, war, or zeal?")
        if domain == "arcana":
            self.domain = "Arcana Domain"
            arcana_spells = [["detect magic", "magic missile"], ["magic weapon", "Nystul's magic aura"], ["dispel magic", "magic circle"], ["arcane eye", "leomund's secret chest"], ["planar binding", "teleportation circle"]]
            arcana_spf = [[["skill", 0, "arcana"]], [["feature", 5, "Spell Breaker"], ["feature", 7, "Potent Spellcasting"]], [["spell", "cantrip", 2, 0, raw_input("Arcana Domain: What two wizard cantrips do you want to learn? Please input.")], ["spell", "six", 16, 1], ["spell", "seven", 16, 1], ["spell", "eight", 16, 1], ["spell", "nine", 16, 1]], [["divine", 1, "Arcane Abjuration"]]]
            self.act_domain(arcana_spells, arcana_spf)
        elif domain == "ambition":
            self.domain = "Ambition Domain"
            ambition_spells = [["bane", "Disguise Self"], ["Mirror image", "ray of enfeeblement"], ["bestow curse", "vampiric touch"], ["death ward", "dimension door"], ["dominate person", "modify memory"]]
            ambition_spf = [[["skill", 0, "Warding Flare"]], [["divine", 1, "Invoke Duplicity"], ["divine", 5, "Cloak of Shadows"]], [["feature", 7, "Potent Spellcasting"], ["feature", 16, "Improved Duplicity"]]]
            self.act_domain(ambition_spells, ambition_spf)
        elif domain == "city":
            self.domain = "City Domain"
            city_spells = [["comprehend languages", "remote access"], ["find vehicle", "heat metal"], ["lightning bolt", "protection from ballistics"], ["locate creature", "synchronicity"], ["commune with city", "shutdown"]]
            city_spf = [[["spell", "cantrip", 1, 0, "On/Off"]], [["proficiency", 0, ["sidearms", "vehicles (land)"]]], [["feature", 0, "Heart of the City"], ["feature", 5, "Block Watch"], ["feature", 7, "Divine Strike (Psychic)"], ["feature", 16, "Express Transit"]], [["divine", 1, "Spirits of the City"]]]
            self.act_domain(city_spells, city_spf)
        elif domain == "death":
            self.domain = "Death Domain"
            death_spells = [["false life", "ray of sickness"], ["blindness/deafness", "ray of enfeeblement"], ["animate dead", "vampiric touch"], ["blight", "death ward"], ["antilife shell", "cloudkill"]]
            death_spf = [[["proficiency", 0, "martial weapons"]], [["spell", "cantrip", 1, 0, raw_input("Death Domain Initialization: What necromancy cantrip do you want to learn? Please input. ")]], [["feature", 0, "Reaper"], ["feature", 5, "Inescapable Destruction"], ["feature", 7, "Divine Strike (Necromancy)"], ["feature", 16, "Improved Reaper"]], [["divine", 1, "Touch of Death"]]]
            self.act_domain(death_spells, death_spf)
        elif domain == "forge":
            self.domain = "Forge Domain"
            forge_spells = [["identify", "searing smite"], ["heat metal", "magic weapon"], ["elemental weapon", "protection from energy"], ["fabricate", "wall of fire"], ["animate objects", "creation"]]
            forge_spf = [[["proficiency", 0, ["heavy armor", "smith's tools"]]], [["feature", 0, "Blessing of the Forge"], ["feature", 5, "Soul of the Forge"], ["feature", 7, "Divine Strike (Fire)"], ["feature", 16, "Saint of Forge and Fire"]], [["divine", 1, "Artisan's Blessing"]], [["resistance", 5, "fire"], ["resistance", 16, "fire (immunity)"]]]
            self.act_domain(forge_spells, forge_spf)
        elif domain == "grave":
            self.domain = "Grave Domain"
            grave_spells = [["bane", "false life"], ["gentle repose", "ray of enfeeblement"], ["revivify", "vampiric touch"], ["blight", "death ward"], ["antilife shell", "raise dead"]]
            grave_spf = [[["cantrip", 1, 0, "Spare the Dying"]], [["feature", 0, "Circle of Mortality"], ["feature", 0, "Eyes of the Grave"], ["feature", 5, "Sentinel at Death's Door"], ["feature", 7, "Potent Spellcasting"], ["feature", 16, "Keeper of Souls"]], [["divine", 1, "Path to the Grave"]]]
            self.act_domain(grave_spells, grave_spf)
        elif domain == "knowledge":
            self.domain = "Knowledge Domain"
            knowledge_spells = [["command", "identify"], ["augury", "suggestion"], ["nondetection", "speak with dead"], ["arcane eye", "confusion"], ["legend lore", "scrying"]]
            knowledge_spf = [[["language", 0, raw_input("Knowledge Domain Initialization: What two extra languages do you want to learn? Please input. ")]], [["skill", 0, raw_input("What two skills do you want to be proficient in? \nArcana, History, Nature, or Religion? Please input both. ")]], [["feature", 0, "Blessing of Knowledge"]], [["divine", 1, "Knowledge of the Ages"], ["divine", 5, "Read Thoughts"]], [["feature", 7, "Potent Spellcasting"], ["feature", 16, "Visions of the Past"]]]
            self.act_domain(knowledge_spells, knowledge_spf)
        elif domain == "zeal":
            self.domain = "Zeal Domain"
            zeal_spells = [["searing smite", "thunderous smite"], ["magic weapon", "shatter"], ["haste", "fireball"], ["fire shield (warm only)", "freedom of movement"], ["destructive wave", "flame strike"]]
            zeal_spf = [[["proficiency", 0, ["martial weapons", "heavy armor"]]], [["feature", 0, "Priest of Zeal"], ["feature", 5, "Resounding Strike"], ["feature", 7, "Divine Strike"], ["feature", 16, "Blaze of Glory"]], [["divine", 1, "Consuming Fervor"]]]
            self.act_domain(zeal_spells, zeal_spf)
        elif domain == "light":
            self.domain = "Light Domain"
            light_spells = [["burning hands", "faerie fire"], ["flaming sphere", "scorching ray"], ["daylight", "fireball"], ["guardian of faith", "wall of fire"], ["flame strike", "scrying"]]
            light_spf = [[["cantrip", 1, 0, "light"]], [["feature", 0, "Warding Flame"], ["feature", 5, "Improved Flare"], ["feature", 7, "Potent Spellcasting"], ["feature", 16, "Corona of Light"]], [["divine", 1, "Radiance of the Dawn"]]]
            self.act_domain(light_spells, light_spf)
        elif domain == "nature":
            self.domain = "Nature Domain"
            nature_spells = [["animal friendship", "speak with animals"], ["barkskin", "spike growth"], ["plant growth", "wind wall"], ["dominate beast", "grasping vine"], ["insect plague", "tree stride"]]
            nature_spf = [[["cantrip", 1, 0, raw_input("Nature Domain Initialization: What druid cantrip do you want to learn? Please input. ")]], [["proficiency", 0, "Heavy armor"]], [["divine", 1, "Charm Animals and Plants"]], [["feature", 5, "Dampen Elements"], ["feature", 7, "Divine Strike (nature)"], ["feature", 16, "Master of Nature"]]]
            self.act_domain(nature_spells, nature_spf)
        elif domain == "order":
            self.domain = "Order Domain"
            order_spells = [["command", "heroism"], ["enhance ability", "hold person"], ["mass healing word", "slow"], ["compulsion", "locate creature"], ["commune", "dominate person"]]
            order_spf = [[["proficiency", 0, "heavy armor"]], [["feature", 0, "Voice of Authority"], ["feature", 7, "Divine Strike (force)"], ["feature", 16, "Order's Wrath"]], [["divine", 1, "Order's Demand"]]]
            self.act_domain(order_spells, order_spf)
        elif domain == "protection":
            self.domain = "Protection Domain"
            protection_spells = [["compelled duel", "protection from good and evil"], ["aid", "protection from poison"], ["protection from energy", "slow"], ["guardian of faith", "Otiluke's resilient sphere"], ["antilife shell", "wall of force"]]
            protection_spf = [[["proficiency", 0, "heavy armor"]], [["feature", 0, "Shield of the Faithful"], ["feature", 5, "Blessed Healer"], ["feature", 7, "Divine Strike (radiant)"], ["feature", 16, "Indomitable Defense"]], [["divine", 1, "Radiant Defense"]]]
            self.act_domain(protection_spells, protection_spf)
        elif domain == "solidarity":
            self.domain = "Solidarity Domain"
            solidarity_spells = [["bless", "guiding bolt"], ["aid", "warding bond"], ["beacon of hope", "crusader's mantle"], ["aura of life", "guardian of faith"], ["circle of power", "mass cure wounds"]]
            solidarity_spf = [[["proficiency", 0, "heavy armor"]], [["feature", 0, "Solidarity's Action"], ["feature", 5, "Oketra's Blessing"], ["feature", 7, "Divine Strike (normal)"], ["feature", 16, "Supreme Healing"]], [["divine", 1, "Preserve Life"]]]
            self.act_domain(solidarity_spells, solidarity_spf)
        elif domain == "strength":
            self.domain = "Strength Domain"
            strength_spells = [["divine favor", "shield of faith"], ["enhance ability", "protection from poison"], ["haste", "protection from energy"], ["dominate beast", "stoneskin"], ["destructive wave", "insect plague"]]
            strength_spf = [[["cantrip", 1, 0, raw_input("Strength Domain Initialization: What druid cantrip do you want to learn?")]], [["skill", 0, raw_input("Strength Domain Initialization: What extra skill do you want to be proficient in? Animal handling, athletics, nature, or survival?")]], [["proficiency", 0, "heavy armor"]], [["divine", 1, "Feat of Strength"], ["divine", 5, "Rhona's Blessing"]], [["feature", 7, "Divine Strike (normal)"]], [["resistance", 16, "bludgeoning, piercing, and slashing damage from nonmagical attacks (Avatar of Battle)"]]]
            self.act_domain(strength_spells, strength_spf)
        elif domain == "tempest":
            self.domain = "Tempest Domain"
            tempest_spells = [["fog cloud", "thunderwave"], ["gust of wind", "shatter"], ["call lightning", "sleet storm"], ["control water", "ice storm"], ["destructive wave", "insect plague"]]
            tempest_spf = [[["proficiency", 0, ["martial weapons", "heavy armor"]]], [["feature", 0, "Wrath of the Storm"], ["feature", 5, "Thunderbolt Strike"], ["feature", 7, "Divine Strike (thunder)"], ["feature", 16, "Stormborn"]], [["divine", 1, "Destructive Wrath"]], [[]], [[]]]
            self.act_domain(tempest_spells, tempest_spf)
        elif domain == "trickery":
            self.domain = "Trickery Domain"
            trick_spells = [["charm person", "disguise self"], ["mirror image", "pass without trace"], ["blink", "dispel magic"], ["dimension door", "polymorph"], ["dominate person", "modify memory"]]
            trick_spf = [[["feature", 0, "Blessing of the Trickster"], ["feature", 7, "Divine Strike (poison)"], ["feature", 16, "Improved Duplicity"]], [["divine", 1, "Invoke Duplicity"], ["divine", 5, "Cloak of Shadows"]]]
            self.act_domain(trick_spells, trick_spf)
        elif domain == "war":
            self.domain = "War Domain"
            war_spells = [["divine favor", "shield of faith"], ["magic weapon", "spiritual weapon"], ["crusader's mantle", "spirit guardians"], ["freedom of movement", "stoneskin"], ["flame strike", "hold monster"]]
            war_spf = [[["proficiency", 0, ["martial weapons", "heavy armor"]]], [["feature", 0, "War Priest"]], [["divine", 1, "Guided Strike"], ["divine", 5, "War God's Blessing"]], [["feature", 7, "Divine Strike (normal)"]], [["resistance", 16, "bludgeoning, piercing, and slashing damange from non-magical weapons (Avatar of Battle)"]]]
            self.act_domain(war_spells, war_spf)
        else:
            self.domain = "Life Domain"
            life_spells = [["bless", "cure wounds"], ["lesser restoration", "spiritual weapon"], ["beacon of hope", "revivify"], ["death ward", "guardian of faith"], ["mass cure wounds", "raise dead"]]
            life_spf = [[["proficiency", 0, "heavy armor"]], [["feature", 0, "Disciple of Life"], ["feature", 5, "Blessed Healer"], ["feature", 7, "Divine Strike (radiant)"], ["feature", 16, "Supreme Healing"]], [["divine", 1, "Preserve Life"]]]
            self.act_domain(life_spells, life_spf)

    def act_domain(self, spells, sfp):
        self.lvl_one[0] += 2
        self.lvl_one[1].append(spells[0])
        if self.level > 2:
            self.lvl_two[0] += 2
            self.lvl_two[1].append(spells[1])
        if self.level > 4:
            self.lvl_three[0] += 2
            self.lvl_three[1].append(spells[2])
        if self.level > 6:
            self.lvl_four[0] += 2
            self.lvl_four[1].append(spells[3])
        if self.level > 8:
            self.lvl_five[0] += 2
            self.lvl_five[1].append(spells[4])

        for item in sfp:
            for ind in item:
                if ind[0] == "skill":
                    if self.level > ind[1]:
                        self.skill.append(ind[2])
                if ind[0] == "feature":
                    if self.level > ind[1]:
                        self.feature.append(ind[2])
                if ind[0] == "proficiency":
                    if self.level > ind[1]:
                        self.proficiency.append(ind[2])
                if ind[0] == "language":
                    if self.level > ind[1]:
                        self.language.append(ind[2])
                if ind[0] == "spell":
                    if ind[1] == "cantrip":
                        self.cantrips[0] += ind[3]
                        self.cantrips[1].append(str(ind[4]))
                    if self.level > ind[2]:
                        if ind[1] == "six":
                            self.lvl_six[0] += ind[3]
                            self.lvl_six[1].append(str(raw_input("Domain Level Up: What level 6 spell do you want to learn?")))
                    if self.level > ind[2]:
                        if ind[1] == "seven":
                            self.lvl_seven[0] += ind[3]
                            self.lvl_seven[1].append(str(raw_input("Domain Level Up: What level 7 spell do you want to learn?")))
                    if self.level > ind[2]:
                        if ind[1] == "eight":
                            self.lvl_eight[0] += ind[3]
                            self.lvl_eight[1].append(str(raw_input("Domain Level Up: What level 8 spell do you want to learn?")))
                    if self.level > ind[2]:
                        if ind[1] == "nine":
                            self.lvl_nine[0] += ind[3]
                            self.lvl_nine[1].append(str(raw_input("Domain Level Up: What level 9 spell do you want to learn?")))
                if ind[0] == "divine":
                    if self.level > ind[1]:
                        self.channel_divine_desc.append(ind[2])
                if ind[0] == "resistance":
                    if self.level > ind[1]:
                        self.resistance.append(ind[2])
