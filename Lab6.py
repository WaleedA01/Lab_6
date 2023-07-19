# Lab 6 Waleed Aref    
def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

#decode function here

def main():
    encoded_password = None

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    while option != "3":
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            pass
            # implement decode function here
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
