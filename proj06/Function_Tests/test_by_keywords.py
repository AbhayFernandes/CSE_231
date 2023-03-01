import unittest
from proj06 import get_books_by_keyword


class GetBooksByKeywordsTest(unittest.TestCase):
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
        def test_get_books_by_keyword_1(self):
            expected = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                         "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                         '1982', 3.97, 479, 172), 
                        ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 
                         'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of corruption.', 
                         '1996', 4.07, 512, 2045), 
                        ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                         'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                         '1959', 3.67, 208, 310)
                        ]
            keywords = ['archbishop','Trilogy','Island','corruption']
            student = get_books_by_keyword(self.master_list, keywords)
            print("\nkeywords: ", keywords)
            print("\nExpected: ", expected)
            print("\nStudent: ", student)
            assert student == expected
    
        def test_get_books_by_keyword_2(self):
            expected = []
            keywords = ['electro']
            student = get_books_by_keyword(self.master_list, keywords)
            print("\nkeywords: ", keywords)
            print("\nExpected: ", expected)
            print("\nStudent: ", student)
            assert student == expected
    



if __name__ == '__main__':
    unittest.main()
