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
            if backpackSword or sword:
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
                    print("You missed your swing, and now you are vulnerable.\n")
                    wolfDamage = random.randint(10, 30)
                    print(f"The wolf then swung at you for {wolfDamage} damage!\n*You lose {wolfDamage} health*\n")
                    health -= wolfDamage
                    time.sleep(2)

            if wolfHealth > 0:
                print(f"The wolf now has {wolfHealth} health!")
                wolfDamage = random.randint(10, 30)
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
                    print("Glad to hear it!")
                    wolfAlive = True
                if playagain.lower() == "n":
                    areYouSure = input("This will erase all of your progress - Are you sure?\n")
                    if areYouSure.lower() == "n":
                        print("Glad to hear it!\n")
                        wolfAlive = True
                    if areYouSure.lower() == "y":
                        break
                        playGame = False
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
                    print("You missed your swing, and now you are vulnerable.\n")
                    youngBearDamage = random.randint(10, 25)
                    print(f"The young bear then swung at you for {youngBearDamage} damage!\n*You lose {youngBearDamage} health*\n")
                    time.sleep(2)
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
                print("You killed the young bear with one final blow \n*You receive 5 regular food*\n")
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
                        wolfAlive = True
                    if areYouSure.lower() == "y":
                        break
                        playGame = False
if enemyEncounter == 2:
    print("While walking through a meadow, you hear a lot of screeching and snorting, and then all of a sudden a wild boar runs up to you.\n")
    boar = input("What do you do? \n a. Attack the boar \n b. Run away\n")
    if boar.lower() == "b":
        if backpackAxe or backpackSword == True:
            print("You somehow got away from the wild boar, but it managed to create a deep gash in your left arm, causing you to lose a substantial amount of health. \n*You lose 30 health points*\n")
            health -= 30
            time.sleep(2)
            print(f"Your health is now {health}")
        if backpackAxe and backpackSword == False:
            print("Since you didn't have any heavy objects weighing you down, you managed to get away unscathed.\n")
    if boar.lower() == "a":
        boarAlive = True
        while boarAlive:
            if sword or backpackSword:
                swordDamage = random.randint(30, 50)
                print(f"You hit the boar for {swordDamage} damage!\n")
                boarHealth -= swordDamage
                time.sleep(2)
            if woodAxe or backpackAxe:
                axeHitChance = random.randint(0, 100)
                if axeHitChance <= 75:
                    axeDamage = random.randint(40, 60)
                    print(f"You hit the boar for {axeDamage} damage!\n")
                    boarHealth -= axeDamage
                    time.sleep(2)
                else:
                    print("You missed your swing, and now you are vulnerable.\n")
                    boarDamage = random.randint(20, 40)
                    print(f"The boar then swung at you for {boarDamage} damage!\n*You lose {boarDamage} health*\n")
                    time.sleep(2)
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
                print("You killed the boar with one final blow \n*You receive 8 regular food*\n")
                boarAlive = False
            if health <= 0:
                playagain = input("You Died - Would you like to play again? y/n\n")
                if playagain.lower() == "y":
                    print("Glad to hear it!")
                    youngBearAlive = True
                if playagain.lower() == "n":
                    areYouSure = input("This will erase all of your progress - Are you sure?\n")
                    if areYouSure.lower() == "n":
                        print("Glad to hear it!")
                        wolfAlive = True
                    if areYouSure.lower() == "y":
                        break
                        playGame = False
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
                    print("You missed your swing, and now you are vulnerable.\n")
                    thugDamage = random.randint(15, 30)
                    print(f"The thug then swung at you for {thugDamage} damage!\n*You lose {thugDamage} health*\n")
                    time.sleep(2)
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
                print("You knocked out the thug with one final blow \n*You receive 50 coins and a small snack from their pocket*\n")
                regularFood += 1
                coins += 50
                thugAlive = False
            if health <= 0:
                playagain = input("You Died - Would you like to play again? y/n\n")
                if playagain.lower() == "y":
                    print("Glad to hear it!\n")
                    youngBearAlive = True
                if playagain.lower() == "n":
                    areYouSure = input("This will erase all of your progress - Are you sure?\n")
                    if areYouSure.lower() == "n":
                        print("Glad to hear it!\n")
                        thugAlive = True
                    if areYouSure.lower() == "y":
                        break
                        playGame = False
if wolfAlive or boarAlive or thugAlive or youngBearAlive == False:
    pathToTown = True
if pathToTown == True:
    time.sleep(1)
    print("After making your way through the forest, you finally make it to a small village situated on the edge of the forest.")
    time.sleep(2)
    print("The village is a bustling area, with people walking around, talking, with children playing. There was a glistening fountain in the center of a large square.")
    time.sleep(2)
    print("There we were also several shops in the buildings, that seemed to be quite popular.")
    time.sleep(2)
    town = True
    while town:
        town = input("What do you do? \na. Visit the shops \nb. Talk to the townspeople \nc. Drink from the fountain \nd. Leave the town\n")
        if town.lower() == "a":
            print("You decide that you should walk around town and see what shops are available. After a short stroll through the village, you found 2 shops scattered around the town.")
            whichShop = input("Which shop do you go to? \na. The archery shop \nb. The armor shop \n")
            if whichShop.lower() == "a":
                if coins < 30:
                    print("After looking around the shop, you can see that the only thing you can afford is a bundle of arrows, for which you have no current use.")
                if coins >= 30:
                    print(f"After looking around the shop, you can see that you are able to afford a bow, and {coins - 30} arrows.")
                    archeryShop = True
                    while archeryShop == True and coins > 0:
                        if coins >= 30:
                            archeryShop = input("What do you do? \na. Buy a bow (Lower hit chance, Higher damage) (30 coins) \nb. Buy a bundle of 10 arrows (10 coins)")
                            if archeryShop.lower() == "a" and coins >= 30:
                                print("You bought a bow")
                                bow = True
                        if coins < 30:
                            archeryShop = input("What do you do? \na. Buy a bundle of 10 arrows (10 coins)")
                            if archeryShop.lower() == "a" and coins >= 10:
                                arrows += 10
                        if coins < 0:
                            coins = 0
                            archeryShop = False
                            time.sleep(1)
                            print("You left the shop because you no longer had any coins.")
            if whichShop.lower() == "b":
                if coins < 30:
                    print("After looking around the shop, you cannot afford anything. You then leave the shop")
                if coins >= 30:
                    armorShop = True
                    while armorShop and coins > 30:
                        if coins in range(30,39):
                            print("After looking around the shop, you can see that you are only able to afford a small set of boots.")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "b":
                                print("You left the the shop.")
                                armorShop = False
                        if coins in range(40,49):
                            print("After looking around the shop, you can see that you are only able to afford a small set of steel boots, and some chainmail leggings.")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "c":
                                print("You left the the shop.")
                                armorShop = False
                        if coins in range(50,59):
                            print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, and a chainmail helmet.")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "c" and chainmailHelmet == False:
                                maxHealth += 35
                                coins -= 50
                                print(f"You bought the chainmail helmet, and your Maximum Health went up by 35, to {maxHealth}")
                                chainmailHelmet = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "d":
                                print("You left the the shop.")
                                armorShop = False
                        if coins in range(60,80):
                            print("After looking around the shop, you can see that you are able to afford a small set of steel boots, some chainmail leggings, a chainmail helmet, and a steel chestplate.")
                            armorShop = input("What do you do? \na. Buy the Boots (30 coins)\nb. Buy the chainmail leggings (40 coins)\nc. Buy the chainmail helmet (50 coins)\nd.Buy the steel chestplate (60 coins)\ne. Leave the shop\n")
                            if armorShop.lower() == "a" and chainmailBoots == False:
                                maxHealth += 15
                                coins -= 30
                                print(f"You bought the pair of boots, and your Maximum Health went up by 15, to {maxHealth}")
                                chainmailBoots = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "b" and chainmailLeggings == False:
                                maxHealth += 25
                                coins -= 40
                                print(f"You bought the chainmail leggings, and your Maximum Health went by 25, to {maxHealth}")
                                chainmailLeggings = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "c" and chainmailHelmet == False:
                                maxHealth += 35
                                coins -= 50
                                print(f"You bought the chainmail helmet, and your Maximum Health went up by 35 to {maxHealth}")
                                chainmailHelmet = True
                                time.sleep(2)
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "d" and steelChestplate == False:
                                maxHealth += 45
                                coins -= 60
                                print(f"You bought the steel chestplate, and your Maximum Health went up by 35, to {maxHealth}")
                                steelChestplate = True
                            else:
                                print("You have already purchased this item!")
                                time.sleep(2)
                            if armorShop.lower() == "e":
                                print("You left the the shop.")
                                armorShop = False
                        if coins < 30:
                            print("There is nothing in the store that you can buy, since you do not have enough coins to buy anything.")
                            armorShop = False
        if town.lower() == "b":
            print("You walk around the village, looking for someone to talk to, you see a man wearing farmer's clothes, who seems to be upset about something. You go up to him and ask him what's wrong.")
            time.sleep(2)
            print("He tells you that all of his livestock has been eaten alive, one has dissapeared each day, and he only has a few left.")
            time.sleep(2)
            print("He then asks if you are able to help him.")
            farmer = input("What do you do? \na. Visit his farm to inspect the scene \nb. Ignore him, and go talk to someone else.\n")
