from operator import itemgetter

file1 = open("data1.txt", "r")
file2 = open("data2.txt", "r")
file1.readline()
file2.readline()

scores = {}

def open_file(file_path):
    for line in file_path:
        line = line.strip()
        line = line.split()
        if line[0] in scores:
            scores[line[0]] += int(line[1])
        else:
            scores[line[0]] = int(line[1])


def output(scores):
    # sort alphabetically first
    scores = sorted(scores.items(), key=itemgetter(0))
    print("Name       Total")
    for key, value in scores:
        print(f"{key:10s} {value:<10d}")

def main():
    open_file(file1)
    open_file(file2)
    output(scores)

if __name__ == "__main__":
    main()