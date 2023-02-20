from art import logo
# module random
import random
import os
clear = lambda: os.system('cls')

while True:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    while play_game != 'y' and play_game != 'n':
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if play_game == 'y':
        clear()
        # logo
        print(logo)
    
        cards_game = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
        my_cards = []
        dealer_cards = []
    
        # add cards
        def sum_cards(added_cards):
            sum = 0
            for card in added_cards:
                sum += card
            return sum
        # add cards in my cards array or dealer_cards
        def add_cards(cards, first_hand):
            # my card
            card = random.choice(cards_game)
            # add my card to my_cards list
            cards.append(card)
            if first_hand:
                card = random.choice(cards_game)
                # add my card to my_cards list
                cards.append(card)
    
            return cards
        # ace value changed from 11 to 1
        def soft_hand(cards_list, tot_cards):
            if tot_cards(cards_list) > 21:
                for card_num, card in enumerate(cards_list):
                    if card == 11:
                        cards_list[card_num] = 1
                        break
            
        # show current score
        def show_current_score(my_cards, sum_cards, dealer_cards):
            current_score = print(
                f'Your cards: {my_cards}, current score: {0 if (len(my_cards) == 2 and sum_cards(my_cards) == 21) else sum_cards(my_cards)}')
           
            dealer_first_score = print(f'Computer\'s first card: {dealer_cards[0]}')
        # show final score 
        def show_final_score(my_final_cards, final_cards_sum, final_dealer_cards):
            final_score = print(f'Your final hand: {my_final_cards}, final score: {0 if (len(my_final_cards) == 2 and final_cards_sum(my_final_cards) == 21) else final_cards_sum(my_final_cards)}')
            
            dealer_final_score = print(f'Computer\'s final hand: {final_dealer_cards}, final score: {0 if (len(final_dealer_cards) == 2 and final_cards_sum(final_dealer_cards) == 21) else final_cards_sum(final_dealer_cards)}')
        # win lose draw conditions
        def win_lose_draw_conditions(sum, compare):
            if sum(my_cards) > 21:
                show_final_score(my_cards, sum_cards, dealer_cards)
                print('You went over. You lose 😭')
            if compare:
                if sum(dealer_cards) > 21:
                    print('Opponent went over. You win 😁')
                elif (sum(my_cards) > sum(dealer_cards)) or (sum(my_cards) == 21 < sum(dealer_cards)):
                    print('You win 😃')
                elif sum(my_cards) < sum(dealer_cards): 
                    print('You lose 😤')
                else:
                    print('Draw 🙃')

        # get cards
        def get_cards():
            add_cards(my_cards, True)
            soft_hand(cards_list=my_cards, tot_cards=sum_cards) 
            add_cards(dealer_cards, True)
            soft_hand(cards_list=dealer_cards, tot_cards=sum_cards) 
             
            while sum_cards(dealer_cards) < 17:
                add_cards(dealer_cards, False)
                soft_hand(cards_list=dealer_cards, tot_cards=sum_cards)  
            
            show_current_score(my_cards, sum_cards, dealer_cards)
            
            while True:
                if sum_cards(my_cards) == 21 and sum_cards(dealer_cards) == 21 and len(dealer_cards) == 2 and len(my_cards) == 2:
                    show_final_score(my_final_cards=my_cards, final_cards_sum=sum_cards, final_dealer_cards=dealer_cards)
                    print('Draw 🙃')
                    break
                elif sum_cards(my_cards) == 21 and len(my_cards) == 2:
                    show_final_score(my_final_cards=my_cards, final_cards_sum=sum_cards, final_dealer_cards=dealer_cards)
                    print('Win with a Blackjack 😎')
                    break
                elif sum_cards(dealer_cards) == 21 and len(dealer_cards) == 2:
                    show_final_score(my_final_cards=my_cards, final_cards_sum=sum_cards, final_dealer_cards=dealer_cards)
                    print('Lose, opponent has Blackjack 😱')
                    break
                elif sum_cards(my_cards) < 21:
                    another_card = input('Type \'y\' to get another card, type \'n\' to pass: ')
        
                    while another_card != 'y' and another_card != 'n':
                        another_card = input('Type \'y\' to get another card, type \'n\' to pass: ')
        
                    if another_card == 'y':
                        add_cards(my_cards, False)
                        soft_hand(cards_list=my_cards, tot_cards=sum_cards)
                    
                        show_current_score(my_cards, sum_cards, dealer_cards)
                        
                    else:
                        show_final_score(my_final_cards=my_cards, final_cards_sum=sum_cards, final_dealer_cards=dealer_cards)
                        win_lose_draw_conditions(sum=sum_cards, compare=True)
                        break
                elif sum_cards(my_cards) > 21:
                    win_lose_draw_conditions(sum=sum_cards, compare=False)
                    break
                elif sum_cards(my_cards) == 21:
                    show_final_score(my_cards, sum_cards, dealer_cards)
                    win_lose_draw_conditions(sum=sum_cards, compare=True)
                    break
                    
        get_cards()
    else:
        break