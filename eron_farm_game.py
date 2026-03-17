# Enhanced Eron's Farm Game

import random
from colorama import Fore, Back, Style

class Farm:
    def __init__(self):
        self.animals = []
        self.crops = []
        self.security_system = Buster()
        self.shop_items = {'Seeds': 50, 'Fertilizer': 30}
        self.rank = 0

    def plant_crop(self, crop):
        self.crops.append(crop)
        print(Fore.GREEN + f"Planted {crop}.")

    def sell_crop(self, crop):
        if crop in self.crops:
            self.crops.remove(crop)
            print(Fore.BLUE + f"Sold {crop}.")
        else:
            print(Fore.RED + "You don't have that crop!")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(Fore.YELLOW + f"Added {animal} to the farm.")

    def upgrade_security(self):
        self.security_system.upgrade()

class Animal:
    def __init__(self, name):
        self.name = name

class Buster:
    def __init__(self):
        self.level = 1

    def bark(self):
        print(Fore.RED + "Woof Woof! Buster is on duty!")

    def upgrade(self):
        self.level += 1
        print(Fore.YELLOW + "Buster has been upgraded!")

class Shop:
    def __init__(self):
        self.stock = {'Seeds': 50, 'Fertilizer': 30}

    def purchase(self, item):
        if item in self.stock:
            price = self.stock[item]
            print(Fore.CYAN + f"Purchased {item} for {price} coins.")
        else:
            print(Fore.RED + "Item not available.")

class Game:
    def __init__(self):
        self.farm = Farm()
        self.shop = Shop()

    def start(self):
        print(Style.BRIGHT + "Welcome to Eron's Farm!")
        # Game loop here

# Run the game
if __name__ == '__main__':
    game = Game()
    game.start()