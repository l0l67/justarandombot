import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = []
def round1(cards):
    global player_ges
    global d_card1
    global d_card2
    global card1
    global card2
    player_ges = int()
    card1 = random.choice(values)
    cards.append(card1)
    card2 = random.choice(values)
    cards.append(card2)
    d_card1 = random.choice(values)
    d_card2 = random.choice(values)
    player_ges += card1 + card2

def round2(cards):
    global card3
    card3 = random.choice(values)
    cards.append(card3)
    player_ges += card3
