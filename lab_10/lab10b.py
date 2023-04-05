import cards

# Create the deck of cards

the_deck = cards.Deck()
# the_deck.shuffle()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( the_deck.deal() )
    player2_list.append( the_deck.deal() )

print("Starting Hands")
print("Hand1:", player1_list)
print("Hand2:", player2_list, "\n")

player_1_score = 0
player_2_score = 0
while True:
    try:
        card_1 = player1_list.pop(0)
    except IndexError:
        break
    try:
        card_2 = player2_list.pop(0)
    except IndexError:
        break
    print("Battle was 1: " + str(card_1) + ", 2: " + str(card_2), ". ", end="")
    if card_1.rank() == card_2.rank():
        print("Tie")
    elif card_1.rank() > card_2.rank():
        print("Player 1 wins battle.")
        player_1_score += 1
        player1_list.append(card_1)
        player1_list.append(card_2)
    else:
        print("Player 2 wins battle.")
        player_2_score += 1
        player2_list.append(card_2)
        player2_list.append(card_1)
    print("hand1:", player1_list)
    print("hand2:", player2_list, "\n")
    if len(player1_list) == 0:
        break
    if len(player2_list) == 0:
        break
    cont = input("Keep Going: (Nn) to stop:")
    if cont in "nN":
        break




if player_1_score > player_2_score:
    print("Player 1 wins!!!")

elif player_1_score < player_2_score:
    print("Player 2 wins!!!")
