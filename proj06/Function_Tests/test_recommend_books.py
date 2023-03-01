import unittest
from proj06 import recommend_books,read_file

class RecommendBooksTest(unittest.TestCase):
        def test_recommend_books_no_sorting(self):
            master_list = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
                           "Volume Two of Stephen Donaldson's acclaimed second trilogy featuing the compelling anti-hero Thomas Covenant.", 
                           '1982', 3.97, 479, 172), 
                          ('9.78001E+12', 'An Autobiography', 'Agatha Christie', ['authors', ' english'], 
                           'Donation.', 
                           '1977', 4.27, 560, 3975), 
                          ('9.78001E+12', 'Master of the Game', 'Sidney Sheldon', ['adventure stories'], 
                           'Kate Blackwell is an enigma and one of the most powerful women in the world. But at her ninetieth birthday celebrations there are ghosts of absent friends and absent enemies.', 
                           '1982', 4.11, 489, 43540), 
                          ('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
                           "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.", 
                           '1994', 4.04, 501, 49170), 
                          ('9.78001E+12', 'Glittering Images', 'Susan Howatch', ['english fiction'], 
                           'It is 1937, and Charles Ashworth, a Canon to the Archbishop of Canterbury, is sent to untangle a web of self-delusion and corruption at the episcopal palace of the charismatic Bishop of Starbridge.', 
                           '1996', 4.07, 512, 2045), 
                          ('9.78081E+12', 'Lord of the Flies', 'William Golding', ['fiction'], 
                           'Story of the return to the wild of a group of British schoolboys marooned on an island.', 
                           '1959', 3.67, 208, 310)
                          ]
            expected = [('9.78001E+12', 'If Tomorrow Comes', 'Sidney Sheldon', ['adventure stories'], 
             "One of Sidney Sheldon's most popular and bestselling titles, repackaged and reissued for a new generation of fans.", 
             '1994', 4.04, 501, 49170)
            ]
            category = "adventure stories"
            rating = 4.00
            page_number = 500
            keywords = ['bestselling']
            print("\n"+20*"-"+"No sorting check")
            student = recommend_books(master_list, keywords, category, rating, page_number,True)
            print("master_list: ", master_list)
            print("\ncategory: ", category)
            print("rating: ", rating)
            print("page_number: ", page_number)
            print("keywords:",keywords)
            print("\nExpected: ", expected)
            print("\nStudent: ", student)
            assert student == expected
    
        def test_recommend_books_2(self):
            fp = open("books_medium.csv",encoding='utf-8')
            master_list = read_file(fp)

            expected = [('9.78006E+12', 'The Good, the Bad, and the Undead', 'Kim Harrison', ['fiction'], 
                         "It's a tough life for witch Rachel Morgan, sexy, independent bounty hunter, prowling the darkest shadows of downtown Cincinnati for criminal creatures of the night. She can handle the leather-clad vamps and even tangle with a cunning demon or two. But a serial killer who feeds on the experts in the most dangerous kind of black magic is definitely pressing the limits. Confronting an ancient, implacable evil is more than just child's play -- and this time, Rachel will be lucky to escape with her very soul.", 
                         '2005', 4.26, 453, 53112), 
                        ('9.78002E+12', 'The Short Stories of Ernest Hemingway', 'Ernest Hemingway', ['fiction'], 
                         "Forty-nine stories reflect much of the intensity of Hemingway's own life and environment", 
                         '1986', 4.26, 499, 106), 
                        ('9.78006E+12', 'A Tree Grows in Brooklyn', 'Betty Smith', ['fiction'], 
                         "The beloved American classic about a young girl's coming-of-age at the turn of the century, Betty Smith's A Tree Grows in Brooklyn is a poignant and moving tale filled with compassion and cruelty, laughter and heartache, crowded with life and people and incident. The story of young, sensitive, and idealistic Francie Nolan and her bittersweet formative years in the slums of Williamsburg has enchanted and inspired millions of readers for more than sixty years. By turns overwhelming, sublime, heartbreaking, and uplifting, the daily experiences of the unforgettable Nolans are raw with honesty and tenderly threaded with family connectedness -- in a work of literary art that brilliantly captures a unique time and place as well as incredibly rich moments of universal experience.", 
                         '2006', 4.26, 496, 326733)
                        ]
            category = "fiction"
            rating = 4.2
            a_z = False
            page_number = 500
            keywords =['happy','life']
            print("\n"+20*"-"+"sorting descending")
            print("Data file: books_medium.csv")
            student = recommend_books(master_list, keywords, category, rating, page_number,a_z)
            fp.close()
            print("category: ", category)
            print("rating: ", rating)
            print("page_number: ", page_number)
            print("keyword:",keywords)
            print("a_z:",False)
            print("\nExpected: ", expected)
            print("\nStudent: ", student)
            assert student == expected


if __name__ == '__main__':
    unittest.main()


