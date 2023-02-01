def leap_year(year):
    return (int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0))

def rotate(string, number):
    return string[len(string) - number:] + string[:len(string) - number]

def digit_count(number):
    number = int(number)
    zero_count, odd_count, even_count = 0,0,0
    for i in range(1, len(str(number))+1):
        digit = number % 10
        if digit == 0:
            zero_count += 1
        elif digit % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
        number = number // 10
    return even_count, odd_count, zero_count

def float_check(string):
    decimal = 0
    for idx, char in enumerate(string):
        if char == ".":
            string = string[:idx] + string[idx+1:]
            decimal += 1
    return ((decimal == 1 or decimal == 0) and string.isdigit())


def main():
    while True:
        string = input("Enter a string: ")
        number = int(input("Enter a number: "))
        print(rotate(string, number))

if __name__ == "__main__":
    main()