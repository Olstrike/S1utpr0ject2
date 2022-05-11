import resources
from resources import Character, Goblin, save_character, load_characters, create_character
from random import randint, shuffle, choice

diffeculty = input("What diffeculty would you like to play? \n Easy, Normal, Hard or Impossible?: ")
#svårighets-grad. Enkel if sats för att förändra skada, hälsa och rustnings värdena.
if diffeculty == Easy:
    Goblin_damage = ...
    Goblin_health = ...
    Goblin_armor = ...
    Skeleton_damage = ...
    Skeleton_health = ...
    Skeleton_armor = ...
    Ork_damage = ...
    Ork_health = ...
    Ork_armor = ...







def fight(players : list, enemies : list):
    participants = players + enemies # skapa initiativordning 
    shuffle(participants)
    
    for char in participants:
        target = ""
        # är karaktären en spelare eller en goblin?
        if char in players:
            target = choice(enemies)
        else:
            target = choice(players)
            
        target.take_damage(char.get_attack())
        
        if target.get_health() == 0:
            print(f"{target.get_name()} has died!")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} has {target.get_health()} hp remaining.")
        
        if len(enemies) == 0 or len(players) == 0:
            break
            
    
if __name__ == "__main__":
    enemies = []
    players = load_characters()
    #players = []
    
    # emy = Character("Emy", 20, 5, 2)
    # nick = Character("Nick", 15, 2, 1)
    # players.append(emy)
    # players.append(nick)

    print("Do you want to create new characters?")
    create_new = input("(y/n): ")
    if(create_new.lower() == "y"):
        how_many = int(input("How many?: "))
        for i in range(how_many):
            players.append(create_character())

    amount_of_goblins = int(input("How many goblins do you want to fight?: "))
    for i in range(amount_of_goblins):
        enemies.append(Goblin(randint(10, 15), randint(0, 2), i+1))
    

    
    round = 1
    while len(enemies) != 0 and len(players) != 0:
        print(f"ROUND {round}, FIGHT!")
        fight(players, enemies)
        print()
        round +=1
    
    if len(enemies) == 0:
        print("The players won!")
        print("Would you like to save the remaining characters?")
        save_progress = input("(y/n): ")
        if save_progress == "y":
            save_character(players)
        else:
            print("No progress was saved.")
        
    elif len(players) == 0:
        print("The Goblins won!")
    