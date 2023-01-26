VOWELS = 'aeiou'

done = False
while not done:
    word = input("Enter a word ('quit' to quit): \n").lower()
    if word == 'quit':
        break
    if word[0] in VOWELS:
        print(word + "way")
    elif not any(letter in VOWELS for letter in word):
        print(word + "ay")
    else:
        for i in enumerate(word):
            print(i) 