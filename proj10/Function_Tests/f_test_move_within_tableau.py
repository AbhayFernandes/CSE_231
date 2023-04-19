
from proj10 import move_within_tableau
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
print("move_within_tableau( tableau, 1, 0)")
move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
assert tableau == instructor_tableau

to_col = 1
from_col = 2
instructor_tableau = [[c1],[c3],[c2],[c4,c5,c6]]
print("move_within_tableau( tableau, 2, 1):")
move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)
assert tableau == instructor_tableau

print("-"*20)
print("-"*20)
tableau = [[],[],[c2,c3],[c4,c5,c6]]
instructor_tableau = [[],[],[c2,c3],[c4,c5,c6]]
print("Tableau before:",tableau)
to_col = 0
from_col = 1
print("move_within_tableau( tableau, 1, 0):")
move_within_tableau( tableau, from_col, to_col )
print("Instructor Tableau after:",instructor_tableau)
print("Student Tableau after:",tableau)

assert tableau == instructor_tableau #tableau should not change
