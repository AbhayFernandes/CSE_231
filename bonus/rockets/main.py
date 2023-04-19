from myclass import Rocket

def main():
    rocket0 = Rocket(0, 1, 0)
    rocket1 = Rocket(10, 10, 1)
    rocket2 = Rocket(-10, 0, 2)
    # put all rockets into a list:
    rockets = [rocket0, rocket1, rocket2]
    print("\nShow where each rocket is:")
    for i in rockets:
        print(i)
    # sort the list explicitly:
    for i in rockets:
        for j in rockets:
            if i > j:
                rockets[rockets.index(i)] = j
                rockets[rockets.index(j)] = i
    print("\nRank the rockets:")
    for i in rockets:
        print(i)

if __name__ == "__main__":
    main()
