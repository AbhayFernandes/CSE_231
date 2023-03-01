import os

def get_max_value(num1, num2):
    #compare num1 and num2 and return the larger value
    if num1 < num2:
        return num2
    else:
        return num1


def get_min_value(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
    

def main():
    file = open("data.txt", "r")
    file.readline()
    max_height = 0
    max_weight = 0
    max_bmi = 0
    min_height = 1e6
    min_weight = 1e6
    min_bmi = 1e6
    total_height = 0
    total_weight = 0
    total_bmi = 0
    count = 0
    print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"))
    for line in file:
        name = line[0:12].strip()
        height = float(line[12:24])
        weight = float(line[24:])
        bmi = weight/height**2
        max_height = get_max_value(max_height, height)
        max_weight = get_max_value(max_weight, weight)
        max_bmi = get_max_value(max_bmi, bmi)
        min_height = get_min_value(min_height, height)
        min_weight = get_min_value(min_weight, weight)
        min_bmi = get_min_value(min_bmi, bmi)
        total_height += height
        total_weight += weight
        total_bmi += bmi
        count += 1
        print(f"{name:<12s}{height:<12.2f}{weight:<12.2f}{bmi:<12.2f}")
    print("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", total_height/count, total_weight/count, total_bmi/count))
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", max_height, max_weight, max_bmi))
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", min_height, min_weight, min_bmi))


if __name__ == "__main__":
    main()

