# Lab 6 Waleed Aref    
def encode(password):  # you'll want to change this to encode()  -Mary
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode(encoded_password):  # decodes password by subtracting 3 from each digit of encoded password
    # encoded_password = '45678888'
    decoded_password_list = []
    encoded_password_list = list(encoded_password)
    for idx, elem in enumerate(encoded_password_list):
        decoded_password_list.append(str(int(elem) - 3))
    decoded_password_string = ''.join(decoded_password_list)
    # decoded_password_string = '12345555'
    return decoded_password_string


def main():
    encoded_password = None

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")  # you'll want a blank line before and after this print statement  -Mary

    while option != "3":
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":  # decode the encoded password
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
        else:
            print("Invalid option!")

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

    print("Exiting the program...")


if __name__ == '__main__':
    main()
