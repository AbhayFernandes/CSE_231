from operator import itemgetter

def build_map( in_file1, in_file2 ):
    
    in_file1.readline()
    in_file2.readline()
    data_map = {}

    #READ EACH LINE FROM FILE 1
    for line in in_file1:
        continent_list = line.strip().split()
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        if continent != "":
            if continent not in data_map:
                data_map[continent] = {}
            if country != "" and country not in data_map[continent]:
                data_map[continent][country] = set()

    #READ EACH LINE FROM FILE 2        
    for line in in_file2:
        # Split the line into two words
        countries_list = line.strip().split()
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        # Ignore empty strings
        if country != "":
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                if country in data_map[continent]:
                    data_map[continent][country].add(city)
    return data_map

def display_map( data_map ):

    # Modify this code to display a sorted nested dictionary
    #sorted list of the continent keys
    continents_list = sorted(data_map.keys())
    # For each continent
    for continent in continents_list:
        print("{}:".format(continent)) #continents in continents_list
        countries_list = sorted(data_map[continent].keys()) #sorted list of the countries keys in the continents
        # For each country
        for country in countries_list:
                print("{:>10s} --> ".format(country),end = '') #countries in countries_list
                cities = sorted(data_map[continent][country])
                # For each city
                for city in cities: 
                    #As long as not last city, add a comma and a space after the cities names
                    if city != cities[-1]:
                        print('{}, '.format(city),end = '') # city in cities                      
                    # if it is the last, don't add a comma and a space.
                    else:
                        print('{}\n'.format(city),end = '')

def open_file():

    try:
        filename = input("Enter file name: ")
        print()
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    # YOUR CODE
    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()
