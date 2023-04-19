from proj10 import check_for_win
import cards

# create 4 aces
c1 = cards.Card(1,1)
c2 = cards.Card(1,2)
c3 = cards.Card(1,3)
c4 = cards.Card(1,4)

stock = cards.Deck()
# empty the stock
for i in range(50):
    stock.deal()

tableau = [[c1],[],[c2,c3],[c4]]
print("stock.is_empty():",stock.is_empty())
print("tableau:",tableau)
win = check_for_win( tableau, stock )
print("check_for_win:",win)
assert win == False
print("-"*20)
      
stock = cards.Deck()
# empty the stock
for i in range(52):
    stock.deal()

tableau = [[c1],[],[c2,c3],[c4]]
print("stock.is_empty():",stock.is_empty())
print("tableau:",tableau)
win = check_for_win( tableau, stock )
print("check_for_win:",win)
assert win == True
print("-"*20)

c5 = cards.Card(13,4)
tableau = [[c1],[],[c5,c3],[c4]]
print("stock.is_empty():",stock.is_empty())
print("tableau:",tableau)
win = check_for_win( tableau, stock )
print("check_for_win:",win)
assert win == False
print("-"*20)

tableau = [[c1],[c2],[c3],[c4]]
print("stock.is_empty():",stock.is_empty())
print("tableau:",tableau)
win = check_for_win( tableau, stock )
print("check_for_win:",win)
assert win == True
print("-"*20)

c6 = cards.Card(11,3)
tableau = [[c1],[c2],[c5,c3],[c4,c6]]
print("stock.is_empty():",stock.is_empty())
print("tableau:",tableau)
win = check_for_win( tableau, stock )
assert win == False
print("check_for_win:",win)
