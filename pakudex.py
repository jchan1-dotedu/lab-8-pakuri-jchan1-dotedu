from pakuri import *

class Pakudex:
    dex = []
    capacity = 0

    def __init__(self, capacity=20):
    # Initializes this object to contain exactly capacity objects when completely full. The default capacity pakudex should be 20
        self.capacity = capacity
        self.dex = []
        self.size = 0

    def get_size(self):
    # Returns the number of critters currently being stored in the pakudex
        return len(self.dex)

    def get_capacity(self):
    # Returns the number of critters that the pakudex has the capacity to hold at most
        return self.capacity

    def get_species_array(self):
    # Returns a list of strings containing the species of the critters as ordered in the pakudex; if there are no species added yet, this method should return None
        o = []

        if len(self.dex) == 0:
            return None
        
        for paku in self.dex:
            o.append(paku.get_species())

        return o

    def get_stats(self, species):
    # Returns a list of ints containing the attack, defense, and speed statistics of species at index 0, 1, and 2 respectively; if species is not in the pakudex, returns None
        o = []

        for paku in self.dex:
            if paku.get_species() == species:
                o = [paku.get_attack(), paku.get_defense(), paku.get_speed()]
                return o
        
        return None

    def sort_pakuri(self):
    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name (hint: lists have a .sort() method)
        self.dex.sort()

    def add_pakuri(self, species):
    # Adds species to the pakudex; if successful, return True, and False otherwise
        if len(self.dex) >= self.capacity:
            return False
        
        self.dex.append(Pakuri(species))
        return True
    
    def evolve_species(self, species):
    # Attempts to evolve species within the pakudex; if successful, return True, and False otherwise
        for paku in self.dex:
            if paku.get_species() == species:
                paku.evolve()
                return True
        
        return False
