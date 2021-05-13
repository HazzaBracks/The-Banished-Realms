import pygame
import time
import random

# variables
health = 100
maxHealth = 100
coins = 0
leftCamp = False
backpackSword = False
backpackAxe = False

bow = False
sword = False
woodAxe = False  # higher damage, less hit chance
axeDamage = 0
swordDamage = 0
bowDamage = 0
arrows = 0
swordHitChance = 0
axeHitChance = 0
bowHitChance = 0
bowCriticalHitChance = 0

chainmailHelmet = False
steelChestplate = False
chainmailBoots = False
chainmailLeggings = False

commonFood = 0
regularFood = 0
luxuriousFood = 0  # different food will have different healing amounts

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
largeWolfDead = False
largeWolfAlive = False
largeWolfHealth = 75
largeWolfDamage = 0

talkedToWoman = False
ring = False
ringQuest = False
talkedToFarmer = False
talkedToMerchant = False
parcelDelivered = False
fountain = False

archeryShop = False
armorShop = False
town = False

playGame = True

# intro
while playGame == True:
    intro = input("Welcome to The Banished Realms, a medieval text-based input rpg - Would you like to play? (y/n): ")
    if intro.lower() == "n":
        print("Then why are you here? Go do something else!")
        playGame = False
    elif intro.lower() == "y":
        print("Glad to hear it! - Your glorious adventure awaits!")
        time.sleep(2)
        print("You wake up in a small, but messy tent, which sounds as though it is in the middle of a tranquil forest,")
        time.sleep(2)
        print("with the wind whispering through the leaves, and many a bird chirping in the distance.")
        time.sleep(2)
        print("When you look through the open flaps of the tent, you see a slowly dying campfire stationed directly in front of your tent.")
        time.sleep(2)
        print("There is also a large backpack sitting to your left, and a few small snacks as well as a wooden shortsword on your right.")
        time.sleep(2)
        while True:
            campsite = input("What do you do? \n a. Fill the backpack with the sword and food and then leave the campsite \n b. Leave without backpack and items \n c. Continue to inspect the campsite\n")
            if campsite.lower() == "c":
                while True:
                    print("You continued to search the surrounding area, and found a small purse of 50 coins, and a large, heavy, axe lodged in a tree stump.")
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
    print("You left the camp, and before you sits an expansive forest. You see that there is a narrow dirt path, and you follow it.  \n After a few minutes of walking, you notice a fork in the path up ahead, with a sign post with signs pointing towards the paths. The sign leading to the left says 'To Elven Village', and the sign to the right says 'To Elven Forest'\n")
    whichway = input("Which way do you choose? \n a. Left \n b. Right \n (Left goes to town, Right goes deeper into forest)\n")
    if whichway.lower() == "a":
        enemyEncounter = random.randint(1, 3)
    if whichway.lower() == "b":
        enemyEncounter = random.randint(2, 4)
if enemyEncounter == 4:
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
                if bow:
                    if arrows >= 1:
                        bowHitChance = random.randint(30, 60)
                        print(f"You hit the wolf for {bowDamage} damage!\n")
                        print(f"You now have {arrows} arrows left!\n")
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
                        print(f"You gain {health+(howMany*10)} health!\n")
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
                        print(f"You gain {health+(howMany*30)} health!\n")
                        if health > maxHealth:
                            health = maxHealth
                        print(f"Your health is now {health}\n")
                    else:
                        print("You do not have enough food for that, please choose a valid amount.\n")
                if heal.lower() == "c":
                    if luxuriousFood >= 1:
                        print(f"You ate one luxurious food!")
                        health = maxHealth
                        health -= 1
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
                if bow:
                    if arrows >= 1:
                        bowHitChance = random.randint(30, 60)
                        print(f"You hit the young bear for {bowDamage} damage!\n")
                        print(f"You now have {arrows} arrows left!\n")
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
                        print(f"You gain {health+(howMany*10)} health!\n")
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
                        print(f"You gain {health+(howMany*30)} health!\n")
                        if health > maxHealth:
                            health = maxHealth
                        print(f"Your health is now {health}\n")
                    else:
                        print("You do not have enough food for that, please choose a valid amount.\n")
                if heal.lower() == "c":
                    if luxuriousFood >= 1:
                        print(f"You ate one luxurious food!")
                        health = maxHealth
                        health -= 1
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
                if bow:
                    if arrows >= 1:
                        bowHitChance = random.randint(30, 60)
                        print(f"You hit the boar for {bowDamage} damage!\n")
                        print(f"You now have {arrows} arrows left!\n")
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
                        health -= 1
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
                if bow:
                    if arrows >= 1:
                        bowHitChance = random.randint(30, 60)
                        print(f"You hit the thug for {bowDamage} damage!\n")
                        print(f"You now have {arrows} arrows left!\n")
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
                    print("You killed the thug with one final blow!\n")
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
                        health -= 1
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
    print("After making your way through the forest, you finally make it to a small village situated on the edge of the forest.\n")
    time.sleep(2)
    print("The village is a bustling area, with people walking around, talking, with children playing. There was a glistening fountain in the center of a large square.\n")
    time.sleep(2)
    print("There we were also several shops in the buildings, that seemed to be quite popular.\n")
    time.sleep(2)
    town = True
    while town:
        town = input("What do you do? \na. Visit the shops \nb. Talk to the townspeople \nc. Visit the fountain \nd. Leave the town\n")
        if town.lower() == "a":
            print("You decide that you should walk around town and see what shops are available. After a short stroll through the village, you found 2 shops scattered around the town.\n")
            whichShop = input("Which shop do you go to? \na. The archery shop \nb. The armor shop \n")
            if whichShop.lower() == "a":
                if ringQuest == True:
                    print("Before you begin looking around the store, out of the corner of your eye, you also spot a small, glinting object underneath one of the stalls holding the bundles of arrows.\n")
                    ringFound = input("Do you choose to investigate the object? \na. Investigate \nb. Laave it be\n")
                    if ringFound.lower() == "a":
                        print("You choose to investigate the glint, and it turns out to be a wedding ring. This must be the woman's, and you decide to deliver it to her as soon as possible.\n")
                        time.sleep(2)
                    if ringFound.lower() == "b":
                        print("You leave the object be, and move on.\n")
                        time.sleep(2)
                if coins < 30:
                    print("After looking around the shop, you can see that the only thing you can afford is a bundle of arrows, for which you have no current use.\n")
                if coins >= 30:
                    print(f"After looking around the shop, you can see that you are able to afford a bow, and {coins - 30} arrows.\n")
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
                if coins < 30:
                    print("After looking around the shop, you cannot afford anything. You then leave the shop\n")
                if coins >= 30:
                    armorShop = True
                    while armorShop and coins > 30:
                        if coins in range(30,39):
                            print("After looking around the shop, you can see that you are only able to afford a small set of boots.\n")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "b":
                                print("You left the the shop.\n")
                                armorShop = False
                        if coins in range(40,49):
                            print("After looking around the shop, you can see that you are only able to afford a small set of steel boots, and some chainmail leggings.\n")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}\n")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "c":
                                print("You left the the shop.")
                                armorShop = False
                        if coins in range(50,59):
                            print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, and a chainmail helmet.\n")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}\n")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "c" and chainmailHelmet == False:
                                maxHealth += 35
                                coins -= 50
                                print(f"You bought the chainmail helmet, and your Maximum Health went up by 35, to {maxHealth}\n")
                                chainmailHelmet = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "d":
                                print("You left the the shop.\n")
                                armorShop = False
                        if coins in range(60,80):
                            print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, a chainmail helmet, and a steel chestplate.")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd.Buy the steel chestplate (60 coins)\ne. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}\n")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}\n")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "c" and chainmailHelmet == False:
                                maxHealth += 35
                                coins -= 50
                                print(f"You bought the chainmail helmet, and your Maximum Health went up by 35 to {maxHealth}\n")
                                chainmailHelmet = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!\n")
                                time.sleep(2)
                            if armorShop.lower() == "d" and steelChestplate == False:
                                maxHealth += 45
                                coins -= 60
                                print(f"You bought the steel chestplate, and your Maximum Health went up by 35, to {maxHealth}\n")
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
            if ring == True and talkedToWoman == False:
                townsFolkQuest == 1
            if largeWolfDead == True and talkedToFarmer == True:  # NEW QUEST
                townsFolkQuest == 2
            if townsFolkQuest == 1:
                if ring == False and talkedToWoman == False: # NEW QUEST
                    print("You're walking around town, trying to find someone to talk to. You then see a woman who is weeping. You approach her, and ask what is wrong.\n")
                    time.sleep(2)
                    print("She then says that she has lost her wedding ring, in a sorrowful tone. She then asks you if you are able to help her find it again. She said she would reward you hansomely.\n")
                    woman = input("What do you do? \na. Help her find the ring \nb. Ignore her and move on.\n")
                    if woman.lower() == "a":
                        print("The woman thanks you, and promises to reward you hansomely if you return the ring.\n")
                        ringQuest = True
                if ring == False and talkedToWoman == True: # TIP
                    print("The woman says 'I might have dropped it while talking to my friend in the archery shop.' (Tip - Look in the Archery Shop)\n")
                if ring == True and talkedToWoman == True: # FINISH QUEST, REWARD
                    print("The woman thanks you dearly and says: 'You have no idea how much this means to me! Here you go, have 50 coins as a thank you.'\n")
            if townsFolkQuest == 2:
                if largeWolfDead == False and talkedToFarmer == False: # NEW QUEST
                    print("When looking around for someone to talk to, you a distraught farmer stands out to you. You approach him, and ask him what is wrong.\n")
                    time.sleep(2)
                    print("He then mentions that nearly all of his livestock have been either stolen from his farmland, or eaten alive. He suspects a large wolf has been terrorizing the animals in his and other's farms. He will reward you hansomely if you fulfill his offer.\n")
                    farmer = input("What do you do? \na. Help the farmer kill the wolf \nb. Decline his offer.\n")
                    talkedToFarmer = True
                    if farmer.lower() == "a":
                        talkedToFarmer == True
                        print("The farmer thanks you, and tells you the wolf usually hides out right outside the walls of the town.\n")
                    if farmer.lower() == "b":
                        print("You tell the farmer you are not interested, and leave the scene.\n")
                if largeWolfDead == False and talkedToFarmer == True:
                    print("The farmer tells you that the wolf was last spotted directly outside of the gates of the town. (Tip - Leave the town)\n")
                if largeWolfDead == True and talkedToFarmer == True:
                    print("When you show the farmer the trophy, he seems very thankful, and gives you your reward that all of the farmers pooled together.\n")
            if townsFolkQuest == 3:
                if parcelDelivered == False and talkedToMerchant == False:
                    print("When looking around for someone to talk to, a merchant of some sort jumps in front of you. They then ask you if you are willing to deliver a parcel to one of their clients, since they are too busy to do it themselves.\n")
                    time.sleep(2)
                    farmer = input("What do you do? \na. Help the merchant deliver the goods *unharmed* \nb. Decline his offer\n")
                    if farmer.lower() == "a":
                        print("You decide to help the merchant.\n")
                    if farmer.lower() == "b":
                        print("You decline the merchant's offer, and walk away.\n")
                if parcelDelivered == False and talkedToMerchant == True:
                    print("You overhear the merchant saying 'I could've sworn my client was over by the fountain over there.' (Tip - Look at the fountain)\n")
                if parcelDelivered == True and talkedToMerchant == True:
                    print("The merchant thanks you for your service to him, and hands you a handful of coins worth 40 coins.\n")
        if town.lower() == "c":
            if parcelDelivered == False and talkedToMerchant == True:
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
                        if parcelDelivered == True:
                            print("The woman thanks you again for delivering the parcel.\n")
                        if parcelDelivered == False:
                            print("The woman thanks you for delivering the parcel. (Tip - You may now go back to the merchant to claim your reward)\n")
                    if fountain.lower() == "c":
                        print("You left the fountain.")
        if town.lower() == "d":
            print("As you are leaving the town's gates, a villager approaches you and says: 'Be careful, they don't call it 'Dread Forest' for nothing.' Taking this into consideration, you venture out into the neighbouring forest.\n")
            town = False
            print("You stand outside the gates to the town facing the forest, you can either go back into town or continue going deeper into the forest.")
            forest = input("What do you do? \na. Turn back around and go into town \nb. Continue deeper into the 'Dread Forest'")
            if forest.lower() == "a":
                town = True
                print("You walk back into town.")
                time.sleep(2)
            if forest.lower() == "b":
                print("You are walking through the forest away from the town, and an eerie chill runs down your spine, as if something is watching you from the deep forest beside you.\n")
                if talkedToFarmer == True and largeWolfDead == False:
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
                                if bow:
                                    if arrows >= 1:
                                        bowHitChance = random.randint(30, 60)
                                        print(f"You hit the large wolf for {bowDamage} damage!\n")
                                        print(f"You now have {arrows} arrows left!\n")
                                    else:
                                        print("You do not have enough arrows to shoot at the large wolf. Try using another weapon.\n")
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
                                        areYouSure = input("This will erase all of your progress - Are you sure?\n")
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
                                        print(f"You ate one luxurious food!")
                                        health = maxHealth
                                        health -= 1
                                    if luxuriousFood < 1:
                                        print("You don't have enough food for that!")
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
                            print("You take the head as a trophy, and resolve to return to town to collect your reward from the farmer.")
                print("")
