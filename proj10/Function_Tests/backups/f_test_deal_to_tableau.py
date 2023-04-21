from proj10 import deal_to_tableau
import cards

def compare_stocks(stock1,stock2):  # necessary because Deck __eq__ does not exist
    '''return True if stocks are identical; False otherwise'''
    if len(stock1) != len(stock2):
        return False
    for i in range(len(stock1)):
        if stock1.deal() != stock2.deal():
            return False
    return True

# initial stock
D = cards.Deck()
for i in range(44):  # remove most cards for easier viewing of results
    D.deal()
print("Stock before:",D)

# final stock
D2 = cards.Deck()
for i in range(48):  # remove most cards for easier viewing of results
    D2.deal()

c1 = cards.Card(1,3)
c2 = cards.Card(2,2)
c3 = cards.Card(3,3)
c4 = cards.Card(4,4)
c5 = cards.Card(5,2)
c6 = cards.Card(6,2)

c7 = cards.Card(1,1)
c8 = cards.Card(2,1)
c9 = cards.Card(3,1)
c10 = cards.Card(4,1)
c11 = cards.Card(5,1)
c12 = cards.Card(6,1)
c13 = cards.Card(7,1)
c14 = cards.Card(8,1)


T = [[c1],[],[c2,c3],[c4,c5,c6]]
print("Tableau before:",T)

deal_to_tableau(T,D)

print("Tableau after:",T)
print("Stock after:",D)

T_after = [[c1,c14],[c13],[c2,c3,c12],[c4,c5,c6,c11]]
assert T == T_after
assert compare_stocks(D,D2) == True