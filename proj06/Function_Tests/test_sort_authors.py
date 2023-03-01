import unittest
from proj06 import sort_authors
import copy


class SortAuthorsTest(unittest.TestCase):
    def test_sort_authors_with_ties(self):
        master_list = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                       "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                       '1982', 3.97, 479, 172), 
                      ('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                       'Donation.', 
                       '1977', 4.27, 560, 3975), 
                      ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                       'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                       '1982', 4.11, 489, 43540), 
                      ('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
                       "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.", 
                       '1994', 4.04, 501, 49170), 
                      ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 
                       'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of corruption.', 
                       '1996', 4.07, 512, 2045), 
                      ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                       'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                       '1959', 3.67, 208, 310)
                      ]
        original = copy.deepcopy(master_list)
        expected = [('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 'Donation.', 
                     '1977', 4.27, 560, 3975), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                     '1982', 4.11, 489, 43540), 
                    ('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
                     "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.", 
                     '1994', 4.04, 501, 49170), 
                    ('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                     "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                     '1982', 3.97, 479, 172), 
                    ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of corruption.', 
                     '1996', 4.07, 512, 2045), 
                    ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                     'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                     '1959', 3.67, 208, 310)
                    ]
        print("\n"+20*"-"+"with ties default")
        student = sort_authors(master_list)
        print("master_list: ", master_list)
        print("\nExpected: ", expected)
        print("\nStudent: ", student)
        print()
        assert student == expected
        assert master_list == original  #check that the original master_list did not change        

    def test_sort_authors_default(self):
        master_list = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                       "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                       '1982', 3.97, 479, 172), 
                      ('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                       'Donation.', 
                       '1977', 4.27, 560, 3975), 
                      ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                       'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                       '1982', 4.11, 489, 43540), 
                      ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                       'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                       '1959', 3.67, 208, 310)
                      ]
        original = copy.deepcopy(master_list)
        expected = [('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                     'Donation.', '1977', 4.27, 560, 3975), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                     '1982', 4.11, 489, 43540), 
                    ('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                     "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                     '1982', 3.97, 479, 172), 
                    ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                     'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                     '1959', 3.67, 208, 310)
                    ]
        print("\n"+20*"-"+"Default ascending")
        student = sort_authors(master_list)
        
        print("master_list: ", master_list)
        print("\nExpected: ", expected)
        print("\nStudent: ", student)
        print()
        assert student == expected
        assert master_list == original  #check that the original master_list did not change
        
    def test_sort_authors_descending(self):
        master_list = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                       "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                       '1982', 3.97, 479, 172), 
                      ('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                       'Donation.', 
                       '1977', 4.27, 560, 3975), 
                      ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                       'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                       '1982', 4.11, 489, 43540), 
                      ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                       'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                       '1959', 3.67, 208, 310)
                      ]
        original = copy.deepcopy(master_list)
        expected = [('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                     'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                     '1959', 3.67, 208, 310), 
                    ('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                     "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                     '1982', 3.97, 479, 172), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                     '1982', 4.11, 489, 43540), 
                    ('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                     'Donation.', '1977', 4.27, 560, 3975)
                    ]
        print("\n"+20*"-"+"Descending")
        student = sort_authors(master_list,False)
        
        print("master_list: ", master_list)
        print("\nExpected: ", expected)
        print("\nStudent: ", student)
        print()
        assert student == expected
        assert master_list == original  #check that the original master_list did not change    



if __name__ == '__main__':
    unittest.main()


