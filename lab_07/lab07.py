import csv
import os
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Docstring'''
    output = []
    spamreader = csv.reader(fp, delimiter=',')
    for line in spamreader:
        output.append(line)
    output = output[4:]
    output.pop(1)
    return output


def get_totals(L):
    total = 0
    for line in L:
        if line[1][0] == "<":
            line[1] = line[1][1:]
        line[1] = int(line[1].replace(',',''))
        total += line[1]
    total -= 10700000
    return L[0][1],total  # temoprary return value so main runs


def get_largest_states(L):
    min = L[0][2]
    output = []
    for line in L:
        if line[2] > min:
            output.append(line[0])
    return output


def get_industry_counts(L):
    # count how many occurences of an industry there are
    # format: [(industry, count), ...]
    output = [["Construction", 0], ["Manufacturing", 0], ["Agriculture", 0], ["Business services", 0], ["Leisure/hospitality", 0]]
    L.pop(0)
    for line in L:
        for industry in output:
            if line[9] == industry[0]:
                industry[1] += 1
    key = itemgetter(1)
    output.sort(key=key, reverse=True)
    return output


def main():
    dir_name = os.path.dirname(os.path.abspath(__file__)) 
    fp = open(os.path.join(dir_name, "immigration.csv"))
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
