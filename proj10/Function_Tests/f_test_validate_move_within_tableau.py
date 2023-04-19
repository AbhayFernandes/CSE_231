
from proj10 import validate_move_within_tableau
import cards
    

c1 = cards.Card(1,3)
c2 = cards.Card(2,2)
c3 = cards.Card(3,3)
c4 = cards.Card(4,4)
c5 = cards.Card(5,2)
c6 = cards.Card(6,2)
c7 = cards.Card(6,1)

tableau = [[c1],[],[c2,c3],[c4,c5,c6]]
instructor_tableau = [[c1],[],[c2,c3],[c4,c5,c6]]
print("Tableau before:",tableau)

to_col = 0
from_col = 1
valid = validate_move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
print("validate_move_within_tableau( tableau, 1, 0):",valid)
assert valid == False
assert tableau == instructor_tableau #tableau should not change

to_col = 1
from_col = 2
valid = validate_move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
print("validate_move_within_tableau( tableau, 2,1):",valid)
assert valid == True
assert tableau == instructor_tableau #tableau should not change

print("-"*20)
tableau = [[],[],[c2,c3],[c4,c5,c6]]
instructor_tableau = [[],[],[c2,c3],[c4,c5,c6]]
print("Tableau before:",tableau)
to_col = 0
from_col = 1
valid = validate_move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
print("validate_move_within_tableau( tableau, 1, 0):",valid)
assert valid == False
assert tableau == instructor_tableau #tableau should not change