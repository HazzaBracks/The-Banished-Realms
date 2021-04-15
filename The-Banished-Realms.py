# This file will contain all of the main code for The Banished Realms.
#imports
import pygame
import time
coins = 50

#variables

#intro
intro = input("Welcome to The Banished Realms, a medieval text-based input rpg - Would you like to play? (y/n)")
  if intro.lower() == "n":
    print("Then why are you here? Go do something else!")
  if intro.lower() == "y":
    print("Glad to hear it! - Your glorious adventure awaits!")
    time.sleep(1)
    print("You wake up in a small, but messy tent, which sounds as though it is in the middle of a tranquil forest,")
    print("with the wind whispering through the leaves, and many a bird chirping in the distance.")
    print("When you look through the open flaps of the tent, you see a slowly dying campfire stationed directly in front of your tent.")
    print("There is also a large backpack sitting to your left, and a few small snacks as well as a wooden shortsword on your right.")
    campsite = input("What do you do? \n a. Fill the backpack with the sword and leave the campsite \n b. Leave without backpack and items \n c. Continue to inspect the campsite
      if campsite.lower() == "c":
        print("You continued to search the surrounding area, and found a small purse of 50 golden coins, and a large, heavy, axe lodged in a tree stump.")
          campinspected = input(Now that you have inspected the campsite, do you choose to leave it with or without the backpack? \n a. Leave with backpack \n b. Leave without backpack”)
