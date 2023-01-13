import random
import docx2txt



characters1 = ["wizard", "warrior", "knight", "archer", "rogue", "paladin", "druid", "monk", "cleric", "ranger", "barbarian", "sorcerer", "warlock", "bard", "shaman"]
characters2 = ["ogre", "giant", "harpy", "dragon", "troll", "wyrm", "cyclops", "basilisk", "griffon", "manticore", "phoenix", "unicorn", "centaur", "satyr", "siren", "mermaid", "dryad", "nymph", "elf", "dwarf", "gnome", "fairy", "pixie", "sprite", "gargoyle", "golem", "hominid", "werewolf", "vampire", "zombie", "skeleton"]

#Elementals
fire_adjectives = ["flaming", "blazing", "sizzling", "scorching", "burning", "searing", "incandescent", "igneous", "pyroclastic", "fiery"]
water_adjectives = ["aquatic", "hydrous", "liquefied", "moist", "soggy", "damp", "humid", "deluged", "soaked", "drenched"]
earth_adjectives = ["earthy", "solid", "stony", "grounded", "earthen", "terrestrial", "geological", "pedestrian", "natural", "rocky"]
air_adjectives = ["aerial", "gaseous", "windy", "breezy", "ethereal", "aeriform", "atmospheric", "celestial", "insubstantial", "cloudy"]
void_adjectives = ["empty", "vacant", "blank", "unoccupied", "desolate", "sterile", "barren", "devoid", "void", "hollow"]
lightning_adjectives = ["electric", "electrified", "energetic", "lively", "flashy", "dazzling", "shocking", "thunderous", "stormy", "lightning"]

#Modern
Robotics_adjectives = ["advanced", "mechanical", "automated", "cybernetic", "robotic", "artificial", "hi-tech", "machine", "roboticized", "cybernetically-enhanced"]
Cyber_adjectives = ["cybernetic", "digital", "electronic", "hi-tech", "virtual", "computerized", "networked", "data-driven", "cyber-enhanced", "computer-generated"]
Steampunk_adjectives = ["clockwork", "steam-powered", "Victorian", "Victorian-inspired", "steam-driven", "retrofuturist", "mechanical", "steam-mechanical", "clockwork-powered", "steam-powered"]
Nanotechnology_adjectives = ["nanoscale", "microscopic", "minuscule", "atomic", "subatomic", "molecular", "nanomechanical", "nanocircuitry", "nanobot-enhanced", "nanostructural"]
Plasma_adjectives = ["ionized", "glowing", "radiant", "incandescent", "luminous", "fiery", "electrical", "charged", "plasma-based", "ionic"]
Gravity_adjectives = ["weightless", "gravitational", "zero-g", "anti-gravitational", "gravitationally-defying", "weightlessness-inducing", "gravitational-wave-emitting", "zero-g-capable", "gravitational-field-manipulating", "anti-gravitational-field-generating"]
Magnetism_adjectives = ["magnetic", "electromagnetic", "magnetized", "electromagnetically-charged", "magnetically-attractive", "electromagnetically-repulsive", "magnetically-polarized", "electromagnetically-pulsating", "magnetically-induced", "electromagnetically-induced"]
Dark_Matter_adjectives = ["enigmatic", "mysterious", "hidden", "invisible", "unknowable", "undetectable", "unseen", "unfathomable", "unobservable", "unexplained"]

#Eastern
Samurai_adjectives = ["honorable", "noble", "valiant", "gallant", "chivalrous", "dignified", "courteous", "respectful", "courtesy", "brave"]
Ninja_adjectives = ["stealthy", "sneaky", "furtive", "secretive", "surreptitious", "undercover", "clandestine", "covert", "hidden", "shrouded"]
Geisha_adjectives = ["graceful", "elegant", "refined", "cultivated", "well-mannered", "poised", "urbane", "polished", "genteel", "cultured"]
Sumo_adjectives = ["massive", "heavyweight", "oversized", "gigantic", "colossal", "monstrous", "towering", "enormous", "whopping", "prodigious"]
Kabuki_adjectives = ["dramatic", "theatrical", "showy", "ostentatious", "flamboyant", "extravagant", "flamboyance", "exhibitionist", "playful", "theatricality"]
Taiko_adjectives = ["rhythmic", "percussive", "drumming", "drumbeat", "pulsating", "thundering", "resonant", "energetic", "vibrant", "lively"]
Bamboo_adjectives = ["slender", "graceful", "delicate", "flimsy", "fragile", "grace", "lithe", "nimble", "supple", "willowy"]

#Pirates
pirate_adjectives = ["treacherous", "conniving", "devious", "sneaky", "crafty", "cunning", "guileful", "scheming", "scurvy", "dishonorable",
"raucous", "rowdy", "boisterous", "loud", "noisy", "unruly", "turbulent", "uncontrolled", "wild", "frenzied",
"daring", "bold", "brave", "courageous", "fearless", "gallant", "valiant", "intrepid", "heroic", "dauntless",
"salty", "briny", "oceangoing", "seafaring", "maritime", "nautical", "sea-faring", "oceanic", "coastal", "mariner",
"ruthless", "heartless", "merciless", "unscrupulous", "unprincipled", "opportunistic", "selfish", "self-serving", "greedy", "covetous"]

#Total Mayhem
def choose_random_word(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        word = random.choice(words)
        return word





print("(1). Elementals \n"
      "(2). Modern \n"
      "(3). Eastern \n"
      "(4). Pirates \n"
      "(5). Total Mayhem \n")
choice = int(input("Please select a number \n"))

if choice == 1:
    print("(1). Fire"
          "(2). Water"
          "(3). Earth"
          "(4). Air"
          "(5). Void"
          "(6). Lightning")
    choice1 = int(input("Please select a number \n"))
    if choice1 == 1:
      adjective_list = fire_adjectives
    elif choice1 == 2:
      adjective_list = water_adjectives
    elif choice1 == 3:
      adjective_list = earth_adjectives
    elif choice1 == 4:
      adjective_list = air_adjectives
    elif choice1 == 5:
      adjective_list = void_adjectives
    elif choice1 == 6:
      adjective_list = lightning_adjectives

    character1 = random.choice(characters1)
    character2 = random.choice(characters2)
    adjective = random.choice(adjective_list)
    response = f"{adjective} {character1} {character2}"
    print(response)

elif choice == 2:
    print("(1). Robotics"
          "(2). Cyber"
          "(3). Steampunk"
          "(4). Nanotechnology"
          "(5). Plasma"
          "(6). Gravity"
          "(7). Magnetism"
          "(8). Dark Matter")
    choice2 = int(input("Please select a number \n"))
    if choice2 == 1:
        adjective_list = Robotics_adjectives
    elif choice2 == 2:
        adjective_list = Cyber_adjectives
    elif choice2 == 3:
        adjective_list = Steampunk_adjectives
    elif choice2 == 4:
        adjective_list = Nanotechnology_adjectives
    elif choice2 == 5:
        adjective_list = Plasma_adjectives
    elif choice2 == 6:
        adjective_list = Gravity_adjectives
    elif choice2 == 7:
        adjective_list = Magnetism_adjectives
    elif choice2 == 8:
        adjective_list = Dark_Matter_adjectives

    character1 = random.choice(characters1)
    character2 = random.choice(characters2)
    adjective = random.choice(adjective_list)
    response = f"{adjective} {character1} {character2}"
    print(response)

elif choice == 3:
    print("(1). Samurai"
          "(2). Ninja"
          "(3). Geisha"
          "(4). Sumo"
          "(5). Kabuki"
          "(6). Taiko"
          "(7). Bamboo")
    choice2 = int(input("Please select a number \n"))
    if choice2 == 1:
        adjective_list = Samurai_adjectives
    elif choice2 == 2:
        adjective_list = Ninja_adjectives
    elif choice2 == 3:
        adjective_list = Geisha_adjectives
    elif choice2 == 4:
        adjective_list = Sumo_adjectives
    elif choice2 == 5:
        adjective_list = Kabuki_adjectives
    elif choice2 == 6:
        adjective_list = Taiko_adjectives
    elif choice2 == 7:
        adjective_list = Bamboo_adjectives


    character1 = random.choice(characters1)
    character2 = random.choice(characters2)
    adjective = random.choice(adjective_list)
    response = f"{adjective} {character1} {character2}"
    print(response)

elif choice ==4:

    adjective_list = pirate_adjectives

    character1 = random.choice(characters1)
    character2 = random.choice(characters2)
    adjective = random.choice(adjective_list)
    response = f"{adjective} {character1} {character2}"
    print(response)

elif choice == 5:


    adjective = choose_random_word('/Users/Uveysq/PycharmProjects/pythonProject/adjectives.txt')

    character1 = random.choice(characters1)
    character2 = random.choice(characters2)
    response = f"{adjective} {character1} {character2}"
    print(response)