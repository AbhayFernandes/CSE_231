from proj10 import move_to_foundation


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

foundation = []
print("Foundation before:",foundation)
print('-'*20)

from_col = 0
print("move_to_foundation( tableau, foundation, 0)")
move_to_foundation( tableau, foundation, from_col )
print("Instructor tableau after:",instructor_tableau)
print("tableau:",tableau)
print("foundation:",foundation)
assert foundation == []
assert tableau == instructor_tableau
print('-'*20)

from_col = 1
print("move_to_foundation( tableau, foundation, 1)")
move_to_foundation( tableau, foundation, from_col )
print("Instructor tableau after:",instructor_tableau)
print("tableau:",tableau)
print("foundation:",foundation)
assert foundation == []
assert tableau == instructor_tableau
print('-'*20)
print('-'*20)
instructor_tableau = [[c1],[],[c2],[c4,c5,c6]]
instructor_foundation = [c3]
print("Tableau before:",tableau)

foundation = []
print("Foundation before:",foundation)
print('-'*20)

from_col = 2
print("move_to_foundation( tableau, foundation, 2)")
move_to_foundation( tableau, foundation, from_col )
print("Instructor tableau after:",instructor_tableau)
print("Instructor foundation after:",instructor_foundation)
print("tableau:",tableau)
print("foundation:",foundation)

assert foundation == instructor_foundation
assert tableau == instructor_tableau
print('-'*20)

from_col = 3
print("move_to_foundation( tableau, foundation, 3)")
move_to_foundation( tableau, foundation, from_col )
print("Instructor tableau after:",instructor_tableau)
print("Instructor foundation after:",instructor_foundation)
print("tableau:",tableau)
print("foundation:",foundation)

assert foundation == instructor_foundation
assert tableau == instructor_tableau
