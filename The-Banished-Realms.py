import pygame
import time
import random
#variables
health = 100
coins = 0
leftCamp = False
backpackSword = False
backpackAxe = False
sword = False
woodAxe = False #higher damage, less hit chance
commonFood = 0
regularFood = 0 
luxuriousFood = 0 #different food will have different healing amounts

#intro
while True:
    intro = input("Welcome to The Banished Realms, a medieval text-based input rpg - Would you like to play? (y/n): ")
    if intro.lower() == "n":
        print("Then why are you here? Go do something else!")
    elif intro.lower() == "y":
        print("Glad to hear it! - Your glorious adventure awaits!")
        time.sleep(1)
        print("You wake up in a small, but messy tent, which sounds as though it is in the middle of a tranquil forest,")
        print("with the wind whispering through the leaves, and many a bird chirping in the distance.")
        print("When you look through the open flaps of the tent, you see a slowly dying campfire stationed directly in front of your tent.")
        print("There is also a large backpack sitting to your left, and a few small snacks as well as a wooden shortsword on your right.")
        while True:
            campsite = input(
                "What do you do? \n a. Fill the backpack with the sword and food and then leave the campsite \n b. Leave without backpack and items \n c. Continue to inspect the campsite\nEnter your choice here: ")
            if campsite.lower() == "c":
                while True:
                    print("You continued to search the surrounding area, and found a small purse of 50 golden coins, and a large, heavy, axe lodged in a tree stump.")
                    campinspected = input("Now that you have inspected the campsite, do you choose to leave it with or without the backpack? \n a. Leave with backpack \n b. Leave without backpack\nEnter your choice here: ")
                    if campinspected.lower() == "b":
                        leftCamp = True
                        break
                    elif campinspected.lower() == "a":
                        while True:
                            swordOrAxe = input(
                                "You try putting the axe and the sword in your backpack, but only one of them will fit. \n The sword looks pretty blunt, but very accurate, and the axe looks much sharper, but a less accurate swing. Which one will you choose? \n a. Sword (Less damage, higher accuracy) \n b. Axe (More damage, lower accuracy\nEnter your choice here: ")
                            if swordOrAxe.lower() == "a":
                                print("You put the sword into your backpack, along with the food and the purse of coins.")
                                backpackSword = True
                                leftCamp = True
                                commonFood = 5
                                break
                            elif swordOrAxe.lower() == "b":
                                print("You put the axe into your backpack, along with the food and the purse of coins.")
                                backpackAxe = True
                                leftCamp = True
                                commonFood = 5
                                break
                            else:
                                print("Invalid Input!\n")
                        break
                    else:
                        print("Invalid Input!\n")
                break
            elif campsite.lower() == "b":
                leftCamp = True
                break
            elif campsite.lower() == "a":
                leftCamp = True
                backpackSword = True
                commonFood = 5
                break
            else:
                print("Invalid Input!\n")
        break
    else:
        print("Invalid Input!\n")
if leftCamp: 
    print("You left the camp, and before you sits an expansive forest. You see that there is a narrow dirt path, and you follow it.  \n After a few minutes of walking, you notice a fork in the path up ahead, with a sign post with signs pointing towards the paths. The sign leading to the left says "To (Elven Village)", and the sign to the right says "To Elven Forest")
    whichway = input("Which way do you choose? \n a. Left \n b. Right \n (Left goes to town, Right goes deeper into forest)")
          if whichway.lower() == "a":
          enemyEncounter = random.randint(1-3)
          break
          if whichway.lower() == "b":
          enemyEncounter = random.randint(2-5)
    if enemyEncounter = 1:
          print("While walking through the forest towards town, you spot a large, but lone wolf standing in the forest, and it looks hungry. It notices you, and begins to run towards you, while snarling loudly. You can choose to run away, or try and fight the wolf to get its meat.
          wolf = input("blah blah sorry i had to go")
