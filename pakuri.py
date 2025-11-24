class Pakuri:
    species = ""
    attack = 0
    defense = 0
    speed = 0

    def __init__(self, species):
    # Initialize the pakuri object with species attribute
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def __lt__(self, other):
        return self.species < other.get_species() 


    def get_species(self):
    # Returns the species of this critter
        return self.species

    def get_attack(self):
    # Returns the attack value of this critter
        return self.attack
    
    def get_defense(self):
    # Returns the defense value for this critter
        return self.defense
    
    def get_speed(self):
    # Returns the speed of this critter
        return self.speed
    
    def set_attack(self, new_attack):
    # Changes the attack value for this critter to new_attack
        self.attack = new_attack

    def set_defense(self, new_defense):
    # Changes the defense value for this critter to new_defense
        self.defense = new_defense

    def set_speed(self, new_speed):
    # Changes the speed value for this critter to new_speed
        self.speed = new_speed
    
    def evolve(self):
    # Will evolve the critter as follows: 
    # double the attack, quadruple the defense, and triple the speed
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3  