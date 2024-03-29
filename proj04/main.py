###########################################################
#  Computer Project #3
#
#  Algorithm
#    get the user's choice
#    if the user wants to convert a decimal number to another base system
#       get the number and base from the user, 
#       call the function to convert the number to the base system
#       output the result
#    if the user wants to convert a decimal number from another base system
#       get the number and base from the user
#       call the function to convert the number from the base system to decimal
#       output the result
#    if the user wants to convert from one representation system to another
#       get the number and base from the user
#       call the function to convert the number from the base system to decimal
#       call the function to convert the number to the base system
#    if the user wants to encode an image with a text
#       get the image, text, and N from the user
#       call the function to encode the image with the text
#       output the result
#    if the user wants to decode an image
#       get the image and N from the user
#       call the function to decode the image
#       output the result
#    if the user wants to display the menu of options
#       display the menu
#    if the user wants to exit the program
#       exit the program
###########################################################

MENU = """\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program."""
BANNER = """
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    """


def numtobase(N, B):
    """convert a number N to a different base system B"""
    string = ""
    # if N is 0, return an empty string
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


def basetonum(S, B):
    """convert a number S from another base system B to a decimal number"""
    if S == "":
        return 0
    S = int(S)
    num = 0
    # loop through each digit in S
    for i in range(1, len(str(S)) + 1):
        digit = S % 10
        # add the digit multiplied by the base raised to the power of the
        # digit's position to the total
        num += digit * (B ** (i - 1))
        S = S // 10
    return num


def basetobase(B1, B2, s_in_B1):
    """convert a number s_in_B1 from base B1 to base B2"""
    N = basetonum(s_in_B1, B1)
    return numtobase(N, B2)


def convert_to_binary(S):
    """convert a string S to a binary string"""
    binary = ""
    for i in S:
        binary += numtobase(ord(i), 2)
    return binary


def encode_image(image, text, N):
    """take a string representing the binary representation of a string, 
    text which is to be encoded using LSB and N representing how 
    many bits per pixel"""
    new_image = ""
    text_to_binary = convert_to_binary(text)
    for i in range(0, len(image), N):
        try:
            # replace the last bit of the pixel with the first bit of the text
            new_bit = image[i : i + N]
            new_bit = new_bit[: N - 1] + text_to_binary[0]
            text_to_binary = text_to_binary[1:]
            # add the new pixel to the new image
            new_image += new_bit
        # if there is no more text to encode, add the rest of the image
        except IndexError:
            new_image += image[i : i + N]
    return new_image


def decode_image(stego, N):
    """Take an image stego and extract the encoded text using 
    LSB and N representing how many bits per pixel"""
    binary_text = ""
    output_string = ""
    # loop through every Nth pixel and add the last bit to the binary text
    for i in range(N - 1, len(stego), N):
        binary_text += stego[i]
    # remove any extra bits at the end
    binary_text = binary_text[: len(binary_text) - len(binary_text) % 8]
    # convert the binary text to a string
    for i in range(0, len(binary_text), 8):
        output_string += chr(basetonum(binary_text[i : i + 8], 2))
    return output_string


def input_positive_int(prompt):
    """Prompt the user for a positive integer and return it.
    Using error checking."""
    while True:
        num = input(prompt)
        try:
            num = int(num)
        except ValueError:
            print(
                "\n\tError: {} was not a valid non-negative integer.".format(
                    num
                )
            )
            continue
        if num < 0:
            print(
                "\n\tError: {} was not a valid non-negative integer.".format(
                    num
                )
            )
            continue
        return num


def input_valid_base(prompt):
    """Prompt the user for a valid base and return it.
    Using error checking."""
    while True:
        base = input(prompt)
        try:
            base = int(base)
        except ValueError:
            print(
                "\n\tError: {} was not a valid non-negative integer.".format(
                    base
                )
            )
            continue
        if base < 0:
            print(
                "\n\tError: {} was not a valid non-negative integer.".format(
                    base
                )
            )
            continue
        if base < 2 or base > 10:
            print(
                f"\n\tError: {base} was not a valid",
                "integer between 2 and 10 inclusive."
            )
            continue
        return base


def main():
    print(BANNER)
    print(MENU)
    # loop until the user enters X
    while True:
        option = input("\n\tEnter option: ").upper()
        if option == "M":
            print(MENU)
        elif option == "A":
            # get the number and base from the user, ouput the result
            num = input_positive_int("\n\tEnter N: ")
            base = input_valid_base("\n\tEnter Base: ")
            print(f"\n\t {num} in base {base}: {numtobase(num, base)}")
        elif option == "B":
            # get the string and base from the user, ouput the result
            string = input("\n\tEnter string number S: ")
            base = input_valid_base("\n\tEnter Base: ")
            print(f"\n\t {string} in base {base}: {basetonum(string, base)}")
        elif option == "C":
            # get the number, base and new base from the user, ouput the result
            base_1 = input_valid_base("\n\tEnter base B1: ")
            base_2 = input_valid_base("\n\tEnter base B2: ")
            string = input("\n\tEnter string number: ")
            print(
                f"\n\t {string} in base {base_1} is",
                f"{basetobase(base_1, base_2, string)} in base {base_2}..."
            )
        elif option == "E":
            # get the image, number of bits per pixel and text from the user
            img_string = input("\n\tEnter a binary string of an image: ")
            bits = input_positive_int(
                "\n\tEnter number of bits used for pixels: "
            )
            hidden_text = input("\n\tEnter a text to hide in the image: ")
            # check if the text can be encoded in the image
            if len(hidden_text) * 8 > len(img_string) // bits:
                print(
                    "\n\tImage not big enough to",
                    "hold all the text to steganography"
                )
            else:
                print(f"\n\t Original image: {img_string}")
                print(f"\n\t Encoded image: {encode_image(img_string, hidden_text, bits)}")
        elif option == "D":
            # get the image and number of bits per pixel from the user
            stego = input("\n\tEnter an encoded string of an image: ")
            bits = input_positive_int(
                "\n\tEnter number of bits used for pixels: "
            )
            # decode the image and output the result
            print(f"\n\t Original text: {decode_image(stego, bits)}")
        elif option == "X":
            break
        else:
            print(f"\nError:  unrecognized option [{option}]")
            print(MENU)
    print("\nMay the force be with you.")


# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines
if __name__ == "__main__":
    main()
