''' Insert heading comments here.'''


MENU = '''\nPlease choose one of the options below:
            A. Convert a decimal number to another base system         
            B. Convert decimal number from another base.
            C. Convert from one representation system to another.
            E. Encode an image with a text.
            D. Decode an image.
            M. Display the menu of options.
            X. Exit from the program.'''
    
def numtobase( N, B ):
    '''convert a number N to a different base system B'''
    string = ""
    while N > 0:
        remainder = N % B
        N = N // B
        string += str(remainder)
    return int(string)

def basetonum( S, B ):
    '''convert a number S from another base system B to a decimal number'''
    num = 0
    for i in range(1, len(str(S))+1):
        digit = S % 10
        num += digit * (B ** (i-1))
        S = S // 10
    return num


def basetobase(B1,B2,s_in_B1):
    '''convert a number s_in_B1 from base B1 to base B2'''
    N = basetonum(s_in_B1, B1)
    return numtobase(N, B2)

def encode_image(image,text,N):
    '''Insert docstring here.'''



def decode_image(sego,N):
    '''Insert docstring here.'''

def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    
    B = int(input("Input Base"))
    N = int(input("Input Number"))
    print(basetonum(N, B))

    pass  # insert your code here

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
