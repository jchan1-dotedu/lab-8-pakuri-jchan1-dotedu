from pakuri import *
from pakudex import *

print("Welcome to Pakudex: Tracker Extraordinaire!")

inp = input("Enter max capacity of the Pakudex: ")
intialized = False
while (not intialized):
    try:
        cap = int(inp)
        pDex = Pakudex(cap)
        if (cap >= 0):
            intialized = True
        else:
            intialized = False
            inp = input("Please enter a valid size. ")
    except ValueError:
        inp = input("Please enter a valid size. ")
        intialized = False

print(f"The Pakudex can hold {pDex.get_capacity()} species of Pakuri.")

while True:
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")


    recognized = False
    while (not recognized):
        try:
            test = int(input("\nWhat would you like to do? "))
            recognized = True
        except ValueError:
            print("Unrecognized menu selection!")
            print("\nPakudex Main Menu")
            print("-----------------")
            print("1. List Pakuri")
            print("2. Show Pakuri")
            print("3. Add Pakuri")
            print("4. Evolve Pakuri")
            print("5. Sort Pakuri")
            print("6. Exit")

    match test:
        case 1:
            if pDex.get_size() == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")

                strDex = pDex.get_species_array()

                i = 0
                for species in strDex:
                    print(f"{i + 1}. {strDex[i]}")
                    i += 1

        case 2:
            spec = input("Enter the name of the species to display: ")
            specList = []
            specList = pDex.get_stats(spec)
            if specList is None:
                print("Error: No such Pakuri!")
            else:
                print("\n Species: " + spec)
                print("\n Attack: " + specList[0])
                print("\n Defense: " + specList[1])
                print("\n Speed: " + specList[2])

        case 3:
            spec = input("Enter the name of the species to add: ")
            
            if (pDex.get_species_array() is not None):
                if len(pDex.get_species_array()) >= pDex.get_capacity():
                    print("Error: Pakudex is full!")
                elif spec in pDex.get_species_array():
                    print("Error: Pakudex already contains this species!")
            
            else:
                pDex.add_pakuri(spec)
                print(f"Pakuri species {spec} successfully added!")

        case 4:
            spec = input("Enter the name of the species to evolve: ")
            
            if spec in pDex.get_species_array():
                pDex.evolve_species(spec)
                print(spec + " has evolved!")
            else:
                print("Error: No such Pakuri!")
                
        case 5:
            pDex.sort_pakuri()
            print("Pakuri have been sorted!")

        case 6:
            print("Thanks for using Pakudex! Bye!")
            break
        
        case _:
            print("Unrecognized menu selection!")



