from proj08 import read_file, read_discount, per_discount, in_year, by_genre, by_genre_no_disc, by_dev, by_dev_with_disc, by_dev_year
import unittest

class MasterTest(unittest.TestCase):
    def test_read_file(self):
        fp = open("games_clean_small.csv")
        print("games_clean_small.csv")
        instructor = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}


        print("Instructor:")
        print(instructor)
        student = read_file(fp)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        fp = open("games_medium.csv")
        print("games_medium.csv")
        instructor = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



        print("Instructor:")
        print(instructor)
        student = read_file(fp)
        print("Student:")
        print(student)

        assert student == instructor


    def test_read_discount(self):
        fp = open("discount_small.csv",encoding='UTF-8')
        print("discount_small.csv")
        instructor = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}

        print("Instructor:")
        print(instructor)
        student = read_discount(fp)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        fp = open("discount_medium.csv",encoding='UTF-8')
        print("discount_medium.csv")
        instructor = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                        'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                            "Assassin's Creed�: Director's Cut Edition": 70.14, 
                            'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                                'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                                    'Mirror': 60.0, 'Trine Enchanted Edition': 75.16, 'Trine 3: The Artifacts of Power': 75.13}


        print("Instructor:")
        print(instructor)
        student = read_discount(fp)
        print("Student:")
        print(student)

        assert student == instructor

    def test_per_discount(self):
        print("games_clean_small.csv and discount_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}

        games = ['Bloons TD 6', 'Dota 2','SkiFy']
        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}

        instructor = [5.268, 0.0, 0.252]
        print("Instructor:")
        print(instructor)
        student = per_discount(master_D,games,discount_D)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}


        games=['X3: Reunion','Bloons TD 6','Artifact']
        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                        'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                            "Assassin's Creed�: Director's Cut Edition": 70.14, 
                            'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                                'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                                    'Mirror': 60.0, 'Artifact': 75.16, 'Trine 3: The Artifacts of Power': 75.13}

        instructor = [2.08116, 5.268, 0.891259]
        print("Instructor:")
        print(instructor)
        student = per_discount(master_D,games,discount_D)
        print("Student:")
        print(student)

        assert student == instructor

    def test_in_year(self):
        print("Dictionary from games_clean_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}


        year = 2018
        print("Year:",year)
        instructor = ['Artifact', 'Bloons TD 6', 'DayZ', 'SkiFy']
        print("Instructor:")
        print(instructor)
        student = in_year(master_D,year)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        print("Dictionary from games_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



        year = 2006
        print("Year:",year)
        instructor = ['X2: The Threat', 'X3: Reunion', 'X3: Terran Conflict']
        print("Instructor:")
        print(instructor)
        student = in_year(master_D,year)
        print("Student:")
        print(student)

        assert student == instructor
    

    def test_by_genre(self):
        print("Dictionary from games_clean_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}



        genre = 'Action'
        print("Genre:",genre)
        instructor = ['Counter-Strike: Global Offensive', 'DayZ', 'Dota 2', 'Grand Theft Auto V'] 
        print("Instructor:")
        print(instructor)
        student = by_genre(master_D,genre)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        print("Dictionary from games_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



        genre = 'Strategy'
        print("Genre:",genre)
        instructor = ['X3: Terran Conflict', 'Bloons TD 6', 'X2: The Threat', 'X3: Reunion', 'Dota 2', 'Artifact']
        print("Instructor:")
        print(instructor)
        student = by_genre(master_D,genre)
        print("Student:")
        print(student)

        assert student == instructor

    
    def test_by_genre_no_disc(self):
        print("games_clean_small.csv and discount_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}


        discount_D = instructor = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}
        genre = 'Action'
        print("Genre:",genre)
        instructor = ['Counter-Strike: Global Offensive', 'Dota 2', 'Grand Theft Auto V', 'DayZ']
        print("Instructor:")
        print(instructor)
        student = by_genre_no_disc(master_D,discount_D,genre)
        print("Student:")
        print(student)

        assert student == instructor

        print("\n"+"-"*20)
        print("games_medium.csv and discount_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}

        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                        'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                            "Assassin's Creed�: Director's Cut Edition": 70.14, 
                            'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                                'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                                    'Mirror': 60.0, 'Trine Enchanted Edition': 75.16, 'Trine 3: The Artifacts of Power': 75.13} 
        genre = 'Strategy'
        print("Genre:",genre)
        instructor = ['Dota 2', 'X2: The Threat', 'Artifact', 'Bloons TD 6', 'X3: Terran Conflict']
        print("Instructor:")
        print(instructor)
        student = by_genre_no_disc(master_D,discount_D,genre)
        print("Student:")
        print(student)

        assert student == instructor

    
    def test_by_dev(self):
        print("Dictionary from games_clean_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}



        dev = 'Valve'
        print("Developer:",dev)
        instructor = ['Artifact', 'Dota 2', 'Counter-Strike: Global Offensive']
        print("Instructor:")
        print(instructor)
        student = by_dev(master_D,dev)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        print("Dictionary from games_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



        dev = 'Egosoft'
        print("Developer:",dev)
        instructor = ['X3: Terran Conflict', 'X3: Reunion', 'X2: The Threat']
        print("Instructor:")
        print(instructor)
        student = by_dev(master_D,dev)
        print("Student:")
        print(student)

        assert student == instructor

    
    def test_by_dev_year(self):
        print("games_clean_small.csv and discount_smaa.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}

        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}
        year = 2018
        dev = 'Valve'
        print("Developer:",dev)
        print("Year: ",year)
        instructor = ['Artifact']
        print("Instructor:")
        print(instructor)
        student = by_dev_year(master_D,discount_D,dev,year)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        print("games_medium.csv and discount_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}

        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                        'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                            "Assassin's Creed�: Director's Cut Edition": 70.14, 
                            'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                                'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                                    'Mirror': 60.0, 'Trine Enchanted Edition': 75.16, 'Trine 3: The Artifacts of Power': 75.13}

        dev = 'Egosoft'
        year = 2006
        print("Developer:",dev)
        print("Year: ",year)
        instructor = ['X3: Reunion', 'X2: The Threat', 'X3: Terran Conflict']
        print("Instructor:")
        print(instructor)
        student = by_dev_year(master_D,discount_D,dev,year)
        print("Student:")
        print(student)

        assert student == instructor

    
    def test_by_dev_with_disc(self):
        print("Dictionary from games_clean_small.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}


        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}
        dev = 'Valve'
        print("Developer:",dev)
        instructor = []
        print("Instructor:")
        print(instructor)
        student = by_dev_with_disc(master_D,discount_D,dev)
        print("Student:")
        print(student)

        assert student == instructor
        print("\n"+"-"*20)
        print("Dictionary from games_medium.csv")
        master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
                    'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                        'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                            'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                                'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                                    'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                        'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                            'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                                'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                                    'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



        discount_D = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
                    'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                        'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                            "Assassin's Creed�: Director's Cut Edition": 70.14, 
                            'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                                'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                                    'Mirror': 60.0, 'Trine Enchanted Edition': 75.16, 'Trine 3: The Artifacts of Power': 75.13} 
        dev = 'Egosoft'
        print("Developer:",dev)
        instructor = ['X3: Reunion']
        print("Instructor:")
        print(instructor)
        student = by_dev_with_disc(master_D,discount_D,dev)
        print("Student:")
        print(student)

        assert student == instructor