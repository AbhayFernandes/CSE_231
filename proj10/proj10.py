import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    return (None, None, None)  # stub so that the skeleton compiles; delete 
                               # and replace it with your code
    
def deal_to_tableau( tableau, stock):
    pass  # stub; delete and replace it with your code

           
def validate_move_to_foundation( tableau, from_col ):
    return False  # stub; delete and replace it with your code   

    
def move_to_foundation( tableau, foundation, from_col ):
    pass  # stub; delete and replace it with your code   


def validate_move_within_tableau( tableau, from_col, to_col ):
    return False  # stub; delete and replace it with your code



def move_within_tableau( tableau, from_col, to_col ):
    pass  # stub; delete and replace it with your code   

        
def check_for_win( tableau, stock ):
    return False  # stub; delete and replace it with your code   

def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()


def get_option():
    return []   # stub; delete and replace with your code
        
def main():
    pass

if __name__ == '__main__':
     main()
