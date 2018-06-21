import math
import random

from supplemental.chr_clas.barbarian import Barbarian
from supplemental.chr_clas.bard import Bard
from supplemental.chr_clas.cleric import Cleric
from supplemental.chr_clas.druid import Druid

from supplemental.chr_clas.fighter import Fighter
from supplemental.chr_clas.monk import Monk
from supplemental.chr_clas.paladin import Paladin
from supplemental.chr_clas.ranger import Ranger
from supplemental.chr_clas.rogue import Rogue
from supplemental.chr_clas.sorcerer import Sorcerer
from supplemental.chr_clas.warlock import Warlock
from supplemental.chr_clas.wizard import Wizard

from supplemental.race.dragonborn import Dragonborn
from supplemental.race.dwarf import Dwarf
from supplemental.race.elf import Elf
from supplemental.race.gnome import Gnome
from supplemental.race.half_elf import Half_Elf
from supplemental.race.half_orc import Half_Orc
from supplemental.race.halfling import Halfling
from supplemental.race.human import Human
from supplemental.race.tiefling import Tiefling


class Character:
    def __init__(self):
        self.name = ""
        self.player = ""
        self.sex = ""
        self.age = ""
        self.height = ""
        self.weight = ""

        self.race = ""
        self.subrace = ""
        self.chr_class = ""
        self.archetype = ""
        self.size = ""
        self.color = ""
        self.background = ""
        self.personality_trait = ""
        self.ideal = ""
        self.flaw = ""
        self.bond = ""
        self.alignment = ""

        self.level = 0

        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        self.proficiency_bonus = 0
        self.path = ""

        self.hit_dice = ""
        self.max_hp = 0
        self.speed = 0
        self.swim_speed = 15
        self.fly_speed = 0

        self.skill = []

        self.save = []

        self.language = []
        self.proficiency = []
        self.feature = []
        self.feat = []
        self.resistance = []
        self.advantage = []
        self.disadvantage = []

        self.armor = ["", ""]

        self.attack = []
        self.equipment = []
        self.gold = 0.0
        self.weapon = []
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

        # class/race specific things

        self.rage = False # barbarian
        self.rage_desc = []
        self.rage_ct = 0
        self.rage_dmg = 0

        self.jack_bonus = 0 # bard

        self.divine_desc = [] # cleric
        self.divine_ct = 0

        self.style = "" # fighter

        self.ki_ct = 0 # monk
        self.ki_dc = 0
        self.ki_features = []
        self.unarmored_mvmt = 0

        self.oath_desc = [] # paladin
        self.divinity_desc = []
        self.fighting_style = ""
        self.fighting_style_desc = []

        self.master_desc = [] # ranger

        self.sneak_attack_desc = [] # rogue
        self.sneak_attack_dmg = ""
        self.expert_skills = []

        self.metamagic_desc = [] # sorcerer
        self.sorcery_pts = 0

        self.pact = "" # warlock
        self.pact_desc = []
        self.spell_slots = 0
        self.slot_lvl = 0
        self.invocation_ct = 0
        self.invocations = []

        self.tradition_desc = [] # wizard
        self.spellbook_ct = 0
        self.spell_master = []
        self.sig_spells = []

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

    def set_race(self):
        race = raw_input("what race is your character? ")
        self.race = race
        if race == "dragonborn":
            chr = Dragonborn(self.level)
            self.strength = self.strength + chr.strength
            self.charisma = self.charisma + chr.charisma
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.language.append(chr.languages)
            self.resistance.append(chr.resistance)
            self.attack.append(str(self.attack))
            self.color = chr.color
        elif race == "dwarf":
            chr = Dwarf(self.level)
            self.constitution = self.constitution + chr.constitution
            self.strength = self.strength + chr.strength
            self.wisdom = self.wisdom + chr.wisdom
            self.max_hp = self.max_hp + chr.max_hp
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.language.append("\n\t\t\t" + str(chr.languages))
            self.resistance.append("\n\t\t\t" + str(chr.resistance))
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
            self.subrace = chr.subrace
        elif race == "elf":
            chr = Elf(self.level)
            self.dexterity = self.dexterity + chr.dexterity
            self.intelligence = self.intelligence + chr.intelligence
            self.wisdom = self.wisdom + chr.wisdom
            self.charisma = self.charisma + chr.charisma
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.magic.append(str(chr.magic))
            self.cantrips.append(chr.cantrips)
            self.lvl_one.append(chr.lvl_one)
            self.lvl_two.append(chr.lvl_two)
            self.magic_throw = self.magic_throw + chr.magic_throw
            self.disadvantage.append(str(chr.disadvantage))
            self.proficiency.append(str(chr.proficiency))
            self.language.append(str(chr.language))
            self.subrace = chr.subrace
        elif race == "gnome":
            chr = Gnome()
            self.intelligence = self.intelligence + chr.intelligence
            self.dexterity = self.dexterity + chr.dexterity
            self.constitution = self.constitution + chr.constitution
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.magic.append(str(chr.magic))
            self.magic_throw = self.magic_throw + chr.magic_throw
            self.language.append("\n\t\t\t" + str(chr.language))
            self.resistance.append("\n\t\t\t" + str(chr.resistance))
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
            self.subrace = chr.subrace
        elif race == "half elf":
            chr = Half_Elf(self.level)
            self.strength = self.strength + chr.strength
            self.dexterity = self.dexterity + chr.dexterity
            self.charisma = self.charisma + chr.charisma
            self.wisdom = self.wisdom + chr.wisdom
            self.intelligence = self.intelligence + chr.intelligence
            self.constitution = self.constitution + chr.constitution
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.swim_speed = chr.swim_speed
            self.size = chr.size
            self.magic.append(str(chr.magic))
            self.magic_throw = self.magic_throw + chr.magic_throw
            self.cantrips.append(chr.cantrips)
            self.lvl_one.append(chr.lvl_one)
            self.lvl_two.append(chr.lvl_two)
            self.language.append("\n\t\t\t" + str(chr.language))
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
            self.advantage.append("\n\t\t\t" + str(chr.advantage))
        elif race == "half orc":
            chr = Half_Orc()
            self.strength = self.strength + chr.strength
            self.constitution = self.constitution + chr.constitution
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.language.append("\n\t\t\t" + str(chr.language))
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
        elif race == "halfling":
            chr = Halfling()
            self.dexterity = self.dexterity + chr.dexterity
            self.charisma = self.charisma + chr.charisma
            self.constitution = self.constitution + chr.constitution
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
            self.resistance.append("\n\t\t\t" + str(chr.resistance))
            self.language.append("\n\t\t\t" + str(chr.language))
            self.subrace = chr.subrace
        elif race == "human":
            chr = Human()
            self.strength = self.strength + chr.strength
            self.dexterity = self.dexterity + chr.dexterity
            self.charisma = self.charisma + chr.charisma
            self.wisdom = self.wisdom + chr.wisdom
            self.intelligence = self.intelligence + chr.intelligence
            self.constitution = self.constitution + chr.constitution
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.size = chr.size
            self.language.append("\n\t\t\t" + str(chr.language))
        else:
            print("default is Tiefling")
            chr = Tiefling(self.level)
            self.dexterity = self.dexterity + chr.dexterity
            self.intelligence = self.intelligence + chr.intelligence
            self.charisma = self.charisma + chr.charisma
            self.age = random.randrange(chr.age_low, chr.age_high)
            self.weight = random.randrange(chr.weight_low, chr.weight_high)
            self.height = random.randrange(chr.height_low, chr.height_high)
            self.speed = chr.speed
            self.fly_speed = chr.speed_flying
            self.feature.append(str(chr.feature))
            self.proficiency.append("\n\t\t\t" + str(chr.proficiency))
            self.resistance.append("\n\t\t\t" + str(chr.resistance))
            self.language.append("\n\t\t\t" + str(chr.language))
            self.magic.append(str(chr.magic))
            self.magic_throw = self.magic_throw + chr.magic_throw
            self.cantrips.append(chr.cantrips)
            self.lvl_one.append(chr.lvl_one)
            self.lvl_two.append(chr.lvl_two)
            self.subrace = chr.subrace

    def set_class(self):
        clas = raw_input("what class is your character? ")
        self.chr_class = clas
        if clas == "barbarian":
            chr = Barbarian(int(self.level), self.race, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence, self.wisdom)
            self.archetype = chr.archetype
            self.strength = chr.strength
            self.intelligence = chr.intelligence
            self.dexterity = chr.dexterity
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(str(chr.proficiency))
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(str(chr.saving_throw))
            self.feature.append(str(chr.feature))
            self.resistance.append(str(chr.resistance))
            self.equipment.append(str(chr.equipment))
            self.path = chr.path
            self.max_hp = self.max_hp + chr.hp
            self.swim_speed = chr.swim_speed
            self.attack.append(chr.attack)
            self.rage = True
            self.rage_dmg = chr.rage_dmg
            self.rage_ct = chr.rage_count
            self.rage_desc = (str(chr.rage_description))
            self.hit_dice = chr.hit_dice
            self.skill = chr.skill
            self.armor = ["none", "10"]
        elif clas == "bard":
            chr = Bard(self.level, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence, self.wisdom)
            self.archetype = chr.college
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.jack_bonus = int(chr.jack_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.equipment.append(chr.equipment)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spells.append(chr.spells)
            self.spell_ct += chr.spell_ct
        elif clas == "cleric":
            chr = Cleric(self.level, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence, self.wisdom)
            self.archetype = chr.domain
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
            self.divine_ct += chr.channel_divine_ct
            self.divine_desc.append(str(chr.channel_divine_desc))
        elif clas == "druid":
            chr = Cleric(self.level, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence,
                         self.wisdom)
            self.archetype = chr.circle
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "fighter":
            chr = Fighter(self.level, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence,
                         self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.archetype
            self.style = chr.style
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "monk":
            chr = Monk(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.way
            self.ki_features.append(chr.ki_features)
            self.ki_ct = chr.ki_ct
            self.ki_dc = chr.ki_dc
            if not self.armor:
                self.speed += chr.unarmored_mvmt
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "paladin":
            chr = Paladin(self.level, self.strength, self.dexterity, self.constitution, self.charisma, self.intelligence,
                         self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.style = chr.style
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.oath
            self.oath_desc.append(chr.oath_desc)
            self.divinity_desc.append(chr.divinity_desc)
            self.fighting_style = chr.fighting_style
            self.fighting_style_desc.append(chr.fighting_style_desc)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "ranger":
            chr = Ranger(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.style = chr.style
            self.archetype = chr.master
            self.master_desc.append(chr.master_desc)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "rogue":
            chr = Rogue(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.archetype
            self.sneak_attack_dmg = chr.sneak_attack_dmg
            self.sneak_attack_desc.append(chr.sneak_attack_desc)
            self.expert_skills.append(chr.expert_skills)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "sorcerer":
            chr = Sorcerer(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.origin
            self.metamagic_desc.append(chr.metamagic_desc)
            self.sorcery_pts += chr.sorcery_pts
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        elif clas == "warlock":
            chr = Warlock(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.patron
            self.pact_desc.append(chr.pact_desc)
            self.pact = chr.pact
            self.spell_slots += chr.spell_slots
            self.slot_lvl += chr.slot_lvl
            self.invocations.append(chr.invocations)
            self.invocation_ct += chr.invocation_ct
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct
        else:
            print("Default class is wizard")
            chr = Wizard(self.level, self.strength, self.dexterity, self.constitution, self.charisma,
                          self.intelligence,
                          self.wisdom)
            self.strength = chr.strength
            self.dexterity = chr.dexterity
            self.intelligence = chr.intelligence
            self.wisdom = chr.wisdom
            self.charisma = chr.charisma
            self.constitution = chr.constitution
            self.proficiency.append(chr.proficiency)
            self.proficiency_bonus = int(chr.proficiency_bonus)
            self.save.append(chr.saving_throw)
            self.feature.append(chr.feature)
            self.resistance.append(chr.resistance)
            self.equipment.append(chr.equipment)
            self.language.append(chr.language)
            self.max_hp = self.max_hp + chr.hp
            self.hit_dice = chr.hit_dice
            self.attack.append(chr.attack)
            self.armor = chr.armor
            self.magic.append(chr.magic)
            self.magic_throw += str(chr.magic_throw)
            self.spell_dc = chr.spell_dc
            self.spell_attack += chr.spell_attack
            self.cantrips.append(chr.cantrips)
            self.skill.append(chr.skill)
            self.weapon.append(chr.weapon)
            self.archetype = chr.tradition
            self.tradition_desc = chr.tradition_desc
            self.spellbook_ct += chr.spellbook_ct
            self.spell_master.append(chr.spell_master)
            self.sig_spells.append(chr.sig_spells)
            i = 0
            while i < 9:
                self.spells[i][0] += chr.spells[i][0]
                self.spells[i][1].append(chr.spells[i][1])
                i += 1
            self.spell_ct += chr.spell_ct



    # returns armor, ac, and weapon info
    def combat_to_string(self):

        if self.armor:
            combat = "Armor type wearing: " + str(self.armor[0]) + \
                     "\nArmor AC: \t\t\t" + str(self.armor[1]) + "\n"
        else:
            combat = "No Armor\n"
        wpn_string = ""
        for wpn in self.weapon:
            wpn_string = wpn_string + "Weapon: \t\t\t" + str(wpn)

        if wpn_string == "":
            wpn_string = "No Weapons"

        eqp = ""
        for ep in self.equipment:
            eqp = eqp + "Equipment: \t" + str(ep)

        if eqp == "":
            eqp = "No Equipment (something went wrong, dude)"

        spells = ""
        for spell in self.spells:
            spells = spells + "Spell: \t\t\t\t" + str(spell)
        if spells == "":
            spells = "No known spells"

        save = "\nSpell Ability: \t\t" + self.magic_throw

        return combat + wpn_string + "\n" + eqp + "\n" + spells + save

    # returns level, ability scores, score modifiers, hp
    def score_to_string(self):
        return "Level: \t\t\t\t" + str(self.level) + \
               "\nStrength, Mod: \t\t" + str(self.strength) + ", + " + str(self.strength_mod()) + \
               "\nDexterity, Mod: \t" + str(self.dexterity) + ", + " + str(self.dexterity_mod()) + \
               "\nConstitution, Mod: \t" + str(self.constitution) + ", + " + str(self.constitution_mod()) + \
               "\nIntelligence, Mod: \t" + str(self.intelligence) + ", + " + str(self.intelligence_mod()) + \
               "\nWisdom, Mod: \t\t" + str(self.wisdom) + ", + " + str(self.wisdom_mod()) + \
               "\nCharisma, Mod: \t\t" + str(self.charisma) + ", + " + str(self.charisma_mod()) + \
               "\nHit Dice: \t\t\t" + str(self.hit_dice) + \
               "\nMax HP: \t\t\t" + str(int(self.max_hp)) + \
               "\nSpeed: \t\t\t\t" + str(self.speed) + \
               "\nSwimming Speed: \t" + str(self.swim_speed) + \
                "\nFlying Speed: \t\t" + str(self.fly_speed) + "\n"

    # returns skills, saving throws, languages, proficiencies, features, and feats
    def feature_to_string(self):
        skil = ""
        sav = ""
        lang = ""
        profs = ""
        feats = ""
        featts = ""
        res = ""
        dis = ""
        atv = ""
        for item in self.skill:
            skil = skil + "Skill: \t\t\t\t\t\t\t" + str(item)
        for prof in self.save:
            sav = sav + "Proficient saving throw: \t\t" + str(prof)
        for language in self.language:
            lang = lang + "Language Known: \t" + str(language)
        for proficient in self.proficiency:
            profs = profs + str(proficient)
        for feature in self.feature:
            feats = feats + "Feature: \t\t\t\t\t\t" + str(feature)
        for feat in self.feat:
            featts = featts + "Feats: \t\t\t\t\t\t\t" + str(feat)
        for resis in self.resistance:
            res = res + str(resis)
        for adv in self.disadvantage:
            dis = dis + "Disadvantage: \t\t" + str(adv)
        for thy in self.advantage:
            atv = atv + "Advantages: \t\t" + str(thy)

        if skil == "":
            skil = "No Skills"
        if sav == "":
            sav = "No Saving Throws"
        if lang == "":
            lang = "No Known Languages"
        if profs == "":
            profs = "No Proficiencies"
        if feats == "":
            feats = "No Features"
        if featts == "":
            featts = "No Feats"
        if res == "":
            res = "No Resistances"
        if dis == "":
            dis = "No Disadvantages"
        if atv == "":
            atv = "No Advantages"

        return skil + "\n" + sav + "\n" + lang + "\n" + "Proficiencies: " +  profs + "\n" + feats + "\n" + featts + "\n" + "Resistance: " + res + "\n" + dis + "\n" + atv + "\n"

    # returns class/race specific things
    def special_to_string(self):
        rage = ""
        if self.rage:
            rage = "Rage Description: " + str(self.rage_desc) + "\n"\
                "Rage Count (max): " + str(self.rage_ct) + "\n"\
                "Rage Damage Modifier: +" + str(self.rage_dmg)

        return rage

    # returns name, player, xp, and all character information
    def character_to_string(self):
        color = ""
        if self.chr_class == "dragonborn":
            color = "\nColor: \t\t\t" + self.color
        beg = "\nName: \t\t\t\t" + self.name + \
              "\nPlayer Name: \t\t" + self.player + \
              "\nSex: \t\t\t\t" + self.sex + \
              "\nAge: \t\t\t\t" + str(self.age) + \
              "\nHeight: \t\t\t" + str(self.height) + " inches" + \
              "\nWeight: \t\t\t" + str(self.weight) + " pounds" + \
              "\n\nRace: \t\t\t\t" + self.race + \
              "\nSubrace: \t\t\t" + self.subrace + \
              "\nClass: \t\t\t\t" + self.chr_class + \
              "\nArchetype: \t\t\t" + self.archetype + \
              "\nBackground: \t\t" + self.background + \
              "\nPersonality Trait: \t" + self.personality_trait + \
              "\nIdeals: \t\t\t" + self.ideal + \
              "\nFlaws: \t\t\t\t" + self.flaw + \
              "\nBonds: \t\t\t\t" + self.bond + \
              "\nAlignment: \t\t\t" + self.alignment
        return beg + color + "\n"


    # returns the entire character to string
    def to_string(self):
        return self.character_to_string() + "\n" + self.score_to_string() + "\n" + self.feature_to_string() + "\n" + self.combat_to_string() + "\n" + "\n" + self.special_to_string() + "\n"

    # TODO
    # returns entire character to json in case they want to have that?
    # stretch goal
    def to_json(self):
        return ""
