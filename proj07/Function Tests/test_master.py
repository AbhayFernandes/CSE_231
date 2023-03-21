import unittest
from proj07 import get_average, get_data_in_range, get_max, get_min, get_modes, high_low_averages, read_files


class MasterTest(unittest.TestCase):
    def test_get_average(self):
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]]
        cities = ['lansing_small', 'chicago_small']
        print("data:",data)
        print("cities:",cities)
        col = 2
        print("column #:",col)
        instructor = [('lansing_small', 25.5), ('chicago_small', 35.25)]
        print("Instructor:")
        print(instructor)
        student = get_average(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor
        print("\n"+"-"*20)
        col = 5
        print("column #:",col)
        instructor = [('lansing_small', 1.75), ('chicago_small', 0.2)]
        print("Instructor:")
        print(instructor)
        student = get_average(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor
    
    def test_get_data_in_range(self):
        master_list = [
        [('5/2/1999', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
        ('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
        ('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
        ('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0),
        ('3/6/2002', 31.0, 34.0, 28.0, 0.0, 0.1, None)
        ], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
        ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
        ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
        ('11/20/2003', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
        ]
        ]
        start_date = '1/1/2000'
        end_date = '12/31/2001'
        instructor = [[('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
        ('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
        ('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
        ], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
        ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
        ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None)
        ]
        ]
        print("Instructor:")
        print(instructor)
        student = get_data_in_range(master_list,start_date,end_date)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        start_date = '1/1/1900'
        end_date = '12/31/2025'
        instructor = [
        [('5/2/1999', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
        ('3/1/2000', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
        ('1/1/2000', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
        ('12/31/2001', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0),
        ('3/6/2002', 31.0, 34.0, 28.0, 0.0, 0.1, None)
        ], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
        ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
        ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
        ('11/20/2003', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
        ]
        ]
        print("Instructor:")
        print(instructor)
        student = get_data_in_range(master_list,start_date,end_date)
        print("Student:")
        print(student)
        assert student == instructor
    
    def test_get_max(self):
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]]
        cities = ['lansing_small', 'chicago_small']
        print("data:",data)
        print("cities:",cities)
        col = 2
        print("column #:",col)
        instructor = [('lansing_small', 31.0), ('chicago_small', 43.0)]
        print("Instructor:")
        print(instructor)
        student = get_max(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        col = 5
        print("column #:",col)
        instructor = [('lansing_small', 3.1), ('chicago_small', 0.3)]
        print("Instructor:")
        print(instructor)
        student = get_max(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

    def test_get_min(self):
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]]
        cities = ['lansing_small', 'chicago_small']
        print("data:",data)
        print("cities:",cities)
        col = 2
        print("column #:",col)
        instructor = [('lansing_small', 18.0), ('chicago_small', 29.0)]
        print("Instructor:")
        print(instructor)
        student = get_min(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        col = 5
        print("column #:",col)
        instructor = [('lansing_small', 0.4), ('chicago_small', 0.1)]
        print("Instructor:")
        print(instructor)
        student = get_min(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

    def test_get_modes(self):
        print("Case 1: All have one mode")
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.2, 0.09, 0.9, 5.0),  ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 26.4, 22.0, 0.12, 2.6, 5.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, -26.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 20.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, -26.0, 0.0, 0.3, 0.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 22.0, -26.47, 0.12, 2.6, 5.0),('12/25/2022', 17.0, 18.0, -26.32, 0.01, 0.4, 9.0),('11/25/2022', 17.0, 18.0, -25.97, 0.01, 0.4, 9.0)]]
        cities = ['NY', 'LA']
        col = 3
        print("data:",data)
        print("cities:",cities)
        print("column #:",col)
        instructor = [('NY', [22.0], 4), ('LA', [-26.47], 5)]
        print("Instructor:")
        print(instructor)
        student = get_modes(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        print("Case 2: all have multiple modes")
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 23.2, 0.09, 0.9, 5.0),  ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 26.4, 13.17, 0.12, 2.6, 5.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, -26.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 22.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, -25.0, 0.0, 0.3, 0.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 22.0, -26.47, 0.12, 2.6, 5.0),('12/25/2022', 17.0, 18.0, 22.0, 0.01, 0.4, 9.0),('11/25/2022', 17.0, 18.0, -25.97, 0.01, 0.4, 9.0)]]
        col = 3
        cities = ['CA', 'TX']
        print("data:",data)
        print("cities:",cities)
        print("column #:",col)
        instructor = [('CA', [13.0, 22.0], 2), ('TX', [-26.47, 22.0], 3)]
        print("Instructor:")
        print(instructor)
        student = get_modes(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        print("Case 3: all have no modes")
        data = [[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]]
        cities = ['lansing_small', 'chicago_small']
        col = 5
        print("data:",data)
        print("cities:",cities)
        print("column #:",col)
        instructor = [('lansing_small', [], 1), ('chicago_small', [], 1)]
        print("Instructor:")
        print(instructor)
        student = get_modes(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor

        print("\n"+"-"*20)
        print("Case 4: mixtures of number of modes")
        data = [[('1/1/1948', None, 26.0, 22.5, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 28.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], [('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 23.2, 0.09, 0.9, 5.0),  ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 26.4, 13.17, 0.12, 2.6, 5.0)],
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, -26.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 20.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, -26.0, 0.0, 0.3, 0.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 22.0, -26.47, 0.12, 2.6, 5.0),('12/25/2022', 17.0, 18.0, -26.32, 0.01, 0.4, 9.0),('11/25/2022', 17.0, 18.0, -25.97, 0.01, 0.4, 9.0)]]
        cities = ['FL', 'CA', 'MI']
        col = 3
        print("data:",data)
        print("cities:",cities)
        print("column #:",col)
        instructor = [('FL', [], 1), ('CA', [13.0, 22.0], 2), ('MI', [-26.47], 5)]
        print("Instructor:")
        print(instructor)
        student = get_modes(col,data,cities)
        print("Student:")
        print(student)
        assert student == instructor
    
    def test_high_low_averages(self):
        cities = ['LA','FL', 'CA', 'NY'] 
        categories = ['low temp', 'snow']
        data  =[[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], [('1/1/1948', None, 26.0, 22.5, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 28.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], [('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 23.2, 0.09, 0.9, 5.0),  ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 26.4, 13.17, 0.12, 2.6, 5.0)],
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]
        ]

        print("data:",data)
        print("cities:",cities)
        print("categories:",categories)
        instructor = [[('CA', 18.75), ('NY', 23.5)], [('NY', 0.2), ('LA', 1.75)]]
        print("Instructor:",instructor)
        student =  high_low_averages(data, cities, categories)
        print("Student:",student)
        assert student == instructor

        print("\n"+'-'*20)
        cities = ['LA','FL', 'CA', 'NY'] 
        categories = ['low temp', 'electro', 'snow']
        data  =[[('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], [('1/1/1948', None, 26.0, 22.5, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), ('11/18/2022', 28.0, 31.0, 28.0, 0.12, 2.6, 5.0), ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)], [('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), ('1/2/1948', None, 27.0, 23.2, 0.09, 0.9, 5.0),  ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0), ('12/25/2020', 17.0, 18.0, 22.4, 0.01, 0.4, 9.0),('11/18/2022', 28.0, 26.4, 13.17, 0.12, 2.6, 5.0)],
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)]
        ]

        print("data:",data)
        print("cities:",cities)
        print("categories:",categories)
        instructor = [[('CA', 18.75), ('NY', 23.5)], None, [('NY', 0.2), ('LA', 1.75)]]
        print("Instructor:",instructor)
        student =  high_low_averages(data, cities, categories)
        print("Student:",student)
        assert student == instructor

    def test_read_files(self):
        fp1=open("lansing_small.csv",'r')
        fp2=open("chicago_small.csv",'r')
        cities_fp = [fp1,fp2]
        print("opening lansing_small.csv,chicago_small.csv")
        instructor = [
        [('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
        ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
        ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
        ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
        ], 
        [('11/17/2000', 31.0, 34.0, 28.0, 0.0, 0.1, None), 
        ('11/18/2000', 29.0, 35.0, 23.0, 0.0, None, None), 
        ('11/19/2000', 33.0, 43.0, 23.0, 0.02, None, None), 
        ('11/20/2000', 25.0, 29.0, 20.0, 0.0, 0.3, 0.0)
        ]
        ]
        print("Instructor:")
        print(instructor)
        student = read_files(cities_fp)
        print("\nStudent:")
        print(student)
        assert student == instructor
        print('\n'+'-'*20)
        fp1=open("lansing_small.csv",'r')
        cities_fp = [fp1]
        print("opening lansing_small.csv")
        instructor = [
        [('1/1/1948', None, 26.0, 22.0, 0.84, 3.1, 3.0), 
        ('1/2/1948', None, 27.0, 22.0, 0.09, 0.9, 5.0), 
        ('11/18/2022', 28.0, 31.0, 22.0, 0.12, 2.6, 5.0), 
        ('12/25/2022', 17.0, 18.0, 13.0, 0.01, 0.4, 9.0)
        ]
        ]
        print("Instructor:")
        print(instructor)
        student = read_files(cities_fp)
        print("\nStudent:")
        print(student)
        assert student == instructor

if __name__ == '__main__':
    unittest.main()