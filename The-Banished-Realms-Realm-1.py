# IMPORTED MODULES
import pygame
import time
import random
import threading

creditsY = 0

pygame.init()
crashed = False
gameDisplay = pygame.display.set_mode((1280, 600))
clock = pygame.time.Clock()
black = (0, 0, 0)
def spritedisplay(img, x, y):
    gameDisplay.fill(black)
    gameDisplay.blit(img, (x, y))
sprite = None
def inputs():
    global sprite
    global creditsY

    # STATISTIC VARIABLES
    health = 100
    maxHealth = 100
    coins = 0
    commonFood = 0
    regularFood = 0
    luxuriousFood = 0

    # WEAPON VARIABLES
    backpackSword = False
    backpackAxe = False
    bow = False
    sword = False
    woodAxe = False
    axeDamage = 0
    swordDamage = 0
    bowDamage = 0
    arrows = 0
    swordHitChance = 0
    axeHitChance = 0
    bowHitChance = 0
    bowCriticalHitChance = 0

    # ARMOUR VARIABLES
    chainmailHelmet = False
    steelChestplate = False
    chainmailBoots = False
    chainmailLeggings = False
    wendigoRibCage = False
    wendigoSkull = False

    # ENEMY VARIABLES
    wolfAlive = False
    wolfHealth = 50
    wolfDamage = 0
    boarAlive = False
    boarHealth = 60
    boarDamage = 0
    thugAlive = False
    thugHealth = 55
    thugDamage = 0
    youngBearAlive = False
    youngBearHealth = 55
    youngBearDamage = 0
    largeWolfAlive = False
    largeWolfHealth = 75
    largeWolfDamage = 0
    spiritAlive = False
    spiritHealth = 225
    spiritDamage = 0

    # BOSS VARIABLES
    wendigo1Alive = False
    wendigo1Health = 10
    wendigo1Damage = 0
    wendigo2Alive = False
    wendigo2Health = 40
    wendigo2Damage = 0
    wendigo3Alive = False
    wendigo3Health = 150
    wendigo3Damage = 0
    wendigoDead = False
    wendigoAttack = 0

    # QUEST VARIABLES
    talkedToWoman = False
    ring = False
    ringQuest = False
    talkedToFarmer = False
    largeWolfDead = False
    talkedToMerchant = False
    parcelDelivered = False
    talkedToHistorian = False
    artifactQuest = False
    artifact = False
    spiritDead = False
    talkedToRecruiter = False

    # LOCATION VARIABLES
    archeryShop = False
    armorShop = False
    town = False
    fountain = False
    leftCamp = False
    bushes = True
    fruitTree = True
    ruins = False
    elderHouse = False
    forest = False

    # GAME VARIABLES
    credits = False
    playGame = True

    while playGame == True:
        sprite = pygame.image.load("Banished Realms Title Screen.png")
        intro = input("Welcome to The Banished Realms, a medieval text-based input rpg - Would you like to play? (y/n): ")
        if intro.lower() == "n":
            print("Then why are you here? Go do something else!")
            playGame = False
        elif intro.lower() == "y":
            print("Glad to hear it! - Your glorious adventure awaits!")
            time.sleep(2)
            sprite = pygame.image.load("campSite (dndspeak.com).png")
            time.sleep(2)
            print("You wake up in a small, but messy tent, which sounds as though it is in the middle of a tranquil forest,")
            time.sleep(8)
            print("with the wind whispering through the leaves, and many a bird chirping in the distance.")
            time.sleep(8)
            print("When you look through the open flaps of the tent, you see a slowly dying campfire stationed directly in front of your tent.")
            time.sleep(8)
            print("There is also a large backpack sitting to your left, and a few small snacks as well as a wooden shortsword on your right.")
            time.sleep(8)
            while True:
                campsite = input("What do you do? \n a. Fill the backpack with the sword and food and then leave the campsite \n b. Leave without backpack and items \n c. Continue to inspect the campsite\n")
                if campsite.lower() == "c":
                    while True:
                        sprite = pygame.image.load("axe(u:BlenderDude91 - Reddit).png")
                        time.sleep(2)
                        print("You continued to search the surrounding area, and found a small purse of 50 coins, and a large, heavy, axe lodged in a tree stump.\n")
                        time.sleep(8)
                        coins += 50
                        campinspected = input("Now that you have inspected the campsite, do you choose to leave it with or without the backpack? \n a. Leave with backpack \n b. Leave without backpack\n")
                        if campinspected.lower() == "b":
                            leftCamp = True
                            break
                        elif campinspected.lower() == "a":
                            while True:
                                swordOrAxe = input("You try putting the axe and the sword in your backpack, but only one of them will fit. \n The sword looks pretty blunt, but very accurate, and the axe looks much sharper, but a less accurate swing. Which one will you choose? \n a. Sword (Less damage, higher accuracy) \n b. Axe (More damage, lower accuracy\n")
                                if swordOrAxe.lower() == "a":
                                    print("You put the sword into your backpack, along with the food and the purse of coins.\n")
                                    backpackSword = True
                                    leftCamp = True
                                    commonFood = 5
                                    break
                                elif swordOrAxe.lower() == "b":
                                    print("You put the axe into your backpack, along with the food and the purse of coins.\n")
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
        sprite = pygame.image.load("forest1.png")
        print("You left the camp, and before you sits an expansive forest. You see that there is a narrow dirt path, and you follow it.  \n After a few minutes of walking, you notice a fork in the path up ahead, with a sign post with signs pointing towards the paths. The sign leading to the left says 'To Elven Village', and the sign to the right says 'To Elven Forest'\n")
        whichway = input("Which way do you choose? \n a. Left \n b. Right \n (Left goes to town, Right goes deeper into forest)\n")
        if whichway.lower() == "a":
            enemyEncounter = random.randint(1, 3)
        if whichway.lower() == "b":
            enemyEncounter = random.randint(2, 4)
        if enemyEncounter == 4:
            time.sleep(1)
            sprite = pygame.image.load("wolf 1 (Daniel Ljunggren - Concept Art World).png")
            time.sleep(1)
            print("While walking through the forest, you spot a large, but lone wolf standing in the forest, and it looks hungry. It notices you, and begins to run towards you, while snarling loudly. You can choose to run away, or try and fight the wolf to get its meat.\n")
            wolf = input("What do you do? \n a. Attack the wolf \n b. Run away\n")
            if wolf.lower() == "b":
                if backpackAxe or backpackSword == True:
                    print("You somehow got away from the wolf, but it managed to create a deep gash in your left arm, causing you to lose a substantial amount of health. \n*You lose 30 health points*\n")
                    health -= 30
                    time.sleep(2)
                    print(f"Your health is now {health}")
                if backpackAxe and backpackSword == False:
                    print("Since you didn't have any heavy objects weighing you down, you managed to get away unscathed.\n")
            if wolf.lower() == "a":
                wolfAlive = True
                while wolfAlive:
                    wolfFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                    if wolfFight.lower() == "a":
                        if sword or backpackSword:
                            swordDamage = random.randint(30, 50)
                            print(f"You hit the wolf for {swordDamage} damage!\n")
                            wolfHealth -= swordDamage
                            time.sleep(2)
                        if woodAxe or backpackAxe:
                            axeHitChance = random.randint(0, 100)
                            if axeHitChance < 75:
                                axeDamage = random.randint(40, 60)
                                print(f"You hit the wolf for {axeDamage} damage!\n")
                                wolfHealth -= axeDamage
                                time.sleep(2)
                            else:
                                print("You missed your swing, and are now vulnerable to attack.")
                        if bow:
                            if arrows >= 1:
                                bowHitChance = random.randint(0, 100)
                                bowDamage = random.randint(30, 60)
                                if bowHitChance in range(0, 60):
                                    print(f"You hit the wolf for {bowDamage} damage!\n")
                                    wolfHealth -= bowDamage
                                    print(f"You now have {arrows} arrows left!\n")
                                if bowHitChance in range(61, 70):
                                    print(f"You hit the wolf in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*")
                                    wolfHealth -= bowDamage + 20
                                else:
                                    print("You missed your shot, and did no damage to the wolf.")
                            else:
                                print("You do not have enough arrows to shoot at the wolf. Try using another weapon.\n")
                        if wolfHealth > 0:
                            print(f"The wolf now has {wolfHealth} health!\n")
                            wolfDamage = random.randint(25, 40)
                            print(f"The wolf then swung at you for {wolfDamage} damage!\n*You lose {wolfDamage} health*\n")
                            health -= wolfDamage
                            time.sleep(2)
                        if health > 0:
                            print(f"Your health is now {health}\n")
                            time.sleep(2)
                        if wolfHealth <= 0:
                            print("You killed the wolf with one final blow \n*You receive 5 regular food*\n")
                            wolfAlive = False
                        if health <= 0:
                            playagain = input("You Died - Would you like to play again? y/n\n")
                            if playagain.lower() == "y":
                                print("Glad to hear it!\n")
                                wolfAlive = True
                            if playagain.lower() == "n":
                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                if areYouSure.lower() == "n":
                                    print("Glad to hear it!\n")
                                    wolfAlive = True
                                if areYouSure.lower() == "y":
                                    break
                                    playGame = False
                    if wolfFight.lower() == "b":
                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                        if heal.lower() == "a" and commonFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                            if howMany in range(0, commonFood):
                                print(f"You ate {howMany} common food!\n")
                                health += 10 * howMany
                                commonFood -= howMany
                                print(f"You gain {health + (howMany * 10)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "b" and regularFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                            if howMany in range(0, regularFood):
                                print(f"You ate {howMany} regular food!\n")
                                health += 30 * howMany
                                regularFood -= howMany
                                print(f"You gain {health + (howMany * 30)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "c":
                            if luxuriousFood >= 1:
                                print(f"You ate one luxurious food!")
                                health = maxHealth
                                luxuriousFood -= 1
                            if luxuriousFood < 1:
                                print("You don't have enough food for that!")
                        if heal.lower() == "d":
                            print("You decide not to eat.\n")
                        wolfDamage = random.randint(10, 30)
                        print(f"The wolf then swung at you for {wolfDamage} damage!\n")
                        health -= wolfDamage
                        print(f"Your health is now {health}\n")
                        time.sleep(2)
                    if wolfFight.lower() == "c":
                        if backpackAxe or backpackSword == True:
                            print("You somehow got away from the wolf, but it managed to create a deep gash in your left arm, causing you to lose a substantial amount of health. \n*You lose 30 health points*\n")
                            health -= 30
                            time.sleep(2)
                            print(f"Your health is now {health}\n")
                        if backpackAxe and backpackSword == False:
                            print("Since you didn't have any heavy objects weighing you down, you managed to get away from the wolf unscathed.\n")
        if enemyEncounter == 3:
            time.sleep(1)
            sprite = pygame.image.load("bear.png")
            time.sleep(1)
            print("You are strolling through the forest, and hear a little bit of rustling in the leaves in front of you. Before you can tell what's going on, a young, but strong-looking bear walks up to you and growls.\n")
            youngBear = input("What do you do? \n a. Attack the young bear \n b. Run away\n")
            if youngBear.lower() == "b":
                if backpackAxe or backpackSword == True:
                    print("You somehow got away from the young bear, but it managed to create a deep gash in your left arm, causing you to lose a substantial amount of health. \n*You lose 30 health points*\n")
                    health -= 30
                    time.sleep(2)
                    print(f"Your health is now {health}")
                if backpackAxe and backpackSword == False:
                    print("Since you didn't have any heavy objects weighing you down, you managed to get away unscathed.\n")
            if youngBear.lower() == "a":
                youngBearAlive = True
                while youngBearAlive:
                    youngBearFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                    if youngBearFight.lower() == "a":
                        if sword or backpackSword:
                            swordDamage = random.randint(30, 50)
                            print(f"You hit the young bear for {swordDamage} damage!\n")
                            youngBearHealth -= swordDamage
                            time.sleep(2)
                        if woodAxe or backpackAxe:
                            axeHitChance = random.randint(0, 100)
                            if axeHitChance < 75:
                                axeDamage = random.randint(40, 60)
                                print(f"You hit the young bear for {axeDamage} damage!\n")
                                youngBearHealth -= axeDamage
                                time.sleep(2)
                            else:
                                print("You missed your swing, and are now vulnerable to attack.")
                        if bow:
                            if arrows >= 1:
                                bowHitChance = random.randint(0, 100)
                                bowDamage = random.randint(30, 60)
                                if bowHitChance in range(0, 60):
                                    print(f"You hit the young bear for {bowDamage} damage!\n")
                                    youngBearHealth -= bowDamage
                                    print(f"You now have {arrows} arrows left!\n")
                                if bowHitChance in range(61, 70):
                                    print(f"You hit the young bear in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*")
                                    youngBearHealth -= bowDamage + 20
                                else:
                                    print("You missed your shot, and did no damage to the young bear.")
                            else:
                                print("You do not have enough arrows to shoot at the young bear. Try using another weapon.\n")
                        if youngBearHealth > 0:
                            print(f"The young bear now has {youngBearHealth} health!\n")
                            youngBearDamage = random.randint(10, 25)
                            print(f"The young bear then swung at you for {youngBearDamage} damage!\n*You lose {youngBearDamage} health*\n")
                            health -= youngBearDamage
                            time.sleep(2)
                        if health > 0:
                            print(f"Your health is now {health}\n")
                            time.sleep(2)
                        if youngBearHealth <= 0:
                            print("You killed the young bear with one final blow \n*You receive 7 regular food*\n")
                            youngBearAlive = False
                        if health <= 0:
                            playagain = input("You Died - Would you like to play again? y/n\n")
                            if playagain.lower() == "y":
                                print("Glad to hear it!\n")
                                youngBearAlive = True
                            if playagain.lower() == "n":
                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                if areYouSure.lower() == "n":
                                    print("Glad to hear it!\n")
                                    youngBearAlive = True
                                if areYouSure.lower() == "y":
                                    break
                                    playGame = False
                    if youngBearFight.lower() == "b":
                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                        if heal.lower() == "a" and commonFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                            if howMany in range(0, commonFood):
                                print(f"You ate {howMany} common food!\n")
                                health += 10 * howMany
                                commonFood -= howMany
                                print(f"You gain {health + (howMany * 10)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "b" and regularFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                            if howMany in range(0, regularFood):
                                print(f"You ate {howMany} regular food!\n")
                                health += 30 * howMany
                                regularFood -= howMany
                                print(f"You gain {health + (howMany * 30)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "c":
                            if luxuriousFood >= 1:
                                print(f"You ate one luxurious food!")
                                health = maxHealth
                                luxuriousFood -= 1
                            if luxuriousFood < 1:
                                print("You don't have enough food for that!")
                        if heal.lower() == "d":
                            print("You decide not to eat.\n")
                        youngBearDamage = random.randint(10, 25)
                        print(f"The young bear then swung at you for {youngBear} damage!\n")
                        health -= youngBearDamage
                        print(f"Your health is now {health}\n")
                        time.sleep(2)
                    if youngBearFight.lower() == "c":
                        if backpackAxe or backpackSword == True:
                            print("You somehow got away from the young bear, but not without being slashed across the left arm.\n*You lose 25 health points*\n")
                            health -= 25
                            time.sleep(2)
                            print(f"Your health is now {health}\n")
                        if backpackAxe and backpackSword == False:
                            print("Since you didn't have any heavy objects weighing you down, you managed to get away from the young bear unscathed.\n")
        if enemyEncounter == 2:
            time.sleep(1)
            sprite = pygame.image.load("wildBoar(Brent's Sketchblog - Pinterest).png")
            time.sleep(1)
            print("While walking through a meadow, you hear a lot of screeching and snorting, and then all of a sudden a wild boar runs up to you.\n")
            boar = input("What do you do? \n a. Attack the boar \n b. Run away\n")
            if boar.lower() == "b":
                if backpackAxe or backpackSword == True:
                    print("You somehow got away from the wild boar, but it managed to create a deep gash in your left arm, causing you to lose a substantial amount of health. \n*You lose 40 health points*\n")
                    health -= 30
                    time.sleep(2)
                    print(f"Your health is now {health}")
                if backpackAxe and backpackSword == False:
                    print("Since you didn't have any heavy objects weighing you down, you managed to get away unscathed.\n")
            if boar.lower() == "a":
                boarAlive = True
                while boarAlive:
                    boarFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                    if boarFight.lower() == "a":
                        if sword or backpackSword:
                            swordDamage = random.randint(30, 50)
                            print(f"You hit the boar for {swordDamage} damage!\n")
                            boarHealth -= swordDamage
                            time.sleep(2)
                        if woodAxe or backpackAxe:
                            axeHitChance = random.randint(0, 100)
                            if axeHitChance < 75:
                                axeDamage = random.randint(40, 60)
                                print(f"You hit the boar for {axeDamage} damage!\n")
                                boarHealth -= axeDamage
                                time.sleep(2)
                            else:
                                print("You missed your swing, and are now vulnerable to attack.")
                        if bow:
                            if arrows >= 1:
                                bowHitChance = random.randint(0, 100)
                                bowDamage = random.randint(30, 60)
                                if bowHitChance in range(0, 60):
                                    print(f"You hit the boar for {bowDamage} damage!\n")
                                    boarHealth -= bowDamage
                                    print(f"You now have {arrows} arrows left!\n")
                                if bowHitChance in range(61, 70):
                                    print(f"You hit the boar in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*")
                                    boarHealth -= bowDamage + 20
                                else:
                                    print("You missed your shot, and did no damage to the boar.")
                            else:
                                print("You do not have enough arrows to shoot at the boar. Try using another weapon.\n")
                        if boarHealth > 0:
                            print(f"The boar now has {boarHealth} health!\n")
                            boarDamage = random.randint(20, 40)
                            print(f"The boar then swung at you for {boarDamage} damage!\n*You lose {boarDamage} health*\n")
                            health -= boarDamage
                            time.sleep(2)
                        if health > 0:
                            print(f"Your health is now {health}\n")
                            time.sleep(2)
                        if boarHealth <= 0:
                            print("You killed the boar with one final blow \n*You receive 7 regular food*\n")
                            boarAlive = False
                        if health <= 0:
                            playagain = input("You Died - Would you like to play again? y/n\n")
                            if playagain.lower() == "y":
                                print("Glad to hear it!\n")
                                boarAlive = True
                            if playagain.lower() == "n":
                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                if areYouSure.lower() == "n":
                                    print("Glad to hear it!\n")
                                    boarAlive = True
                                if areYouSure.lower() == "y":
                                    break
                                    playGame = False
                    if boarFight.lower() == "b":
                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                        if heal.lower() == "a" and commonFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                            if howMany in range(0, commonFood):
                                print(f"You ate {howMany} common food!\n")
                                health += 10 * howMany
                                commonFood -= howMany
                                print(f"You gain {health + (howMany * 10)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "b" and regularFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                            if howMany in range(0, regularFood):
                                print(f"You ate {howMany} regular food!\n")
                                health += 30 * howMany
                                regularFood -= howMany
                                print(f"You gain {health + (howMany * 30)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "c":
                            if luxuriousFood >= 1:
                                print(f"You ate one luxurious food!")
                                health = maxHealth
                                luxuriousFood -= 1
                            if luxuriousFood < 1:
                                print("You don't have enough food for that!")
                        if heal.lower() == "d":
                            print("You decide not to eat.\n")
                        boarDamage = random.randint(20, 40)
                        print(f"The boar then swung at you for {boarBear} damage!\n")
                        health -= boarDamage
                        print(f"Your health is now {health}\n")
                        time.sleep(2)
                    if boarFight.lower() == "c":
                        if backpackAxe or backpackSword == True:
                            print("You somehow got away from the wild boar, but not without being slashed across the left arm.\n*You lose 40 health points*\n")
                            health -= 40
                            time.sleep(2)
                            print(f"Your health is now {health}\n")
                        if backpackAxe and backpackSword == False:
                            print("You somehow got away from the wild boar unscathed.\n")
        if enemyEncounter == 1:
            time.sleep(1)
            sprite = pygame.image.load("thug 1 (Pewterarm - Reddit).png")
            time.sleep(1)
            print("You are walking on the path that leads towards town, and you come across a group of thugs, and one of them approaches you. He pulls out a dagger and says: Give me your money or else!\n")
            thug = input("What do you do? \n a. Resist, and attack the thug \n b. Run away\n")
            if thug.lower() == "b":
                if backpackAxe or backpackSword == True:
                    if coins == 50:
                        print("You try running away from the thug, but his goons have surrounded you and they knocked you out before you could run a meter. When you wake up, you have a headache, and when you check your backpack, you lost your purse full of money. \n*You lost 50 Coins*\n")
                        health -= 10
                        coins -= 50
                        print(f"Your health is now {health}\n")
                        print(f"Your coin amount is now {coins}\n")
                    if coins == 0:
                        print("You try running away from the thug, but his goons have surrounded you and they knocked you out before you could run a meter. When you wake up, you have a headache, and when you check your backpack, you lost your purse full of money. \n*You lost 50 Coins*\n")
                        health -= 10
                        print(f"Your health is now {health}\n")
                        print(f"Your coin amount is now {coins}\n")
                if backpackAxe and backpackSword == False:
                    print("Since you didn't have any heavy objects weighing you down, you managed to get away unscathed.\n")
            if thug.lower() == "a":
                thugAlive = True
                while thugAlive:
                    thugFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                    if thugFight.lower() == "a":
                        if sword or backpackSword:
                            swordDamage = random.randint(30, 50)
                            print(f"You hit the thug for {swordDamage} damage!\n")
                            thugHealth -= swordDamage
                            time.sleep(2)
                        if woodAxe or backpackAxe:
                            axeHitChance = random.randint(0, 100)
                            if axeHitChance < 75:
                                axeDamage = random.randint(40, 60)
                                print(f"You hit the thug for {axeDamage} damage!\n")
                                thugHealth -= axeDamage
                                time.sleep(2)
                            else:
                                print("You missed your swing, and are now vulnerable to attack.")
                        if bow:
                            if arrows >= 1:
                                bowHitChance = random.randint(0, 100)
                                bowDamage = random.randint(30, 60)
                                if bowHitChance in range(0, 60):
                                    print(f"You hit the thug for {bowDamage} damage!\n")
                                    thugHealth -= bowDamage
                                    print(f"You now have {arrows} arrows left!\n")
                                if bowHitChance in range(61, 70):
                                    print(
                                        f"You hit the thug in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*")
                                    thugHealth -= bowDamage + 20
                                else:
                                    print("You missed your shot, and did no damage to the thug.")
                            else:
                                print("You do not have enough arrows to shoot at the thug. Try using another weapon.\n")
                        if thugHealth > 0:
                            print(f"The thug now has {thugHealth} health!\n")
                            thugDamage = random.randint(15, 30)
                            print(f"The thug then swung at you for {thugDamage} damage!\n*You lose {thugDamage} health*\n")
                            health -= thugDamage
                            time.sleep(2)
                        if health > 0:
                            print(f"Your health is now {health}\n")
                            time.sleep(2)
                        if thugHealth <= 0:
                            print("You killed the thug with one final blow, and you gained coins from the past people he has robbed.\n")
                            coins += 50
                            thugAlive = False
                        if health <= 0:
                            playagain = input("You Died - Would you like to play again? y/n\n")
                            if playagain.lower() == "y":
                                print("Glad to hear it!\n")
                                thugAlive = True
                            if playagain.lower() == "n":
                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                if areYouSure.lower() == "n":
                                    print("Glad to hear it!\n")
                                    thugAlive = True
                                if areYouSure.lower() == "y":
                                    break
                                    playGame = False
                    if thugFight.lower() == "b":
                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                        heal = input(
                            "Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                        if heal.lower() == "a" and commonFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                            if howMany in range(0, commonFood):
                                print(f"You ate {howMany} common food!\n")
                                health += 10 * howMany
                                commonFood -= howMany
                                print(f"You gain {health + (howMany * 10)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "b" and regularFood >= 1:
                            howMany = int(input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                            if howMany in range(0, regularFood):
                                print(f"You ate {howMany} regular food!\n")
                                health += 30 * howMany
                                regularFood -= howMany
                                print(f"You gain {health + (howMany * 30)} health!\n")
                                if health > maxHealth:
                                    health = maxHealth
                                print(f"Your health is now {health}\n")
                            else:
                                print("You do not have enough food for that, please choose a valid amount.\n")
                        if heal.lower() == "c":
                            if luxuriousFood >= 1:
                                print(f"You ate one luxurious food!")
                                health = maxHealth
                                luxuriousFood -= 1
                            if luxuriousFood < 1:
                                print("You don't have enough food for that!")
                        if heal.lower() == "d":
                            print("You decide not to eat.\n")
                        boarDamage = random.randint(20, 40)
                        print(f"The thug then swung at you for {thugBear} damage!\n")
                        health -= thugDamage
                        print(f"Your health is now {health}\n")
                        time.sleep(2)
                    if thugFight.lower() == "c":
                        if backpackAxe or backpackSword == True:
                            print("You somehow got away from the thug, but his goons knocked you out, and when you wake up you have no coins.\n*You lose 10 health points, and lose 50 coins*\n")
                            health -= 40
                            coins -= 50
                            if coins < 0:
                                coins = 0
                            time.sleep(2)
                            print(f"Your health is now {health}\n")
                        if backpackAxe and backpackSword == False:
                            print("You somehow got away from the thug and his goons unscathed.\n")
        if wolfAlive or boarAlive or thugAlive or youngBearAlive == False:
            pathToTown = True
        if pathToTown == True:
            time.sleep(1)
            sprite = pygame.image.load("pixelated elven village(Stephanie Hernandez - Pinterest).png")
            time.sleep(2)
            print("After making your way through the forest, you finally make it to a small village situated on the edge of the forest.\n")
            time.sleep(8)
            print("The village is a bustling area, with people walking around, talking, with children playing. There was a glistening fountain in the center of a large square.\n")
            time.sleep(8)
            print("There we were also several shops in the buildings, that seemed to be quite popular.\n")
            time.sleep(5)
            town = True
            while town:
                time.sleep(1)
                sprite = pygame.image.load("pixelated elven village 2 (Caravan Stories).png")
                time.sleep(1)
                town = input("What do you do? \na. Visit the shops \nb. Talk to the townspeople \nc. Visit the fountain \nd. Leave the town\n")
                if town.lower() == "a":
                    print("You decide that you should walk around town and see what shops are available. After a short stroll through the village, you found 2 shops scattered around the town.\n")
                    whichShop = input("Which shop do you go to? \na. The archery shop \nb. The armor shop \n")
                    if whichShop.lower() == "a":
                        time.sleep(1)
                        sprite = pygame.image.load("archeryShop(SwordsvsSwords blog).png")
                        time.sleep(1)
                        if ringQuest == True:
                            print("Before you begin looking around the store, out of the corner of your eye, you also spot a small, glinting object underneath one of the stalls holding the bundles of arrows.\n")
                            ringFound = input("Do you choose to investigate the object? \na. Investigate \nb. Leave it be\n")
                            if ringFound.lower() == "a":
                                print("You choose to investigate the glint, and it turns out to be a wedding ring. This must be the woman's, and you decide to deliver it to her as soon as possible.\n")
                                ring = True
                                time.sleep(2)
                            if ringFound.lower() == "b":
                                print("You leave the object be, and move on.\n")
                                time.sleep(2)
                        if coins < 30:
                            print("After looking around the shop, you can see that the only thing you can afford is a bundle of arrows, for which you have no current use.\n")
                        if coins >= 30:
                            print( f"After looking around the shop, you can see that you are able to afford a bow, and {coins - 30} arrows.\n")
                            archeryShop = True
                            while archeryShop == True and coins > 0:
                                if coins >= 30:
                                    archeryShop = input("What do you do? \na. Buy a bow (Lower hit chance, Higher damage) (30 coins) \nb. Buy a bundle of 10 arrows (10 coins)\n")
                                    if archeryShop.lower() == "a" and coins >= 30:
                                        print("You bought a bow")
                                        bow = True
                                if coins < 30:
                                    archeryShop = input("What do you do? \na. Buy a bundle of 10 arrows (10 coins)\n")
                                    if archeryShop.lower() == "a" and coins >= 10:
                                        arrows += 10
                                if coins < 0:
                                    coins = 0
                                    archeryShop = False
                                    time.sleep(1)
                                    print("You left the shop because you no longer had any coins.\n")
                    if whichShop.lower() == "b":
                        time.sleep(1)
                        sprite = pygame.image.load("armory(Lady - DreamArt, On DeviantArt).png")
                        time.sleep(1)
                        if coins < 30:
                            print( "After looking around the shop, you cannot afford anything. You then leave the shop\n")
                        if coins >= 30:
                            armorShop = True
                            while armorShop and coins > 30:
                                if coins in range(30, 39):
                                    print("After looking around the shop, you can see that you are only able to afford a small set of boots.\n")
                                    armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Leave the shop\n")
                                    if armorShop.lower() == "a" and chainmailBoots == False:
                                        if chainmailBoots == False:
                                            maxHealth += 15
                                            coins -= 30
                                            print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                            chainmailBoots = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "b":
                                        print("You left the the shop.\n")
                                        armorShop = False
                                if coins in range(40, 49):
                                    print("After looking around the shop, you can see that you are only able to afford a small set of steel boots, and some chainmail leggings.\n")
                                    armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Leave the shop\n")
                                    if armorShop.lower() == "a" and chainmailBoots == False:
                                        if chainmailBoots == False:
                                            maxHealth += 15
                                            coins -= 30
                                            print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                            chainmailBoots = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "b" and chainmailLeggings == False:
                                        if chainmailLeggings == False:
                                            maxHealth += 25
                                            coins -= 40
                                            print(f"You bought the pair of leggings, and your Maximum Health went up by 25, to {maxHealth}\n")
                                            chainmailLeggings = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "c":
                                        print("You left the the shop.")
                                        armorShop = False
                                if coins in range(50, 59):
                                    print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, and a chainmail helmet.\n")
                                    armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd. Leave the shop\n")
                                    if armorShop.lower() == "a" and chainmailBoots == False:
                                        if chainmailBoots == False:
                                            maxHealth += 15
                                            coins -= 30
                                            print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                            chainmailBoots = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "b" and chainmailLeggings == False:
                                        if chainmailLeggings == False:
                                            maxHealth += 25
                                            coins -= 40
                                            print(f"You bought the pair of leggings, and your Maximum Health went up by 25, to {maxHealth}\n")
                                            chainmailLeggings = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "c" and chainmailHelmet == False:
                                        if chainmailHelmet == False:
                                            maxHealth += 35
                                            coins -= 50
                                            print(f"You bought the helmet, and your Maximum Health went up by 35, to {maxHealth}\n")
                                            chainmailHelmet = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "d":
                                        print("You left the the shop.\n")
                                        armorShop = False
                                if coins in range(60, 80):
                                    print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, a chainmail helmet, and a steel chestplate.")
                                    armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd.Buy the steel chestplate (60 coins)\ne. Leave the shop\n")
                                    if armorShop.lower() == "a" and chainmailBoots == False:
                                        if chainmailBoots == False:
                                            maxHealth += 15
                                            coins -= 30
                                            print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                            chainmailBoots = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "b" and chainmailLeggings == False:
                                        if chainmailLeggings == False:
                                            maxHealth += 25
                                            coins -= 40
                                            print(f"You bought the pair of leggings, and your Maximum Health went up by 25, to {maxHealth}\n")
                                            chainmailLeggings = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "c" and chainmailHelmet == False:
                                        if chainmailHelmet == False:
                                            maxHealth += 35
                                            coins -= 50
                                            print(f"You bought the helmet, and your Maximum Health went up by 35, to {maxHealth}\n")
                                            chainmailHelmet = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "d" and steelChestplate == False:
                                        if steelChestplate == False:
                                            maxHealth += 45
                                            coins -= 60
                                            print(f"You bought the chestplate, and your Maximum Health went up by 45, to {maxHealth}\n")
                                            steelChestplate = True
                                        else:
                                            print("You have already purchased this item!\n")
                                        time.sleep(2)
                                    if armorShop.lower() == "e":
                                        print("You left the the shop.\n")
                                        armorShop = False
                                if coins < 30:
                                    print("There is nothing in the store that you can buy, since you do not have enough coins to buy anything.\n")
                                    armorShop = False
                if town.lower() == "b":
                    townsFolkQuest = random.randint(1, 4)
                    if ring and talkedToWoman:
                        townsFolkQuest == 1
                    if largeWolfDead:  # NEW QUEST
                        townsFolkQuest == 2
                    if parcelDelivered:
                        townsFolkQuest == 3
                    if spiritDead and artifact:
                        townsFolkQuest == 4
                    if townsFolkQuest == 1:
                        if ring == False and talkedToWoman == False:  # NEW QUEST
                            print("You're walking around town, trying to find someone to talk to. You then see a woman who is weeping. You approach her, and ask what is wrong.\n")
                            time.sleep(2)
                            print("She then says that she has lost her wedding ring, in a sorrowful tone. She then asks you if you are able to help her find it again. She said she would reward you hansomely.\n")
                            woman = input("What do you do? \na. Help her find the ring \nb. Ignore her and move on.\n")
                            if woman.lower() == "a":
                                print("The woman thanks you, and promises to reward you hansomely if you return the ring.\n")
                                ringQuest = True
                        if ring == False and talkedToWoman == True:  # TIP
                            print("The woman says 'I might have dropped it while talking to my friend in the archery shop.' (Tip - Look in the Archery Shop)\n")
                        if ring == True and talkedToWoman == True:  # FINISH QUEST, REWARD
                            print("The woman thanks you dearly and says: 'You have no idea how much this means to me! Here you go, have 50 coins as a thank you.'\n")
                            coins += 50
                    if townsFolkQuest == 2:
                        time.sleep(1)
                        sprite = pygame.image.load("farmer(AlekSandra Mokrzycka - ArtStation).png")
                        time.sleep(1)
                        if largeWolfDead == False and talkedToFarmer == False:  # NEW QUEST
                            print("When looking around for someone to talk to, you a distraught farmer stands out to you. You approach him, and ask him what is wrong.\n")
                            time.sleep(2)
                            print("He then mentions that nearly all of his livestock have been either stolen from his farmland, or eaten alive. He suspects a large wolf has been terrorizing the animals in his and other's farms. He will reward you hansomely if you fulfill his offer.\n")
                            farmer = input("What do you do? \na. Help the farmer kill the wolf \nb. Decline his offer.\n")
                            if farmer.lower() == "a":
                                print("The farmer thanks you, and tells you the wolf usually hides out right outside the walls of the town.\n")
                                talkedToFarmer = True
                            if farmer.lower() == "b":
                                print("You tell the farmer you are not interested, and leave the scene.\n")
                        if largeWolfDead == False and talkedToFarmer:
                            print("The farmer tells you that the wolf was last spotted directly outside of the gates of the town. (Tip - Leave the town)\n")
                        if largeWolfDead and talkedToFarmer:
                            print("When you show the farmer the trophy, he seems very thankful, and gives you your reward that all of the farmers pooled together.\n")
                            coins += 50
                    if townsFolkQuest == 3:
                        time.sleep(1)
                        sprite = pygame.image.load("merchant(Tolouse Leplotte - PainterFactory).png")
                        time.sleep(1)
                        if parcelDelivered == False and talkedToMerchant == False:
                            print("When looking around for someone to talk to, a merchant of some sort jumps in front of you. They then ask you if you are willing to deliver a parcel to one of their clients, since they are too busy to do it themselves.\n")
                            time.sleep(2)
                            farmer = input("What do you do? \na. Help the merchant deliver the goods *unharmed* \nb. Decline his offer\n")
                            if farmer.lower() == "a":
                                print("You decide to help the merchant.\n")
                                talkedToMerchant = True
                            if farmer.lower() == "b":
                                print("You decline the merchant's offer, and walk away.\n")
                        if parcelDelivered == False and talkedToMerchant == True:
                            print("You overhear the merchant saying 'I could've sworn my client was over by the fountain over there.' (Tip - Look at the fountain)\n")
                        if parcelDelivered == True and talkedToMerchant == True:
                            print("The merchant thanks you for your service to him, and hands you a handful of coins worth 40 coins.\n")
                            coins += 40
                    if townsFolkQuest == 4:
                        time.sleep(1)
                        sprite = pygame.image.load("Historian (TSRodriguez - DeviantArt).pngn.png")
                        time.sleep(1)
                        if artifact == False and spiritDead == False and talkedToHistorian == False:
                            print("You walk around town, and you see an old man drop all of the papers and scrolls that he was holding, as he falls to the ground with a grunt.\n")
                            oldMan = input("Do you choose to help him up? (y/n)\n")
                            if oldMan.lower() == "y":
                                print("You help the old man up, and gather his papers for him. He smiles with gratitude, and says: 'Say, you look like an apt adventurer! What do you say you run an errand for me?'\n")
                                spiritQuest = input("What do you do? \na. Accept his quest. \nb. Decline his offer.\n")
                                if spiritQuest == "a":
                                    print("He brings you into his workshop strewn with artifacts and maps. The old man then tells you as he shows you a diagram and a map of some strange amulet and it's whereabouts: \n'I've been studying this artifact for years, but I'm too old to go out and find it. I've been waiting for an adventurer like you to come along and help. \n I believe it is situated on a pedestal in the ancient ritual grounds. I also believe that there is an otherworldy being guarding the artifact.\nReturn it to me unharmed and you will be rewarded well.'\n")
                                    talkedToHistorian = True
                            if oldMan.lower() == "n":
                                print("You decide not to help the old man up, and everyone looks at you in disgust as you walk away.\n")
                        if artifact and spiritDead and talkedToHistorian:
                            print("The old man looks at you in surprise and says: 'I can't believe you got it! Every adventurer I sent has never came back. He mumbles under his breath how he probably should have mentioned that part. He then proclaims: 'Here is your reward as promised!'\n")
                            coins += 60
                        if artifact == False and spiritDead == False and talkedToHistorian:
                            print("The old man says to you: 'If you are having trouble fighting the monster, maybe find some people who are willing to pay you money for completing errands, and use that to buy gear to help you in battle. \nI have also found that the trees outside of town can be shaken to provide some edible berries.\n")
                if town.lower() == "c":
                    time.sleep(1)
                    sprite = pygame.image.load("fountain2(fountainworks design).png")
                    time.sleep(1)
                    print("You decide to walk over to the fountain. The water is glowing slightly blue, and there is a woman standing next to it, as if waiting for someone, or something.\n")
                    fountain = True
                    while fountain:
                        fountain = input("What do you do? \na. Drink from the fountain \nb. Talk to the woman \nc. Go somewhere else\n")
                        if fountain.lower() == "a":
                            print("You drink from the fountain, and you feel rejuvinated. *You regain all lost health*\n")
                            time.sleep(2)
                            health = maxHealth
                            print(f"Your health is now {health}")
                        if fountain.lower() == "b":
                            if parcelDelivered == False and talkedToMerchant:
                                print("The woman thanks you for delivering the parcel. (Tip - You may now go back to the merchant to claim your reward)\n")
                                parcelDelivered = True
                            if parcelDelivered == True:
                                print("The woman thanks you again for delivering the parcel.\n")
                            if parcelDelivered == False and talkedToMerchant == False:
                                print("The woman tells you she is awaiting a parcel from a merchant.")
                        if fountain.lower() == "c":
                            print("You left the fountain.")
                            fountain = False
                if town.lower() == "d":
                    time.sleep(1)
                    sprite = pygame.image.load("dreadForest(Eric Gagnon - ArtStation).png")
                    time.sleep(1)
                    print("As you are leaving the town's gates, a villager approaches you and says: 'Be careful, they don't call it 'Dread Forest' for nothing. If you want to be exploring out there on your own, you better have the best gear possible if you want to come back alive.' \nTaking this into consideration, you venture out into the neighbouring forest.\n")
                    town = False
                    print("You stand outside the gates to the town facing the forest, you can either go back into town or continue going deeper into the forest.")
                    forest = input("What do you do? \na. Turn back around and go into town \nb. Try to forage through some bushes and trees for berries and fruit \nc. Turn left, and go to the ancient ruins, as the sign says. \nd. Turn right, and go deeper into the 'Dread Forest'\n")
                    while forest:
                        if forest.lower() == "a":
                            town = True
                            print("You walk back into town.\n")
                            time.sleep(2)
                        if forest.lower() == "d":
                            time.sleep(1)
                            sprite = pygame.image.load("dreadForest(Palisade village - Pinterest).png")
                            time.sleep(1)
                            print("You are walking through the forest away from the town, and an eerie chill runs down your spine, as if something is watching you from the deep forest beside you.\n")
                            if talkedToFarmer == True and largeWolfDead == False:
                                time.sleep(1)
                                sprite = pygame.image.load("wolf 1 (deceased)(EedenArtwork - DeviantArt.png")
                                time.sleep(1)
                                print("Suddenly, a large wolf jumps out from the bushes beside you, and snarls menacingly. It seems to be the one that the farmer described. You doubt that you will be able to run from it.\n")
                                time.sleep(2)
                                largeWolf = input("What do you do? \n a. Attack the large wolf \n b. Run away\n")
                                if largeWolf.lower() == "b":
                                    if backpackAxe or backpackSword == True:
                                        print("You somehow got away from the large wolf, but not without being slashed across the back and neck. There is now a large gash on your back, and your neck can't move without severe pain.\n*You lose 75 health points*\n")
                                        health -= 75
                                        time.sleep(2)
                                        print(f"Your health is now {health}")
                                    if backpackAxe and backpackSword == False:
                                        print("Since you didn't have any heavy objects weighing you down, you managed to get away with only a cut on your leg.\n*You lose 25 health points*\n")
                                if largeWolf.lower() == "a":
                                    largeWolfAlive = True
                                    while largeWolfAlive:
                                        largeWolfFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                                        if largeWolfFight.lower() == "a":
                                            if sword or backpackSword:
                                                swordDamage = random.randint(30, 50)
                                                print(f"You hit the large wolf for {swordDamage} damage!\n")
                                                largeWolfHealth -= swordDamage
                                                time.sleep(2)
                                            if woodAxe or backpackAxe:
                                                axeHitChance = random.randint(0, 100)
                                                if axeHitChance < 75:
                                                    axeDamage = random.randint(40, 60)
                                                    print(f"You hit the large wolf for {axeDamage} damage!\n")
                                                    largeWolfHealth -= axeDamage
                                                    time.sleep(2)
                                                else:
                                                    print("You missed your swing, and are now vulnerable to attack.")
                                            if bow:
                                                if arrows >= 1:
                                                    bowHitChance = random.randint(0, 100)
                                                    bowDamage = random.randint(30, 60)
                                                    if bowHitChance in range(0, 60):
                                                        print(f"You hit the large wolf for {bowDamage} damage!\n")
                                                        largeWolfHealth -= bowDamage
                                                        print(f"You now have {arrows} arrows left!\n")
                                                    if bowHitChance in range(61, 70):
                                                        print(f"You hit the large wolf in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*\n")
                                                        largeWolfHealth -= bowDamage + 20
                                                    else:
                                                        print("You missed your shot, and did no damage to the large wolf.\n")
                                                else:
                                                    print("You do not have enough arrows to shoot at the stone guardian. Try using another weapon.\n")
                                            if largeWolfHealth > 0:
                                                print(f"The large wolf now has {largeWolfHealth} health!\n")
                                                largeWolfDamage = random.randint(25, 40)
                                                print(f"The large wolf then swung at you for {largeWolfDamage} damage!\n*You lose {largeWolfDamage} health*\n")
                                                health -= largeWolfDamage
                                                time.sleep(2)
                                            if health > 0:
                                                print(f"Your health is now {health}\n")
                                                time.sleep(2)
                                            if largeWolfHealth <= 0:
                                                print("You killed the large wolf with one final blow \n*You receive 7 regular food*\n")
                                                largeWolfAlive = False
                                                largeWolfDead = True
                                            if health <= 0:
                                                playagain = input("You Died - Would you like to play again? y/n\n")
                                                if playagain.lower() == "y":
                                                    print("Glad to hear it!\n")
                                                    largeWolfAlive = True
                                                if playagain.lower() == "n":
                                                    areYouSure = input(
                                                        "This will erase all of your progress - Are you sure?\n")
                                                    if areYouSure.lower() == "n":
                                                        print("Glad to hear it!\n")
                                                        largeWolfAlive = True
                                                    if areYouSure.lower() == "y":
                                                        break
                                                        playGame = False
                                        if largeWolfFight.lower() == "b":
                                            print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                                            heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                                            if heal.lower() == "a" and commonFood >= 1:
                                                howMany = int(input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                                                if howMany in range(0, commonFood):
                                                    print(f"You ate {howMany} common food!\n")
                                                    health += 10 * howMany
                                                    commonFood -= howMany
                                                    print(f"You gain 30 health!\n")
                                                    if health > maxHealth:
                                                        health = maxHealth
                                                    print(f"Your health is now {health}\n")
                                                else:
                                                    print("You do not have enough food for that, please choose a valid amount.\n")
                                            if heal.lower() == "b" and regularFood >= 1:
                                                howMany = int(input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                                                if howMany in range(0, regularFood):
                                                    print(f"You ate {howMany} regular food!\n")
                                                    health += 30 * howMany
                                                    regularFood -= howMany
                                                    print(f"You gain 30 health!\n")
                                                    if health > maxHealth:
                                                        health = maxHealth
                                                    print(f"Your health is now {health}\n")
                                                else:
                                                    print("You do not have enough food for that, please choose a valid amount.\n")
                                            if heal.lower() == "c":
                                                if luxuriousFood >= 1:
                                                    print(f"You ate one luxurious food!\n")
                                                    health = maxHealth
                                                    luxuriousFood -= 1
                                                if luxuriousFood < 1:
                                                    print("You don't have enough food for that!\n")
                                            if heal.lower() == "d":
                                                print("You decide not to eat.\n")
                                            largeWolfDamage = random.randint(25, 45)
                                            print(f"The large wolf then swung at you for {largeWolfDamage} damage!\n")
                                            health -= largeWolfDamage
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if largeWolfFight.lower() == "c":
                                            if backpackAxe or backpackSword == True:
                                                print("You somehow got away from the large wolf, but not without being slashed across the back and neck. There is now a large gash on your back, and your neck can't move without severe pain.\n*You lose 75 health points*\n")
                                                health -= 75
                                                time.sleep(2)
                                                print(f"Your health is now {health}\n")
                                            if backpackAxe and backpackSword == False:
                                                print("Since you didn't have any heavy objects weighing you down, you managed to get away with only a cut on your leg.\n*You lose 25 health points*\n")
                                                health -= 25
                                    if largeWolfDead == True:
                                        print("You take the head as a trophy, and resolve to return to town to collect your reward from the farmer.\n")
                                        forest = False
                            if wendigoDead == False:
                                time.sleep(1)
                                sprite = pygame.image.load("Deer (Alex Padevall - TalentHouse).png")
                                time.sleep(1)
                                print("As you step foot deeper into the forest, you obtain a severe feeling of dread, and a deep chill runs down your spine. Something is very wrong with this forest. The only birds you see flying are crows, and all of the trees are severely diseased.")
                                time.sleep(10)
                                print("After walking through this strange place for a short period, you come across your first animal that isn't a crow: A ragged, diseased deer. Its antlers are decayed, and its eyes look like a dead grey. It approaches you slowly, and wherever it steps, all life surrounding its foot dies, and begins decaying quickly.")
                                time.sleep(15)
                                print("All of the crows that were watching eerily from above all fly away in haste. Even looking at the thing makes you nauseous, but entranced, as if it is drawing you in for some strange reason. For some reason, your mind won't let you run.")
                                time.sleep(10)
                                print("You are trapped.")
                                time.sleep(3)
                                wendigo1Alive = True
                                while wendigo1Alive:
                                    wendigo1Fight = input("Your gut is telling you to kill the deer, but you don't know why. \nWhat do you do?\na. Attack \nb. Heal \n")
                                    if wendigo1Fight.lower() == "a":
                                        if sword or backpackSword:
                                            swordDamage = random.randint(30, 50)
                                            print(f"You hit the diseased deer for {swordDamage} damage! *You gain a feeling of nauseousness, and light-headedness*\n")
                                            wendigo1Health -= swordDamage
                                            time.sleep(2)
                                        if woodAxe or backpackAxe:
                                            axeHitChance = random.randint(0, 100)
                                            if axeHitChance < 75:
                                                axeDamage = random.randint(40, 60)
                                                print(f"You hit the diseased deer for {axeDamage} damage! *You gain a feeling of nauseousness, and light-headedness*\n")
                                                wendigo1Health -= axeDamage
                                                time.sleep(2)
                                            else:
                                                print("You missed your swing, and are now vulnerable to attack.")
                                        if bow:
                                            if arrows >= 1:
                                                bowHitChance = random.randint(0, 100)
                                                bowDamage = random.randint(30, 60)
                                                if bowHitChance in range(0, 60):
                                                    print(f"You hit the diseased deer for {bowDamage} damage!\n")
                                                    time.sleep(2)
                                                    wendigo1Health -= bowDamage
                                                    print(f"You now have {arrows} arrows left!\n")
                                                    time.sleep(2)
                                                if bowHitChance in range(61, 70):
                                                    print(f"For a normal deer, that shot would've been a swift kill, but this one seems irritated at most. *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                                    time.sleep(2)
                                                    wendigo1Health -= bowDamage
                                                else:
                                                    print("You missed your shot, and did no damage to the diseased deer.\n")
                                            else:
                                                print("You do not have enough arrows to shoot at the diseased deer. Try using another weapon.\n")
                                        if wendigo1Health > 0:
                                            time.sleep(2)
                                            wendigo1Damage = random.randint(10, 20)
                                            print(f"The diseased deer then rammed its frail antlers at you for {wendigo1Damage} damage!\n*You lose {wendigo1Damage} health*\n")
                                            health -= wendigo1Damage
                                            time.sleep(2)
                                        if health > 0:
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if wendigo1Health <= 0:
                                            print("The deer looks into your eyes deeply, with a soulless glare. It seems quite irritated that you hit it. Gradually, its torso expands, and you can see its ribcage showing throw its chest.")
                                            time.sleep(8)
                                            print("All of its features begin to become more bony, its now-arched back has sharp ridges as if its spine is trying to break out. Its skin is stretched from the bones, and the hooves now becoming sharp, bony claws.")
                                            time.sleep(10)
                                            wendigo1Alive = False
                                            wendigo1Dead = True
                                            if wendigo1Dead == True:
                                                wendigo2Alive = True
                                        if health <= 0:
                                            playagain = input("You Died - Would you like to play again? y/n\n")
                                            if playagain.lower() == "y":
                                                print("Glad to hear it!\n")
                                                wendigo1Alive = True
                                            if playagain.lower() == "n":
                                                areYouSure = input(
                                                    "This will erase all of your progress - Are you sure?\n")
                                                if areYouSure.lower() == "n":
                                                    print("Glad to hear it!\n")
                                                    wendigo1Alive = True
                                                if areYouSure.lower() == "y":
                                                    break
                                                    playGame = False
                                    if wendigo1Fight.lower() == "b":
                                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                                        if heal.lower() == "a" and commonFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                                            if howMany in range(0, commonFood):
                                                print(f"You ate {howMany} common food!\n")
                                                health += 10 * howMany
                                                commonFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "b" and regularFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                                            if howMany in range(0, regularFood):
                                                print(f"You ate {howMany} regular food!\n")
                                                health += 30 * howMany
                                                regularFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "c":
                                            if luxuriousFood >= 1:
                                                print(f"You ate one luxurious food!\n")
                                                health = maxHealth
                                                luxuriousFood -= 1
                                            if luxuriousFood < 1:
                                                print("You don't have enough food for that!\n")
                                        if heal.lower() == "d":
                                            print("You decide not to eat.\n")
                                        wendigo1Damage = random.randint(10, 20)
                                        print(f"The diseased deer then swung at you for {wendigo1Damage} damage!\n")
                                        health -= wendigo1Damage
                                        print(f"Your health is now {health}\n")
                                        time.sleep(2)
                                while wendigo2Alive:
                                    wendigo2Fight = input("Your gut is telling you to kill that thing, but you don't know why. \nWhat do you do?\na. Attack \nb. Heal \n")
                                    if wendigo2Fight.lower() == "a":
                                        if sword or backpackSword:
                                            swordDamage = random.randint(30, 50)
                                            print(f"You hit the thing for {swordDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                            wendigo2Health -= swordDamage
                                            time.sleep(2)
                                        else:
                                            print("You missed your swing, and are now vulnerable to attack.")
                                        if woodAxe or backpackAxe:
                                            axeHitChance = random.randint(0, 100)
                                            if axeHitChance < 75:
                                                axeDamage = random.randint(40, 60)
                                                print(f"You hit the thing for {axeDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                                wendigo2Health -= axeDamage
                                                time.sleep(2)
                                            else:
                                                print("You missed your swing, and are now vulnerable to attack.")
                                        if bow:
                                            if arrows >= 1:
                                                bowHitChance = random.randint(0, 100)
                                                bowDamage = random.randint(30, 60)
                                                if bowHitChance in range(0, 60):
                                                    print(f"You hit the thing for {bowDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                                    time.sleep(2)
                                                    wendigo2Health -= bowDamage
                                                    print(f"You now have {arrows} arrows left!\n")
                                                    time.sleep(2)
                                                if bowHitChance in range(61, 70):
                                                    print(f"You hit the thing in one of its supposed weakpoints, but it only seems angry that you tried hitting it.\n")
                                                    time.sleep(2)
                                                    wendigo2Health -= bowDamage
                                                else:
                                                    print("You missed your shot, and did no damage to the thing.\n")
                                            else:
                                                print("You do not have enough arrows to shoot at the thing. Try using another weapon.\n")
                                        if wendigo2Health > 0:
                                            time.sleep(2)
                                            wendigo2Damage = random.randint(20, 35)
                                            print(f"The thing then rammed into you with its decaying antlers for {wendigo2Damage} damage!\n")
                                            health -= wendigo2Damage
                                            time.sleep(2)
                                        if health > 0:
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if wendigo2Health <= 0:
                                            time.sleep(2)
                                            print("Once you hit the thing back, at last, it begins retreating to a spot further away from you.\n")
                                            time.sleep(5)
                                            print("Out of nowhere, it stands up on its hind legs, towering meters above you. Its face begins tearing apart slowly, revealing its large, bloody skull, with sharp incisors used for ripping apart whole animals. All of its muscles were now exposed.\n")
                                            time.sleep(10)
                                            sprite = pygame.image.load("pixelated wendigo (original art from JakubJagoda on DeviantArt).png")
                                            time.sleep(1)
                                            print("The skull has some sort of ancient markings on the top of its skull, which were most likely drawn from blood. The bones that were trying to escape the beasts back had now ripped out, sharp spikes protruding from its back.\n")
                                            time.sleep(10)
                                            print("A long, spiny tail shoots out from the beasts behind, stretching meters in length, capable of whipping anything hard enough to put it into a state paralyzation.\n")
                                            time.sleep(10)
                                            print("The beast then lets out a shrill, high pitched shriek which shakes the surrounding area. As it does so, a spray of blood issues from its bloody maw.\n")
                                            time.sleep(10)
                                            print("Everything goes silent.")
                                            time.sleep(3)
                                            print("The hunt has begun.")
                                            time.sleep(3)
                                            wendigo2Alive = False
                                            wendigo2Dead = True
                                            if wendigo2Dead == True:
                                                wendigo3Alive = True
                                        if health <= 0:
                                            playagain = input("You Died - Would you like to play again? y/n\n")
                                            if playagain.lower() == "y":
                                                print("Glad to hear it!\n")
                                                wendigo1Alive = True
                                            if playagain.lower() == "n":
                                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                                if areYouSure.lower() == "n":
                                                    print("Glad to hear it!\n")
                                                    wendigo1Alive = True
                                                if areYouSure.lower() == "y":
                                                    break
                                                    playGame = False
                                    if wendigo2Fight.lower() == "b":
                                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                                        if heal.lower() == "a" and commonFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                                            if howMany in range(0, commonFood):
                                                print(f"You ate {howMany} common food!\n")
                                                health += 10 * howMany
                                                commonFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "b" and regularFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                                            if howMany in range(0, regularFood):
                                                print(f"You ate {howMany} regular food!\n")
                                                health += 30 * howMany
                                                regularFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "c":
                                            if luxuriousFood >= 1:
                                                print(f"You ate one luxurious food!\n")
                                                health = maxHealth
                                                luxuriousFood -= 1
                                            if luxuriousFood < 1:
                                                print("You don't have enough food for that!\n")
                                        if heal.lower() == "d":
                                            print("You decide not to eat.\n")
                                        wendigo2Damage = random.randint(20, 35)
                                        print(f"The thing then rammed into you with its decaying antlers for {wendigo2Damage} damage!\n")
                                        health -= wendigo2Damage
                                        print(f"Your health is now {health}\n")
                                        time.sleep(2)
                                while wendigo3Alive:
                                    wendigo3Fight = input("Your gut is telling you to kill that thing, but you don't know why. \nWhat do you do?\na. Attack \nb. Heal \n")
                                    if wendigo3Fight.lower() == "a":
                                        if sword or backpackSword:
                                            swordDamage = random.randint(30, 50)
                                            print(f"You hit the thing for {swordDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                            wendigo3Health -= swordDamage
                                            time.sleep(2)
                                        if woodAxe or backpackAxe:
                                            axeHitChance = random.randint(0, 100)
                                            if axeHitChance < 75:
                                                axeDamage = random.randint(40, 60)
                                                print(f"You hit the thing for {axeDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                                wendigo3Health -= axeDamage
                                                time.sleep(2)
                                            else:
                                                print("You missed your swing, and are now vulnerable to attack.")
                                        if bow:
                                            if arrows >= 1:
                                                bowHitChance = random.randint(0, 100)
                                                bowDamage = random.randint(30, 60)
                                                if bowHitChance in range(0, 60):
                                                    print(f"You hit the thing for {bowDamage} damage! *You gain a feeling of both deep sadness and overwhelming anger*\n")
                                                    time.sleep(2)
                                                    wendigo3Health -= bowDamage
                                                    print(f"You now have {arrows} arrows left!\n")
                                                    time.sleep(2)
                                                if bowHitChance in range(61, 70):
                                                    print(f"You hit the thing in one of its supposed weakpoints, but it only seems angry that you tried hitting it.\n")
                                                    time.sleep(2)
                                                    wendigo3Health -= bowDamage
                                                else:
                                                    print("You missed your shot, and did no damage to the diseased deer.\n")
                                            else:
                                                print("You do not have enough arrows to shoot at the diseased deer. Try using another weapon.\n")
                                        if wendigo3Health > 0:
                                            time.sleep(2)
                                            wendigoAttack = random.randint(1, 4)
                                            if wendigoAttack == 1:
                                                wendigo3Damage = 45
                                                print(f"The beast then whipped you with its bony tail, causing sharp pain on the place of impact, causing {wendigo3Damage} damage!\n")
                                                time.sleep(3)
                                                health -= wendigo3Damage
                                                time.sleep(2)
                                            if wendigoAttack == 2:
                                                wendigo3Damage = random.randint(40, 45)
                                                print(f"The beast then rammed into you with its blood-wrought antlers for {wendigo3Damage} damage!\n")
                                                time.sleep(3)
                                                health -= wendigo3Damage
                                                print(f"Your health is now {health}\n")
                                                time.sleep(2)
                                            if wendigoAttack == 3:
                                                wendigo3Damage = random.randint(40, 55)
                                                print(f"The beast then slashed with its long, sharp claws, slashing you open for {wendigo3Damage} damage!\n")
                                                time.sleep(3)
                                                health -= wendigo3Damage
                                                print(f"Your health is now {health}\n")
                                                time.sleep(2)
                                            if wendigoAttack == 4:
                                                wendigo3Damage = random.randint(50, 60)
                                                print(f"The beast pounced on you, and bit you, leaving a large set of bite marks, causing a very deep gash which sears with pain. {wendigo3Damage} damage!\n")
                                                time.sleep(3)
                                                health -= wendigo3Damage
                                                print(f"Your health is now {health}\n")
                                                time.sleep(2)
                                        if health > 0:
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if wendigo3Health <= 0:
                                            print("The beast seems worn out, and lets out one final, ear-splitting, blood-curdling screech which shakes you to the bone, before toppling over onto the ground with a gigantic thud.\n")
                                            time.sleep(10)
                                            print("Blood oozes out all of its cuts, creating a matt pool of dark red surrounding the gigantic beast.\n")
                                            time.sleep(10)
                                            print("Congratulations! You killed the beast! You scavenged the body and found: \nIts skull, which can be used as a helmet \nIts ribcage, which can be used to reinforce and strengthen existing armor\n")
                                            wendigoSkull = True
                                            wendigoRibCage = True
                                            time.sleep(3)
                                            wendigo3Alive = False
                                            wendigo3Dead = True
                                        if health <= 0:
                                            playagain = input("You Died - Would you like to play again? y/n\n")
                                            if playagain.lower() == "y":
                                                print("Glad to hear it!\n")
                                                wendigo1Alive = True
                                            if playagain.lower() == "n":
                                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                                if areYouSure.lower() == "n":
                                                    print("Glad to hear it!\n")
                                                    wendigo1Alive = True
                                                if areYouSure.lower() == "y":
                                                    break
                                                    playGame = False
                                    if wendigo3Fight.lower() == "b":
                                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                                        if heal.lower() == "a" and commonFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                                            if howMany in range(0, commonFood):
                                                print(f"You ate {howMany} common food!\n")
                                                health += 10 * howMany
                                                commonFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "b" and regularFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                                            if howMany in range(0, regularFood):
                                                print(f"You ate {howMany} regular food!\n")
                                                health += 30 * howMany
                                                regularFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "c":
                                            if luxuriousFood >= 1:
                                                print(f"You ate one luxurious food!\n")
                                                health = maxHealth
                                                luxuriousFood -= 1
                                            if luxuriousFood < 1:
                                                print("You don't have enough food for that!\n")
                                        if heal.lower() == "d":
                                            print("You decide not to eat.\n")
                                        wendigoAttack = random.randint(1, 4)
                                        if wendigoAttack == 1:
                                            wendigo3Damage = 45
                                            print(f"The beast then whipped you with its bony tail, causing sharp pain on the place of impact, causing {wendigo3Damage} damage!\n")
                                            time.sleep(3)
                                            health -= wendigo3Damage
                                            time.sleep(2)
                                        if wendigoAttack == 2:
                                            wendigo3Damage = random.randint(40, 45)
                                            print(f"The beast then rammed into you with its blood-wrought antlers for {wendigo3Damage} damage!\n")
                                            time.sleep(3)
                                            health -= wendigo3Damage
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if wendigoAttack == 3:
                                            wendigo3Damage = random.randint(40, 55)
                                            print(f"The beast then slashed with its long, sharp claws, slashing you open for {wendigo3Damage} damage!\n")
                                            time.sleep(3)
                                            health -= wendigo3Damage
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if wendigoAttack == 4:
                                            wendigo3Damage = random.randint(50, 60)
                                            print(f"The beast pounced on you, and bit you, leaving a large set of bite marks, causing a very deep gash which sears with pain. {wendigo3Damage} damage!\n")
                                            time.sleep(3)
                                            health -= wendigo3Damage
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                        if forest.lower() == "c":
                            time.sleep(1)
                            sprite = pygame.image.load("Ruins(Vincent LeBocey - ArtStations).png")
                            time.sleep(1)
                            print("You walk down the worn and overgrown path towards the ancient ruins.\n You see there are a few ruined structures surrounding a central area, which contains a pedestal which seems to have a ray of light directed towards it.\n")
                            if talkedToRectruiter and elderHouse == False:
                                print("You walk past the ruins towards the 'elders' house. It is situated in the middle of a meadow in the thick forest.")
                                elderHouse = True
                            while ruins:
                                artifact = input("What do you do? \na. Grab the artifact and leave the site \nb. Inspect the site \nc. Leave the area\n")
                                if artifact.lower() == "a":
                                    print("You grab the artifact quickly, and try to leave before anything goes wrong. Suddenly, all of the rubble in the area with ancient markings begin to glow vividly, and they all begin to move towards a small area in front of you.\n They begin assembling, and sticking to eachother, to form a large assembly of rock, which seems to have arms and legs. \n Once all of the rocks have stopped shifting, the small rocks glow brighter than before, and the object opens its mouth and roars loudly. \n The being appears to be a protector of the artifact that ha been awoken by you.\n")
                                    artifact = True
                                    spiritAlive = True
                                if artifact.lower() == "b":
                                    print("You begin to look around the site, and you see an abundance of rocks with what seems to be magical markings on them.\n Apart from that, you do not see much more.\n")
                                if artifact.lower() == "c":
                                    print("You leave the area.")
                                    ruins = False
                                    forest = True
                                while spiritAlive:
                                    time.sleep(1)
                                    sprite = pygame.image.load("StoneGolem (Yuki Sato - ArtStation).png")
                                    time.sleep(1)
                                    spiritFight = input("What do you do?\na. Attack \nb. Heal \nc. Run\n")
                                    if spiritFight.lower() == "a":
                                        if sword or backpackSword:
                                            swordDamage = random.randint(30, 50)
                                            print(f"You hit the stone guardian for {swordDamage} damage!\n")
                                            spiritHealth -= swordDamage
                                            time.sleep(2)
                                        if woodAxe or backpackAxe:
                                            axeHitChance = random.randint(0, 100)
                                            if axeHitChance < 75:
                                                axeDamage = random.randint(40, 60)
                                                print(f"You hit the stone guardian for {axeDamage} damage!\n")
                                                spiritHealth -= axeDamage
                                                time.sleep(2)
                                            else:
                                                print("You missed your swing, and are now vulnerable to attack.")
                                        if bow:
                                            if arrows >= 1:
                                                bowHitChance = random.randint(0, 100)
                                                bowDamage = random.randint(30, 60)
                                                if bowHitChance in range(0, 60):
                                                    print(f"You hit the stone guardian for {bowDamage} damage!\n")
                                                    spiritHealth -= bowDamage
                                                    print(f"You now have {arrows} arrows left!\n")
                                                if bowHitChance in range(61, 70):
                                                    print(f"You hit the stone guardian in one of it's weak points, and you did extra damage! *You did {bowDamage + 20} damage*")
                                                    spiritHealth -= bowDamage + 20
                                                else:
                                                    print("You missed your shot, and did no damage to the stone guardian.")
                                            else:
                                                print("You do not have enough arrows to shoot at the stone guardian. Try using another weapon.\n")
                                        if spiritHealth > 0:
                                            print(f"The stone guardian now has {spiritHealth} health!\n")
                                            spiritDamage = random.randint(10, 25)
                                            print(f"The stone guardian then swung its large hands at you for {spiritDamage} damage!\n*You lose {spiritDamage} health*\n")
                                            health -= spiritDamage
                                            time.sleep(2)
                                        if health > 0:
                                            print(f"Your health is now {health}\n")
                                            time.sleep(2)
                                        if spiritHealth <= 0:
                                            print("You hit the stone guardian one last time, and it seems as though it has run out of energy, and all of the stones that made it up collapse onto the ground lifelessly.\n")
                                            time.sleep(2)
                                            print("You can now return to the historian with the artifact to recieve your promised reward.")
                                            spiritAlive = False
                                            spiritDead = True
                                        if health <= 0:
                                            playagain = input("You Died - Would you like to play again? y/n\n")
                                            if playagain.lower() == "y":
                                                print("Glad to hear it!\n")
                                                spiritAlive = True
                                            if playagain.lower() == "n":
                                                areYouSure = input("This will erase all of your progress - Are you sure?\n")
                                                if areYouSure.lower() == "n":
                                                    print("Glad to hear it!\n")
                                                    spiritAlive = True
                                                if areYouSure.lower() == "y":
                                                    break
                                                    playGame = False
                                    if spiritFight.lower() == "b":
                                        print(f"You look for any healing items that you may be able to heal yourself with. You have: \n{commonFood} common food \n{regularFood} regular food \n{luxuriousFood} luxurious food\n")
                                        heal = input("Which items would you like to use to heal yourself with? \na. Common Food \nb. Regular Food \nc. Luxurious Food \nd. Back\n")
                                        if heal.lower() == "a" and commonFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {commonFood})\n"))
                                            if howMany in range(0, commonFood):
                                                print(f"You ate {howMany} common food!\n")
                                                health += 10 * howMany
                                                commonFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "b" and regularFood >= 1:
                                            howMany = int(
                                                input(f"How many would you like to eat? (You can eat {regularFood})\n"))
                                            if howMany in range(0, regularFood):
                                                print(f"You ate {howMany} regular food!\n")
                                                health += 30 * howMany
                                                regularFood -= howMany
                                                print(f"You gain 30 health!\n")
                                                if health > maxHealth:
                                                    health = maxHealth
                                                print(f"Your health is now {health}\n")
                                            else:
                                                print("You do not have enough food for that, please choose a valid amount.\n")
                                        if heal.lower() == "c":
                                            if luxuriousFood >= 1:
                                                print(f"You ate one luxurious food!\n")
                                                health = maxHealth
                                                luxuriousFood -= 1
                                            if luxuriousFood < 1:
                                                print("You don't have enough food for that!\n")
                                        if heal.lower() == "d":
                                            print("You decide not to eat.\n")
                                        spiritDamage = random.randint(10, 25)
                                        print(f"The stone guardian then swung its large hands at you for {spiritDamage} damage!\n")
                                        health -= spiritDamage
                                        print(f"Your health is now {health}\n")
                                        time.sleep(2)
                                    if spiritFight.lower() == "c":
                                        if backpackAxe or backpackSword == True:
                                            print("You got away from the stone guardian because it was so slow, but not without losing the artifact in the process. You will have to go back to retrieve it.\n")
                                            artifact = False
                                            time.sleep(2)
                                            print(f"Your health is now {health}\n")
                                        if backpackAxe and backpackSword == False:
                                            print("You got away from the stone guardian because it was so slow, but not without losing the artifact in the process. You will have to go back to retrieve it.\n")
                                            artifact = False
                        if forest.lower() == "b":
                            forage = input("Where do you choose to forage? \na. Bushes \nb. Nearby fruit trees\n")
                            if forage.lower() == "a" and bushes:
                                print("You rustle through the bushes with fruit in them to try and grab some berries. After looking for a few minutes, you managed to get 12 berries.\n")
                                commonFood += 12
                                bushes = False
                            else:
                                print("You have already depleted the nearby berry supplies!\n")
                            if forage.lower() == "b" and fruitTree:
                                print("You grabbed a few pieces of fruit hanging from the nearby fruit trees, and managed to scavenge 5 pieces.\n")
                                regularFood += 5
                                fruitTree = False
                            else:
                                print("You have already depleted the nearby fruit supplies!\n")
                        if wendigoDead:
                            print("As you begin walking back to town, a woman rushes up to you and asks: 'Are you the person that has slain the wendigo that has been terrorizing our village for centuries?'\n")
                            wendigoSlain = input("What do you do? \na. Tell her that it was you \nb. Ask her what a wendigo is\n")
                            if wendigoSlain.lower() == "a":
                                print("She tells you in a rushed frenzy: 'You must go to the village elder immediately! She will tell you all about your heroic deed!'\n")
                                time.sleep(5)
                                print("She says: 'Here, let me show you the way!'\n")
                                time.sleep(3)
                                print("She then leads you through the forest past the ancient ruins, and to the doorstep of an old hut in a small meadow in the forest.\n")
                                talkedToRecruiter = True
                                elderHouse = True
                            if wendigoSlain.lower() == "b":
                                print("The woman tells you that a wendigo is a large beast, which looks like a deer at first, but once it gets close enough to its prey, it tries to kill it, and eat it. This particular one has been causing trouble to our village for generations.\n")
                                time.sleep(10)
                                print("She then asks you again, 'So was it you that slayed the beast?'")
                                wendigoSlain2 = input("What do you do? \na. Tell her it was you \nb. Say it was not you\n")
                                if wendigoSlain2.lower() == "a":
                                    print("She tells you in a rushed frenzy: 'You must go to the village elder immediately! She will tell you all about your heroic deed!'\n")
                                    time.sleep(5)
                                    print("She says: 'Here, let me show you the way!'\n")
                                    time.sleep(3)
                                    print("She then leads you through the forest past the ancient ruins, and to the doorstep of an old hut in a small meadow in the forest.\n")
                                    talkedToRecruiter = True
                                    elderHouse = True
                                if wendigoSlain2.lower() == "b":
                                    print("You tell her that it was not you, and she says: 'Well, look around for them, we need to make sure they are rewarded! Tell them to go to the elder's house, which is located some ways past the ancient ceremony grounds.\n")
                                    time.sleep(5)
                                    print("You resolve to then make your way toward the elder's house, which is past the ancient ruins.\n")
                                    talkedToRecruiter = True
                        if elderHouse and talkedToRecruiter:
                            time.sleep(1)
                            sprite = pygame.image.load("ElderHouse.png")
                            time.sleep(1)
                            print("You arrive at the elder's hut, and begin to walk up the steps that lead to the front door of the hut.\n")
                            time.sleep(5)
                            print("As you open the sliding doors that lead inside, a strong whiff of incense greets your nose. The elder is an old woman sitting in front of you, wearing what looks like ritual attire.\n")
                            time.sleep(6)
                            print("The elder says 'Ahh, so you are the one that saved our village. That wendigo has been preventing us from progressing as a civilization for much too long. But no one up until now had the guts to appose it.\n")
                            time.sleep(10)
                            print("'On behalf of the entire village, we must thank you immensely for freeing us of this great burden which has rested upon our weakening shoulders for far too long.\n")
                            time.sleep(7)
                            print("The old woman hands you a bag which she claims contains 200 coins. She also gives you food which she says was provided by the best cooks in the village, and that it will heal all wounds instantly.\n")
                            time.sleep(9)
                            print("As a final gift, and confident that you are a good warrior, she hands you a mysterious map. She says it is a map of the next realm that you will have to travel to.\n")
                            times.sleep(8)
                            print("Finally, she mentioned how the King of all the realms has disappeared, and in the prophecies of time, it was told that he who conquered each of the realms toughest beasts may free the ruler of al of the lands\n")
                            time.sleep(10)
                            print("As you walk through the doors to leave, she says: 'Good luck, warrior.'")
                            credits = True
    if credits:
        time.sleep(1)
        sprite = pygame.image.load("costume1.png")
        time.sleep(1)
        creditsY += 200
        for i in range(100000000):
            creditsY -= 0.00002

x = threading.Thread(target=inputs)
x.start()
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    try:
        spritedisplay(sprite, 0, creditsY)
    except:
        pass
    pygame.display.update()
    clock.tick(60)
