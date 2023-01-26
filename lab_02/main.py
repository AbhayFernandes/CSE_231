# Good stuff goes here
n = 1
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0
while n != 0:
    n_str = input("\nInput an integer (0 terminates): ")
    n = int(n_str)
    if n <= 0:
        continue
    else:
        positive_int_count += 1
        if (n % 2) == 0:
            even_count += 1
            even_sum += n
        elif (n % 2) != 0:
            odd_count += 1
            odd_sum += n

#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
