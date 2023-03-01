import unittest
from proj06 import get_books_by_criterion


class GetBooksByCriterionTest(unittest.TestCase):
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
    def test_get_books_by_wrong(self):
        criteria = 2
        value = "lord of the Flies"                  
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []
        
        print(20*'-')
        criteria = 1
        value = "lord"                    
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []

        print(20*'-')
        criteria = 3
        value = "lord"                    
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []

        print(20*'-')
        criteria = 5
        value = "1980"                    
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []

        print(20*'-')
        criteria = 6
        value = 5.07                    
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []

        print(20*'-')
        criteria = 7
        value = 650                   
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Student: ", student)
        assert student == []
        
    def test_get_books_by_title(self):
        criteria = 1
        value = "lord of the Flies"
        expected = ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                     'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                     '1959', 3.67, 208, 310)
                    
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Expected: ", expected)
        print("Student: ", student)
        assert student == expected
        
    def test_get_books_by_category(self):
        criteria = 3
        value = "fiction"
        expected = [('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                     'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                     '1959', 3.67, 208, 310)
                    ]
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Expected: ", expected)
        print("Student: ", student)
        assert student == expected

    def test_get_books_by_year(self):
        criteria = 5
        value = '1982'
        expected = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                     "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                     '1982', 3.97, 479, 172), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                     '1982', 4.11, 489, 43540)
                    ]
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Expected: ", expected)
        print("Student: ", student)
        assert student == expected

    def test_get_books_by_ratings(self):
        criteria = 6
        value = 4.07
        expected = [('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 'Donation.', '1977', 4.27, 560, 3975), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', '1982', 4.11, 489, 43540), 
                    ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 
                     'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of corruption.', 
                     '1996', 4.07, 512, 2045)
                    ]
        student= get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Expected: ", expected)
        print("Student: ", student)
        assert student == expected

    def test_get_books_by_pages(self):
        criteria = 7
        value = 500
        expected = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                     "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                     '1982', 3.97, 479, 172), 
                    ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                     'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
                     '1982', 4.11, 489, 43540), 
                    ('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
                     "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.",
                     '1994', 4.04, 501, 49170), 
                    ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 
                     'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of corruption.', 
                     '1996', 4.07, 512, 2045)
                    ]
        student = get_books_by_criterion(self.master_list, criteria, value)
        print("\n"+20*"-")
        print("master_list: ", self.master_list)
        print("Criteria: ", criteria)
        print("Value: ", value)
        print("Expected: ", expected)
        print("Student: ", student)
        assert student == expected


if __name__ == '__main__':
    unittest.main()

