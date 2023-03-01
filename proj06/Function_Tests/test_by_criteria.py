import unittest
from proj06 import get_books_by_criteria


class GetBooksByCriteriaTest(unittest.TestCase):
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
        print(master_list)
        def test_get_books_by_criteria_1(self):
            expected = [('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
             'Kate Blackwell is an enigma and one of the most powerful women in the world.', 
             '1982', 4.11, 489, 43540), 
            ('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
             "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.", 
             '1994', 4.04, 501, 49170)
            ]
            category = "adventure stories"
            rating = 4.00
            page_number = 500
            student = get_books_by_criteria(self.master_list, category, rating, page_number)
            #print("master_list: ", self.master_list)
            print("category: ", category)
            print("rating: ", rating)
            print("page_number: ", page_number)
            print("Expected: ", expected)
            print("Student: ", student)
            assert student == expected
    
        def test_get_books_by_criteria_2(self):
            expected = []
            category = "pyro"
            rating = 5.0
            page_number = 100
            student = get_books_by_criteria(self.master_list, category, rating, page_number)
            #print("master_list: ", self.master_list)
            print("category: ", category)
            print("rating: ", rating)
            print("page_number: ", page_number)
            print("Expected: ", expected)
            print("Student: ", student)
            assert student == expected
    
        def test_get_books_by_criteria_3(self):
            expected = []
            category = "electro"
            rating = 3.2
            page_number = 300
            student = get_books_by_criteria(self.master_list, category, rating, page_number)
            #print("master_list: ", self.master_list)
            print("category: ", category)
            print("rating: ", rating)
            print("page_number: ", page_number)
            print("Expected: ", expected)
            print("Student: ", student)
            assert student == expected


if __name__ == '__main__':
    unittest.main()
