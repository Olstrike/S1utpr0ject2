from random import randint, choice

from Main import Goblin_damage, Skeleton_armor, Skeleton_damage, Skeleton_health

# globala vareabler

class Weapon: 
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage
    
    def get_damage(self):
        return self.damage

#BRYTER MOT STANDARD


class Character:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
        self.generate_weapon()
        self.attack = self.weapon.get_damage()
        
    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    

    def generate_weapon(self):
        random_weapon = randint(0, 98)
        if random_weapon < 20: self.weapon = Weapon("Shortsword", 3)
        if random_weapon >= 20 and random_weapon < 40: self.weapon = Weapon("Broadsword", 5)
        if random_weapon >= 40 and random_weapon < 60: self.weapon = Weapon("Small Knife", 1)
        if random_weapon >= 60 and random_weapon < 80: self.weapon = Weapon("Spear", 2)
        if random_weapon >= 80 and random_weapon < 60: self.weapon = Weapon("Halberd", 4)
        if random_weapon >= 90 and random_weapon < 95: self.weapon = Weapon("Morning Star", 6)
        if random_weapon == 96: self.weapon = Weapon("Sword of Khaine", 50)
        if random_weapon == 97: self.weapon = Weapon("Valyrian steel sword", 20)
        if random_weapon == 98: self.weapon = Weapon("Dildo", 100)





    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_attack(self): # tidigare damage
        return self.attack

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def get_attributes(self):
        return self.name, self.health, self.attack, self.armor

#Här skapar jag de motståndarna som finns och ger dem koden som gör att de funkar.
class goblin:
    def __init__(self, health, armor, id):
            self.health = health
            self.armor = armor
            self.id = id
            self.weapon = choice(Goblin_damage)
            self.attack = self.weapon.get_damage()
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
        
    def __str__(self) -> str:
        return f"Goblin #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Goblin #{self.id}"
    
class skeleton:
    def __init__(self, health, armor, id):
            self.health = Skeleton_health
            self.armor = Skeleton_armor
            self.id = id
            self.weapon = Skeleton_damage
            self.attack = self.weapon.get_damage()
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
        
    def __str__(self) -> str:
        return f"Skeleton #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Skeleton #{self.id}"

class ork:
    def __init__(self, health, armor, id):
            self.health = health
            self.armor = armor
            self.id = id
            self.weapon = choice(Ork_WEAPONS)
            self.attack = self.weapon.get_damage()
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
        
    def __str__(self) -> str:
        return f"Ork #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Ork #{self.id}"

class darkelf:
    def __init__(self, health, armor, id):
            self.health = health
            self.armor = armor
            self.id = id
            self.weapon = choice(Darkelf_WEAPONS)
            self.attack = self.weapon.get_damage()
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
        
    def __str__(self) -> str:
        return f"Darkelf #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Darkelf #{self.id}"

class high_demon:
    def __init__(self, health, armor, id):
            self.health = health
            self.armor = armor
            self.id = id
            self.weapon = choice(Demon_WEAPONS)
            self.attack = self.weapon.get_damage()
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
        
    def __str__(self) -> str:
        return f"High-demon #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Demon #{self.id}"

    
    def __init__(self, health, armor, id):
        self.health = health
        self.armor = armor
        self.id = id
        self.weapon = choice(GOBLIN_WEAPONS)
        self.attack = self.weapon.get_damage()
        
    def __str__(self) -> str:
        return f"Goblin #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Goblin #{self.id}"
#----------------------    

def save_character(chars : list()):
    save_list = []
    for character in chars:
        name, health, attack, armor = character.get_attributes()
        save_string = f"{name}/{health}/{armor}\n"
        save_list.append(save_string)
        
    with open("saved_characters.txt", "w", encoding="utf8") as f:
        for line in save_list:
            f.write(line)
        print("Characters has been saved!")

def load_characters():
    characters = []
    with open("saved_characters.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             int(attributes[1]),
                             int(attributes[2]))
            
            characters.append(char)
    return characters    

def create_character():
    print("Welcome to the Character creator!")
    name = input("what is your characters name?: ")
    health = randint(10, 30)
    armor = randint(0, 5)

    return_char = Character(name, health, armor)

    print()
    print(return_char)
    print("Character has been created")
    return return_char