import cards # ignore
from typing import Tuple, List

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

def init_game() -> Tuple[cards.Deck, List[List[cards.Card]], List[cards.Card]]:
    stock = cards.Deck()
    stock.shuffle()
    tableau = [[], [], [], []]
    foundation = []
    # deal 1 card to each tableau column
    for col in tableau:
        col.append(stock.deal())
    return (stock, tableau, foundation) 
    
def deal_to_tableau( tableau: List[List[cards.Card]], stock: cards.Deck):
    for col in tableau:
        new_card = stock.deal()
        if new_card is not None:
            col.append(new_card)
        else:
            pass

           
def validate_move_to_foundation( tableau: List[List[cards.Card]], from_col: int ) -> bool:
    '''
    this function to determines if a requested move to the foundation is valid.
    '''
    if not tableau[from_col]:
        print("\nError, empty column:".format(from_col + 1))
        return False
    card = tableau[from_col][-1]
    if card.value() == 1:
        print("\nError, cannot move {}.".format(card))
        return False
    for col in tableau:
        if col:
            if card == col[-1]:
                continue
            if card.suit() == col[-1].suit() and col[-1].rank() == 1:
                return True
            if col[-1].rank() > card.rank() and col[-1].suit() == card.suit():
                return True
    print("\nError, cannot move {}.".format(card))
    return False

    
def move_to_foundation( tableau: List[List[cards.Card]], foundation: List[cards.Card], from_col: int ):
    if validate_move_to_foundation(tableau, from_col):
        foundation.append(tableau[from_col].pop())


def validate_move_within_tableau( tableau: List[List[cards.Card]], from_col: int, to_col: int) -> bool:
    if tableau[to_col] != []:
        print("\nError, target column is not empty: {}".format(to_col + 1))
        return False
    if not tableau[from_col]:
        print("\nError, no card in column: {}".format(from_col + 1))
        return False
    if tableau[to_col] == []:
        return True
    return False



def move_within_tableau( tableau: List[List[cards.Card]], from_col: int, to_col: int ):
    if validate_move_within_tableau(tableau, from_col, to_col):
        tableau[to_col].append(tableau[from_col].pop())

        
def check_for_win( tableau: List[List[cards.Card]], stock: cards.Deck ) -> bool:
    cards = []
    if stock.is_empty():
        for col in tableau:
            # get a list of all cards in tableau:
            for card in col:
                cards.append(card)
        # check if all cards are aces:
        for card in cards:
            if card.value() != 1:
                return False
        return True
    return False  # stub; delete and replace it with your code   

def display( stock: cards.Deck, tableau: List[List[cards.Card]], foundation: List[cards.Card] ):
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


def get_option() -> List:
    '''Get a valid option from the user.'''
    choice = input("\nInput an option (DFTRHQ): ").strip()
    og = choice
    choice = choice.upper()
    if choice == 'D':
        return ['D']
    elif choice == 'R':
        return ['R']
    elif choice == 'H':
        return ['H']
    elif choice == 'Q':
        return ['Q']
    elif choice[0] == 'F':
        try:
            col = int(choice[1:].strip()) - 1
            if col < 0 or col > 3:
                print(f"\nError in option: {og}")
                return []
            return ['F', col]
        except:
            print(f"\nError in option: {og}")
            return []
    elif choice[0] == 'T':
        try:
            cols = choice[1:].strip().split()
            if len(cols) != 2:
                print(f"\nError in option: {og}")
                return []
            col1 = int(cols[0]) - 1
            col2 = int(cols[1]) - 1
            if col1 < 0 or col1 > 3 or col2 < 0 or col2 > 3:
                print(f"\nError in option: {og}")
                return []
            return ['T', col1, col2]
        except:
            print(f"\nError in option: {og}")
            return []
    else:
        print(f"\nError in option: {og}")
        return []
        
def main():
    print(RULES)
    print(MENU)
    stock, tableau, foundation = init_game()
    skip = False
    while True:
        if check_for_win(tableau, stock):
            print("\nYou won!")
            break
        if not skip:
            display(stock, tableau, foundation)
        skip = False
        option = get_option()
        if option == []:
            skip = True
            continue
        if option[0] == 'Q':
            print("\nYou have chosen to quit.")
            break
        elif option[0] == 'H':
            print(MENU)
        elif option[0] == 'R':
            print("\n=========== Restarting: new game ============")
            print(RULES)
            print(MENU)
            stock, tableau, foundation = init_game()
        elif option[0] == 'D':
            deal_to_tableau(tableau, stock)
        elif option[0] == 'F':
            move_to_foundation(tableau, foundation, option[1])
        elif option[0] == 'T':
            move_within_tableau(tableau, option[1], option[2])



if __name__ == '__main__':
     main()
