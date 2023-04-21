from proj10 import check_for_win
import cards
import unittest

def compare_stocks(stock1,stock2):  # necessary because Deck __eq__ does not exist
    '''return True if stocks are identical; False otherwise'''
    if len(stock1) != len(stock2):
        return False
    for i in range(len(stock1)):
        if stock1.deal() != stock2.deal():
            return False
    return True

class test_check_for_win(unittest.TestCase):
    def test_check_for_win(self):
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


if __name__ == '__main__':
    unittest.main()
