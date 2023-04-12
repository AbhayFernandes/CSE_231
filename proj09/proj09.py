import string

def open_file():
    while True:
        try:
            fp = open(input("\nInput a file name: "), "r")
            return fp
        except FileNotFoundError:
            print("\n[Error]: no such file")

def read_file(fp):
    out_set = set()
    for line in fp:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation).lower()
            if word != "" and word.isalpha() and len(word) >= 2:
                out_set.add(word)
    return out_set

def fill_completions(words):
    word_list = list(words)
    letter_dic = {}
    for word in word_list:
        for letter in enumerate(word):
            # if tuple (index, position) not in letter_dic:
            if (letter[0], letter[1]) not in letter_dic:
                letter_dic[(letter[0], letter[1])] = set()
    for position in letter_dic:
        for word in word_list:
            try:
                if word[position[0]] == position[1]:
                    letter_dic[position].add(word)
            except IndexError:
                pass
    return letter_dic


def find_completions(prefix,word_dic):
    out_set = list()
    for position in enumerate(prefix):
        if (position[0], position[1]) in word_dic:
            out_set.append(word_dic[(position[0], position[1])])
        else:
            return set()
    # find intersection of all sets in out_set
    if len(out_set) == 0:
        return set()
    return set.intersection(*out_set)

def set_to_string(in_set):
    out_str = ""
    in_list = list(in_set)
    in_list.sort()
    for word in in_list:
        out_str += word + ", "
    return out_str[:-2]

def main():    
    file = open_file()
    word_dic = fill_completions(read_file(file))   
    while True:
        prefix = input("\nEnter a prefix (# to quit): ")
        if prefix == "#":
            print("\nBye")
            break
        completions = find_completions(prefix, word_dic)
        if len(completions) == 0:
            print("\nThere are no completions.")
        else:
            print(f"\nThe words that completes {prefix} are: {set_to_string(completions)}")

        

if __name__ == '__main__':
    main()
