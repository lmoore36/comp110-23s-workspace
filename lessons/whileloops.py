"""Lesson 6 - While Loops Video"""

cards: str = "5235"

card_idx: int = 0
low_card: int = int(cards[0])
#look for each number in the string
while card_idx < 4:
    """print(cards[card_idx])"""
    #check if current card is less thatn low card
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        #update the low card to be the value of current card
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)