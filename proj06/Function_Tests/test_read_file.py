import unittest
from proj06 import read_file


class ReadFileTest(unittest.TestCase):
    def test_read_good_file(self):
        fp = open("data_small.csv",encoding='utf-8')
        instructor = [('9.78001E+12', 'The One Tree', 'Stephen R. Donaldson', ['american fiction'], 
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
        student = read_file(fp)
        print("Data file: data_small.csv")
        #print("Instructor: ", instructor)
        print("Student: ", student)
        print()
        assert student == instructor


if __name__ == '__main__':
    unittest.main()
