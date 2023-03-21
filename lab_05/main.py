def list_to_tuple(a_list):
    out = []
    for i in a_list:
        try:
            out.append(int(i))
        except ValueError:
            print("Error. Please enter only integers.")
            return
    print(tuple(out))

def main():
    a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
    list_to_tuple(a_list)
    
main()