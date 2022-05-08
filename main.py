import random

# dictionaries holding health and each different 
# attack and how much damage it deals
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
    'smash': 15,
    'maul': 20,
    'fury': 35
}
cerberus_list = list(cerberus.values())

# function to choose which attack you want hercules to do
def attack_lion ():
    print('')
    print('The Nemean Lion is starting with 175 health. You are starting with 215 health.')
    global lion_damage
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
        print('Oh no! The Nemean Lion defeated you! You still have a chance! Onto the next enemy, the Lernaean Hydra. Good luck!')
        
 
attack_lion()
