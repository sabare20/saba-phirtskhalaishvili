from random import choice

def change_card(dast, players_cards, player):
    player_cards = players_cards[player]
    print(f'{player} - {player_cards}')
    
    while True:
        try:
            card_for_change = input('Enter card which you want to change: ')
            if card_for_change not in player_cards:
                raise ValueError("The card you entered is not in your hand. Please try again.")
            break
        except ValueError as e:
            print(e)
    
    dast.append(card_for_change)  
    player_cards.remove(card_for_change)  
    new_card = choice(dast) 
    dast.remove(new_card)  
    player_cards.append(new_card)  
    
    print(f'{card_for_change} changed by {new_card}')
    print(f"{player}'s new hand: {player_cards}")
    players_cards[player] = player_cards  
    return players_cards