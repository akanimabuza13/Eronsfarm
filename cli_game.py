import random
from colorama import Fore, Style

class Farm:
    def __init__(self):
        self.crops = []
        self.money = 100
        self.season = 'Spring'

    def plant_crop(self, crop):
        self.crops.append(crop)
        print(Fore.GREEN + f'You have planted {crop.name}!' + Style.RESET_ALL)

    def water_crop(self, crop):
        crop.water()
        print(Fore.BLUE + f'You have watered {crop.name}!' + Style.RESET_ALL)

    def harvest_crop(self, crop):
        if crop.is_ready():
            self.money += crop.value
            self.crops.remove(crop)
            print(Fore.YELLOW + f'You have harvested {crop.name}!' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'{crop.name} is not ready to harvest yet!' + Style.RESET_ALL)

    def display_farm(self):
        print(Fore.MAGENTA + "Farm Overview:" + Style.RESET_ALL)
        for crop in self.crops:
            print(crop)
        print(Fore.CYAN + f'Total Money: ${self.money}' + Style.RESET_ALL)

class Crop:
    def __init__(self, name, growth_time, value):
        self.name = name
        self.growth_time = growth_time
        self.value = value
        self.age = 0

    def water(self):
        self.age += 1

    def is_ready(self):
        return self.age >= self.growth_time

def shop():
    print(Fore.LIGHTYELLOW_EX + "Welcome to the Shop! You can buy seeds here." + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "1. Carrot - $10" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "2. Potato - $15" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "3. Wheat - $20" + Style.RESET_ALL)

def main():
    farm = Farm()
    while True:
        print(Fore.LIGHTYELLOW_EX + "Options: plant, water, harvest, shop, display, exit" + Style.RESET_ALL)
        choice = input(Fore.LIGHTWHITE_EX + "What would you like to do? " + Style.RESET_ALL)

        if choice == 'plant':
            crop_choice = input(Fore.LIGHTWHITE_EX + "Which crop would you like to plant? (Carrot/Potato/Wheat) " + Style.RESET_ALL)
            if crop_choice.lower() == 'carrot':
                farm.plant_crop(Crop('Carrot', 3, 10))
            elif crop_choice.lower() == 'potato':
                farm.plant_crop(Crop('Potato', 5, 15))
            elif crop_choice.lower() == 'wheat':
                farm.plant_crop(Crop('Wheat', 7, 20))
            else:
                print(Fore.RED + "Invalid crop choice!" + Style.RESET_ALL)

        elif choice == 'water':
            crop_name = input(Fore.LIGHTWHITE_EX + "Which crop would you like to water? " + Style.RESET_ALL)
            for crop in farm.crops:
                if crop.name.lower() == crop_name.lower():
                    farm.water_crop(crop)
                    break
            else:
                print(Fore.RED + "This crop is not on your farm." + Style.RESET_ALL)

        elif choice == 'harvest':
            crop_name = input(Fore.LIGHTWHITE_EX + "Which crop would you like to harvest? " + Style.RESET_ALL)
            for crop in farm.crops:
                if crop.name.lower() == crop_name.lower():
                    farm.harvest_crop(crop)
                    break
            else:
                print(Fore.RED + "This crop is not on your farm." + Style.RESET_ALL)

        elif choice == 'shop':
            shop()

        elif choice == 'display':
            farm.display_farm()

        elif choice == 'exit':
            print(Fore.LIGHTGREEN_EX + "Thanks for playing!" + Style.RESET_ALL)
            break

if __name__ == '__main__':
    main()