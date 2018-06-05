class Gnome:
    def __init__(self):
        self.intelligence = 2
        self.dexterity = 0
        self.constitution = 0
        self.age_low = 35
        self.age_high = 400
        self.height_low = 34
        self.height_high = 50
        self.weight_low = 38
        self.weight_high = 45
        self.size = "small"
        self.speed = 25
        self.magic = ""
        self.proficiency = ["darkvision"]
        self.resistance = ["intelligence", "wisdom", "charisma"]
        self.language = ["common", "gnomish"]
        self.set_subrace()

    def speak(self):
        return "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."

    def lore(self):
        return "Whenever you make an Intelligence (History) check related to" \
               " magical, alchemical, or technological items," \
               " you can add twice your proficiency bonus" \
               " instead of any other proficiency bonus that may apply."

    def tinker(self):
        return "You have proficiency with artisan tools (tinker's tools). " \
               "Using those tools, you can spend 1 hour and 10 gp worth of materials" \
               " to construct a Tiny clockwork device (AC 5, 1 hp)." \
               " The device ceases to function after 24 hours " \
               "(unless you spend 1 hour repairing it to keep the device functioning)," \
               " or when you use your action to dismantle it; " \
               "at that time, you can reclaim the materials used to create it. " \
               "You can have up to three such devices active at a time. " \
               "When you create a device, choose one of the following options:" \
               "\n\tClockwork Toy: This toy is a c1ockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier." \
               " When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction." \
               " It makes noises as appropriate to the creature it represents." \
               "\n\tFire Starter: The device produces a miniature flame," \
               " which you can use to light a candle, torch, or campfire." \
               " Using the device requires your action." \
               "\n\tMusic Box: When opened, this music box plays a single song at a moderate volume. " \
               "The box stops playing when it reaches the song's end or when it is closed."

    def set_subrace(self):
        subrace = raw_input("what is your subrace: forest, rock, or deep? ")
        subrace = subrace.lower()
        if(subrace == "forest"):
            self.dexterity = 1
            str(self.magic) + "minor illusion "
            self.proficiency.append(str(self.speak()))

        if(subrace == "rock"):
            self.constitution = 1
            self.proficiency.append(str(self.lore()))
            self.proficiency.append("artisan's tools (tinker tools")
            self.proficiency.append(str(self.tinker()))

        if(subrace == "deep"):
            self.dexterity = 1
            self.age_low = 25
            self.age_high = 225
            self.height_low = 35
            self.height_high = 43
            self.weight_low = 75
            self.weight_high = 125
            self.proficiency.append("dexterity (Stealth)")
            self.language.append("undercommon")