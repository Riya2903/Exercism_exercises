"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card == 'J' or card == 'Q' or card == 'K':
        card = 10
    elif card == 'A':
        card = 1
    else:
        card = int(card)
    return int(card)
    
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if card_one == card_two or value_of_card(card_one)== value_of_card(card_two):
        return (card_one,card_two)
    if (value_of_card(card_one)> value_of_card(card_two)):
        return card_one
    if  value_of_card(card_two) > value_of_card(card_one):
        return card_two
    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if card_one == 'A' :
        return 1
    elif card_two == 'A':
        return 1
    else:
        if card_one == 'J' or card_one == 'Q' or card_one == 'K':
            card_one = 10
        if card_two == 'J' or card_two == 'Q' or card_two == 'K':
            card_two = 10
        
        if int(card_one)+ int(card_two)<=10:
                return 11
        else:
                return 1
           


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    if card_one == 'A' and (card_two == 'J' or card_two == 'K' or card_two == 'Q' or card_two == '10'):
        return True
    elif card_two == 'A' and (card_one == 'J' or card_one == 'K' or card_one == 'Q' or card_one == '10'):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    if card_one == card_two:
        return True
    else:
        if (card_one == 'Q' and card_two == 'K') or (card_two == 'Q' and card_one == 'K'):
            return True
        else:
            return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    if card_one == 'J' or card_one == 'Q' or card_one == 'K':
        card_one = 10
    elif card_one == 'A':
        card_one= 1
    if card_two == 'J' or card_two == 'Q' or card_two == 'K':
        card_two = 10
    elif card_two == 'A':
        card_two= 1
    card_one = int(card_one)
    card_two = int(card_two)
    if (card_one + card_two == 9) or (card_one + card_two == 11) or (card_one + card_two == 10):
        return True
    else:
        return False