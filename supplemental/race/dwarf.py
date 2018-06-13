class Dwarf:
    def __init__(self, level):
        self.level = int(level)
        self.subrace = ""
        self.constitution = 2
        self.strength = 0
        self.wisdom = 0
        self.max_hp = 0
        self.hp_increase = 0
        self.age_low = 40
        self.age_high = 300
        self.height_low = 45
        self.height_high = 65
        self.weight_low = 140
        self.weight_high = 160
        self.speed = 25
        self.size = "medium"
        self.languages = ["common", "dwarvish"]
        self.resistance = ["poison"]
        self.proficiency = ["darkvision", "battleaxe", "handaxe", "throwing hammer", "warhammer", self.stonecunning(),
                            self.tool_prof()]
        self.set_subrace(self.level)

    def stonecunning(self):
        return "whenever you make an intelligence (history) check related to the origin of stonework," \
               " you are considered proficient in the History skill " \
               "and add double your proficiency bonus to the check, " \
               "instead of your normal proficiency bonus."

    def tool_prof(self):
        tool = raw_input("what tool proficiency do you want? smith tools, brew tools, or mason tools?")
        tool = tool.lower()
        if tool == 'smith':
            return "smith's tools"
        elif tool == "brew":
            return "brewing tools"
        elif tool == "mason":
            return "mason's tools"

    def set_subrace(self, level):
        subrace = raw_input("what subrace are you? hill or mountain? ")
        subrace = subrace.lower()
        if subrace == "hill":
            self.subrace = "Hill Dwarf"
            self.wisdom = 1
            while level != 0:
                self.max_hp = (level + self.max_hp)
                level = level - 1
        if subrace == "mountain":
            self.subrace = "Mountain Dwarf"
            self.strength = 2
            self.proficiency.append("light armor")
            self.proficiency.append("medium armor")
