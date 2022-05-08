from asyncio import run
import random

# dictionaries holding health and each different attack and how much damage it deals
hercules = {
    'health': 215, 
    'grace': 10,
    'confuse': 15,
    'bash': 20,
    'ravage': 35
}
hercules_list = list(hercules.values())

nemean_lion = {
    'health': 175,
    'bounce': 10,
    'overpower': 15,
    'blight': 20,
    'reckoning': 35
}
lion_list = list(nemean_lion.values())

lernaean_hydra = {
    'health': 200,
    'mislead': 10,
    'whip': 15,
    'bombard': 20,
    'thrash': 35
}
hydra_list = list(lernaean_hydra.values())

cerberus = {
    'health': 250,
    'rumble': 10,
    'slam': 15,
    'maul': 20,
    'fury': 35
}
cerberus_list = list(cerberus.values())

# function for the fight against the nemean lion
def attack_lion ():
    print('')
    print('The Nemean Lion is starting with 175 health. You are starting with 215 health.')
    while nemean_lion['health'] > 0 and hercules['health'] > 0:
        user_input = input('''
        Which attack do you want to perform?\n
        [a]: grace, [b]: confuse, [c]: bash, or [d]: ravage\n
        Enter a, b, c, or d: ''')
        if user_input == 'a':
            nemean_lion['health'] -= hercules['grace']
            lion_damage = lion_list[random.randint(1, 4)]
            hercules['health'] -= lion_damage
            print(f'\nYou graced the Nemean Lion with your attack and dealt 10 damage. The lion\'s health is now at {nemean_lion["health"]}.')
            if lion_damage == lion_list[1]:
                print(f'\nThe Nemean Lion bounced on you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[2]:
                print(f'\nThe Nemean Lion overpowered you and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[3]:
                print(f'\nThe Neamean Lion blighted you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[4]:
                print(f'\nThe Neamean Lion reckoned you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'b':
            nemean_lion['health'] -= hercules['confuse']
            lion_damage = lion_list[random.randint(1, 4)]
            hercules['health'] -= lion_damage
            print(f'\nYou confused the Nemean Lion and dealt 15 damage. The lion\'s health is now at {nemean_lion["health"]}')
            if lion_damage == lion_list[1]:
                print(f'\nThe Nemean Lion bounced on you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[2]:
                print(f'\nThe Nemean Lion overpowered you and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[3]:
                print(f'\nThe Neamean Lion blighted you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[4]:
                print(f'\nThe Neamean Lion reckoned you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'c':
            nemean_lion['health'] -= hercules['bash']
            lion_damage = lion_list[random.randint(1, 4)]
            hercules['health'] -= lion_damage
            print(f'\nYou bashed the Nemean Lion and dealt 20 damage. The lion\'s health is now at {nemean_lion["health"]}')
            if lion_damage == lion_list[1]:
                print(f'\nThe Nemean Lion bounced on you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[2]:
                print(f'\nThe Nemean Lion overpowered you and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[3]:
                print(f'\nThe Neamean Lion blighted you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[4]:
                print(f'\nThe Neamean Lion reckoned you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'd':
            nemean_lion['health'] -= hercules['ravage']
            lion_damage = lion_list[random.randint(1, 4)]
            hercules['health'] -= lion_damage
            print(f'\nYou ravaged the Nemean Lion and dealt 35 damage. The lion\'s health is now at {nemean_lion["health"]}')
            if lion_damage == lion_list[1]:
                print(f'\nThe Nemean Lion bounced on you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[2]:
                print(f'\nThe Nemean Lion overpowered you and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[3]:
                print(f'\nThe Neamean Lion blighted you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif lion_damage == lion_list[4]:
                print(f'\nThe Neamean Lion reckoned you and dealt 35 damage. Your health is now at {hercules["health"]}')
    if hercules['health'] > 0 and nemean_lion['health'] <= 0:
        print('\nCongrats! You defeated the Nemean lion. Onto the next enemy, the Lernaean Hydra. Good Luck!')
    else:
        print('\nOh no! The Nemean Lion defeated you! You still have a chance! Onto the next enemy, the Lernaean Hydra. Good luck, you\'re gonna need it!')

# function for the fight against the lernaean hydra
def attack_hydra ():
    hercules['health'] = 215
    print('')
    print('The Lernaean Hydra is starting with 200 health. You are starting with 215 health.')
    while lernaean_hydra['health'] > 0 and hercules['health'] > 0:
        user_input = input('''
        Which attack do you want to perform?\n
        [a]: grace, [b]: confuse, [c]: bash, or [d]: ravage\n
        Enter a, b, c, or d: ''')
        if user_input == 'a':
            lernaean_hydra['health'] -= hercules['grace']
            hydra_damage = hydra_list[random.randint(1, 4)]
            hercules['health'] -= hydra_damage
            print(f'\nYou graced the Lernaean Hydra with your attack and dealt 10 damage. The hydra\'s health is now at {lernaean_hydra["health"]}.')
            if hydra_damage == hydra_list[1]:
                print(f'\nThe Lernaean Hydra mislead you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[2]:
                print(f'\nThe Lernaean Hydra whipped you with its tail and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[3]:
                print(f'\nThe Lernaean Hydra bombarded you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[4]:
                print(f'\nThe Lernaean Hydra thrashed you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'b':
            lernaean_hydra['health'] -= hercules['confuse']
            hydra_damage = hydra_list[random.randint(1, 4)]
            hercules['health'] -= hydra_damage
            print(f'\nYou confused the Lernaean Hydra and dealt 15 damage. The hydra\'s health is now at {lernaean_hydra["health"]}')
            if hydra_damage == hydra_list[1]:
                print(f'\nThe Lernaean Hydra mislead you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[2]:
                print(f'\nThe Lernaean Hydra whipped you with it\'s tail and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[3]:
                print(f'\nThe Lernaean Hydra bombarded you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[4]:
                print(f'\nThe Lernaean Hydra thrashed you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'c':
            lernaean_hydra['health'] -= hercules['bash']
            hydra_damage = hydra_list[random.randint(1, 4)]
            hercules['health'] -= hydra_damage
            print(f'\nYou bashed the Lernaean Hydra and dealt 20 damage. The hydra\'s health is now at {lernaean_hydra["health"]}')
            if hydra_damage == hydra_list[1]:
                print(f'\nThe Lernaean Hydra mislead you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[2]:
                print(f'\nThe Lernaean Hydra whipped you with it\'s tail and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[3]:
                print(f'\nThe Lernaean Hydra bombarded you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[4]:
                print(f'\nThe Lernaean Hydra thrashed you and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'd':
            lernaean_hydra['health'] -= hercules['ravage']
            hydra_damage = hydra_list[random.randint(1, 4)]
            hercules['health'] -= hydra_damage
            print(f'\nYou ravaged the Lernaean Hydra and dealt 35 damage. The hydra\'s health is now at {lernaean_hydra["health"]}')
            if hydra_damage == hydra_list[1]:
                print(f'\nThe Lernaean Hydra mislead you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[2]:
                print(f'\nThe Lernaean Hydra whipped you with its tail and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[3]:
                print(f'\nThe Lernaean Hydra bombarded you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif hydra_damage == hydra_list[4]:
                print(f'\nThe Lernaean Hydra thrashed you and dealt 35 damage. Your health is now at {hercules["health"]}')
    if hercules['health'] > 0 and lernaean_hydra['health'] <= 0:
        print('\nCongrats! You defeated the Lernaean Hydra. Onto the last enemy, the Cerberus. Good Luck!')
    else:
        print('\nOh no! The Lernaean Hydra defeated you! You still have a chance! Onto the last enemy, the Cerberus. Good luck, you\'re gonna need it!')

# function for the fight against the cerberus
def attack_cerberus ():
    hercules['health'] = 215
    print('')
    print('The Cerberus is starting with 250 health. You are starting with 215 health.')
    while cerberus['health'] > 0 and hercules['health'] > 0:
        user_input = input('''
        Which attack do you want to perform?\n
        [a]: grace, [b]: confuse, [c]: bash, or [d]: ravage\n
        Enter a, b, c, or d: ''')
        if user_input == 'a':
            cerberus['health'] -= hercules['grace']
            cerberus_damage = cerberus_list[random.randint(1, 4)]
            hercules['health'] -= cerberus_damage
            print(f'\nYou graced the Cerberus with your attack and dealt 10 damage. The Cerberus\' health is now at {cerberus["health"]}.')
            if cerberus_damage == cerberus_list[1]:
                print(f'\nThe Cerberus rumbled with you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[2]:
                print(f'\nThe Cerberus slammed you on the ground and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[3]:
                print(f'\nThe Cerberus mauled you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[4]:
                print(f'\nThe Cerberus went into a fury and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'b':
            cerberus['health'] -= hercules['confuse']
            cerberus_damage = cerberus_list[random.randint(1, 4)]
            hercules['health'] -= cerberus_damage
            print(f'\nYou confused the Cerberus and dealt 15 damage. The Cerberus\' health is now at {cerberus["health"]}')
            if cerberus_damage == cerberus_list[1]:
                print(f'\nThe Cerberus rumbled with you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[2]:
                print(f'\nThe Cerberus slammed you on the ground and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[3]:
                print(f'\nThe Cerberus mauled you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[4]:
                print(f'\nThe Cerberus went into a fury and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'c':
            cerberus['health'] -= hercules['bash']
            cerberus_damage = cerberus_list[random.randint(1, 4)]
            hercules['health'] -= cerberus_damage
            print(f'\nYou bashed the Cerberus and dealt 20 damage. The Cerberus\' health is now at {cerberus["health"]}')
            if cerberus_damage == cerberus_list[1]:
                print(f'\nThe Cerberus rumbled with you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[2]:
                print(f'\nThe Cerberus slammed you on the ground and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[3]:
                print(f'\nThe Cerberus mauled you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[4]:
                print(f'\nThe Cerberus went into a fury and dealt 35 damage. Your health is now at {hercules["health"]}')
        elif user_input == 'd':
            cerberus['health'] -= hercules['ravage']
            cerberus_damage = cerberus_list[random.randint(1, 4)]
            hercules['health'] -= cerberus_damage
            print(f'\nYou ravaged the Cerberus and dealt 35 damage. The Cerberus\' health is now at {cerberus["health"]}')
            if cerberus_damage == cerberus_list[1]:
                print(f'\nThe Cerberus rumbled with you and dealt 10 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[2]:
                print(f'\nThe Cerberus slammed you on the ground and dealt 15 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[3]:
                print(f'\nThe Cerberus mauled you and dealt 20 damage. Your health is now at {hercules["health"]}')
            elif cerberus_damage == cerberus_list[4]:
                print(f'\nThe Cerberus went into a fury and dealt 35 damage. Your health is now at {hercules["health"]}')
    if hercules['health'] > 0 and cerberus['health'] <= 0:
        print('\nCongrats! You captured the Cerberus! You did well fighting all those enemies!')
    else:
        print('\nOh no! You failed to capture the Cerberus. Better luck next time')

# function to run all other functions
def run_game():
    attack_lion()
    attack_hydra()
    attack_cerberus()

run_game()