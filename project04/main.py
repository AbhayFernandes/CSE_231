''' Insert heading comments here.'''


MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''


def numtobase( N, B ):
    '''convert a number N to a different base system B'''
    string = ""
    if N == 0:
        return ""
    while N > 0:
        remainder = N % B
        N = N // B
        string += str(remainder)
    # add leading zeroes to make the string length a multiple of 8
    while len(string) % 8 != 0:
        string += "0"
    return string[::-1]

def basetonum( S, B ):
    '''convert a number S from another base system B to a decimal number'''
    if S == "":
        return 0
    S = int(S)
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

def convert_to_binary(S):
    '''convert a string S to a binary string'''
    binary = ""
    for i in S:
        binary += numtobase(ord(i), 2)
    return binary

def encode_image(image,text,N):
    '''take a string representing the binary representation of a string, text which is to be encoded using LSB and N representing how many bits per pixel'''
    new_image = ""
    text_to_binary = convert_to_binary(text)
    for i in range(0, len(image), N):
        try:
            new_bit = image[i:i+N]
            new_bit = new_bit[:N-1] + text_to_binary[0]
            text_to_binary = text_to_binary[1:]
            new_image += new_bit
        except IndexError:
            new_image += image[i:i+N]
    return new_image


def decode_image(stego, N):
    '''Take an image stego and extract the encoded text using LSB and N representing how many bits per pixel'''
    binary_text = ""
    output_string = ""
    for i in range(N-1, len(stego), N):
        binary_text += stego[i]
    binary_text = binary_text[:len(binary_text) - len(binary_text) % 8]
    for i in range(0, len(binary_text), 8):
        output_string += chr(basetonum(binary_text[i:i+8], 2))
    return output_string

def main():
    print(BANNER)
    print(MENU)
    
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
