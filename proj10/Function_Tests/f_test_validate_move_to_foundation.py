from proj10 import validate_move_to_foundation
import cards

c1 = cards.Card(1,3)
c2 = cards.Card(2,2)
c3 = cards.Card(3,3)
c4 = cards.Card(4,4)
c5 = cards.Card(5,2)
c6 = cards.Card(6,2)
c7 = cards.Card(1,2)

tableau = [[c1],[],[c2,c3],[c4,c5,c6]]
print("Tableau before:",tableau)

tableau_inst = [[c1],[],[c2,c3],[c4,c5,c6]]


print('-'*20)
from_col = 0
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation(tableau,0):",valid)
print("Instructor Tableau after:",tableau_inst)
print("Student Tableau after:",tableau)
assert valid == False
assert tableau == tableau_inst #tableau should not change

print('-'*20)
from_col = 1
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation(tableau,1):",valid)
print("Instructor Tableau after:",tableau_inst)
print("Student Tableau after:",tableau)
assert valid == False
assert tableau == tableau_inst #tableau should not change

print('-'*20)
from_col = 2
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation(tableau,2):",valid)
print("Instructor Tableau after:",tableau_inst)
print("Student Tableau after:",tableau)
assert valid == True
assert tableau == tableau_inst #tableau should not change

print('-'*20)
from_col = 3
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation(tableau,3):",valid)
print("Instructor Tableau after:",tableau_inst)
print("Student Tableau after:",tableau)
assert valid == False
assert tableau == tableau_inst #tableau should not change

print('-'*20)
print('-'*20)
tableau = [[c1],[],[c2],[c4,c5,c6]]
print("Tableau before:",tableau)
print('-'*20)

from_col = 3
instructor_tableau = [[c1],[],[c2],[c4,c5,c6]]
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation( tableau,3):",valid)
print("Instructor tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
assert valid == False
assert tableau == instructor_tableau #tableau should not change

print('-'*20)
print('-'*20)
tableau = [[c1],[c7],[c2],[c4,c5,c6]]
print("Tableau before:",tableau)
print('-'*20)

from_col = 3
instructor_tableau = [[c1],[c7],[c2],[c4,c5,c6]]
valid = validate_move_to_foundation( tableau, from_col )
print("validate_move_to_foundation( tableau,3):",valid)
print("Instructor tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
assert valid == True
assert tableau == instructor_tableau #tableau should not change