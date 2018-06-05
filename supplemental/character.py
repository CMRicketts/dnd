import math

from supplemental.chr_clas.barbarian import Barbarian

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
        self.name = "name"
        self.player = "person"
        self.sex = "m"
        self.age = "19"
        self.height = "5"
        self.weight = "30"

        self.race = ""
        self.subrace = "none"
        self.chr_class = ""
        self.archetype = "archetype"
        self.background = "LG"
        self.personality_trait = "no personality"
        self.ideal = "ideal"
        self.flaw = "flaw"
        self.bond = "bond"
        self.alignment = "alignment"

        self.level = 0

        self.strength = 18
        self.dexterity = 16
        self.constitution = 14
        self.intelligence = 12
        self.wisdom = 10
        self.charisma = 8

        self.max_hp = 0

        self.skill = []

        self.save = []

        self.language = []
        self.proficiency = []
        self.feature = []
        self.feat = []

        self.armor = ""
        self.armor_ac = 0

        self.weapon = []

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
        if race == "dwarf":
            chr = Dwarf(self.level)
        if race == "elf":
            chr = Elf(self.level)
        if race == "gnome":
            chr = Gnome()
        if race == "half elf":
            chr = Half_Elf(self.level)
        if race == "half orc":
            chr = Half_Orc()
        if race == "halfling":
            chr = Halfling()
        if race == "human":
            chr = Human()
        if race == "tiefling":
            chr = Tiefling(self.level)
        return "testing race"

    def set_class(self):
        clas = raw_input("what class is your character? ")
        self.chr_class = clas
        return "testing class"

    # returns armor, ac, and weapon info
    def combat_to_string(self):
        combat = "Armor type wearing: " + self.armor + \
                 "\nArmor AC: \t\t\t" + str(self.armor_ac) + "\n"
        wpn_string = ""
        for wpn in self.weapon:
            wpn_string = wpn_string + "Weapon: \t\t\t" + wpn

        if wpn_string == "":
            wpn_string = "No Weapons"

        return combat + wpn_string

    # returns level, ability scores, score modifiers, hp
    def score_to_string(self):
        return "Level: \t\t\t\t" + str(self.level) + \
               "\nStrength, Mod: \t\t" + str(self.strength) + ", + " + str(self.strength_mod()) + \
               "\nDexterity, Mod: \t" + str(self.dexterity) + ", + " + str(self.dexterity_mod()) + \
               "\nConstitution, Mod: \t" + str(self.constitution) + ", + " + str(self.constitution_mod()) + \
               "\nIntelligence, Mod: \t" + str(self.intelligence) + ", + " + str(self.intelligence_mod()) + \
               "\nWisdom, Mod: \t\t" + str(self.wisdom) + ", + " + str(self.wisdom_mod()) + \
               "\nCharisma, Mod: \t\t" + str(self.charisma) + ", + " + str(self.charisma_mod()) + \
               "\nMax HP: \t\t\t" + str(self.max_hp) + "\n"

    # returns skills, saving throws, languages, proficiencies, features, and feats
    def feature_to_string(self):
        skil = ""
        sav = ""
        lang = ""
        profs = ""
        feats = ""
        featts = ""
        for item in self.skill:
            skil = skil + "\nSkill: \t\t\t\t\t\t\t" + item
        for prof in self.save:
            sav = sav + "\nProficient saving throw: \t\t" + prof
        for language in self.language:
            lang = lang + "\nLanguage Known: \t\t\t\t" + language
        for proficient in self.proficiency:
            profs = profs + "\nProficiency: \t\t\t\t\t" + proficient
        for feature in self.feature:
            feats = feats + "\nFeature: \t\t\t\t\t\t" + feature
        for feat in self.feat:
            featts = featts + "\nFeats: \t\t\t\t\t\t\t" + feat

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

        return skil + "\n" + sav + "\n" + lang + "\n" + profs + "\n" + feats + "\n" + featts + "\n"

    # returns name, player, xp, and all character information
    def character_to_string(self):
        return "\nName: \t\t\t\t" + self.name + \
               "\nPlayer Name: \t\t" + self.player + \
               "\nSex: \t\t\t\t" + self.sex + \
               "\nAge: \t\t\t\t" + self.age + \
               "\nHeight: \t\t\t" + self.height + \
               "\nWeight: \t\t\t" + self.weight + \
               "\n\nRace: \t\t\t\t" + self.race + \
               "\nSubrace: \t\t\t" + self.subrace + \
               "\nClass: \t\t\t\t" + self.chr_class + \
               "\nArchetype: \t\t\t" + self.archetype + \
               "\nBackground: \t\t" + self.background + \
               "\nPersonality Trait: \t" + self.personality_trait + \
               "\nIdeals: \t\t\t" + self.ideal + \
               "\nFlaws: \t\t\t\t" + self.flaw + \
               "\nBonds: \t\t\t\t" + self.bond + \
               "\nAlignment: \t\t\t" + self.alignment + "\n"

    # returns the entire character to string
    def to_string(self):
        return self.character_to_string() + "\n" + self.score_to_string() + "\n" +self.feature_to_string() + "\n" + self.combat_to_string() + "\n"

    # TODO
    # returns entire character to json in case they want to have that?
    # stretch goal
    def to_json(self):
        return ""
