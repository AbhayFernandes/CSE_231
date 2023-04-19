

from proj10 import init_game
import cards as cards

def compare_stocks(stock1,stock2):  # necessary because Deck __eq__ does not exist
    '''return True if stocks are identical; False otherwise'''
    if len(stock1) != len(stock2):
        return False
    for i in range(len(stock1)):
        if stock1.deal() != stock2.deal():
            return False
    return True

instructor_stock = cards.Deck()
instructor_stock.shuffle()

instructor_tableau = []
for i in range(4):
    instructor_tableau.append([instructor_stock.deal()])
print("Instructor_stock:",instructor_stock)
print("Instructor Tableau:",instructor_tableau)

stock, tableau, foundation = init_game()

print("Stock:",stock)
print("Tableau:", tableau)
print("Foundation:",foundation)

print("Comparing stocks:")
assert compare_stocks(stock,instructor_stock) == True
print("Comparing tableau:")
assert tableau == instructor_tableau
print("Comparing foundation:")
assert foundation == []