def decimal_to_octal():
    while True:
        try:
            decimal_num = int(input("Enter a decimal number: "))
            break
        except ValueError:
            print("Error: Invalid decimal number. Please enter a whole number.")
    octal_num = oct(decimal_num).replace("0o", "")
    print(f"The octal representation of {decimal_num} is {octal_num}")

def octal_to_decimal():
    while True:
        oct_num = input("Enter an octal number: ")
        if set(oct_num).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
            break
        else:
            print("Error: Invalid octal number. Please enter a number consisting only of 0-7.")
    decimal_num = int(oct_num, 8)
    print(f"The decimal representation of {oct_num} is {decimal_num}")

def hexidecimal_to_binary():
    while True:
        hex_num = input("Enter a hexadecimal number: ")
        if set(hex_num).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}):
            break
        else:
            print("Error: Invalid hexadecimal number. Please enter a number consisting only of 0-9 and A-F.")
    decimal_num = int(hex_num, 16)
    binary_num = bin(decimal_num).replace("0b", "")
    print(f"The binary representation of {hex_num} is {binary_num}")

def binary_to_hexadecimal():
    while True:
        binary_num = input("Enter a binary number: ")
        if set(binary_num).issubset({'0', '1'}):
            break
        else:
            print("Error: Invalid binary number. Please enter a number consisting only of 0s and 1s.")
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num).replace("0x", "")
    print(f"The hexadecimal representation of {binary_num} is {hex_num}")

def binary_to_decimal():
    while True:
        binary_num = input("Enter a binary number: ")
        if set(binary_num).issubset({'0', '1'}):
            break
        else:
            print("Error: Invalid binary number. Please enter a number consisting only of 0s and 1s.")
    decimal_num = int(binary_num, 2)
    print(f"The decimal representation of {binary_num} is {decimal_num}")

def decimal_to_binary():
    while True:
        try:
            decimal_num = int(input("Enter a decimal number: "))
            if decimal_num < 0:
                print("Error: Decimal number cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid decimal number.")
    binary_num = bin(decimal_num).replace("0b", "")
    print(f"The binary representation of {decimal_num} is {binary_num}")

def hexidecimal_to_decimal():
    while True:
        hex_num = input("Enter a hexadecimal number: ")
        try:
            dec_num = int(hex_num, 16)
            print(f"The decimal equivalent of {hex_num} is {dec_num}")
            break
        except ValueError:
            print("Error: Invalid hexadecimal number. Please enter a valid hexadecimal number.")

def decimal_to_hexidecimal():
    while True:
        try:
            decimal_num = int(input("Enter a decimal number: "))
            if decimal_num < 0:
                print("Error: Decimal number cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid decimal number.")
    hex_num = hex(decimal_num).replace("0x", "")
    print(f"The hexadecimal representation of {decimal_num} is {hex_num}")

def main_menu():
    while True:
        print("\n***Tom's program***")
        print("\n**main Menu**")
        print("1. decimal to octal")
        print("2. octal to decimal")
        print("3. hexidecimal to binary")
        print("4. binary to hexadecimal")
        print("5. Decimal to binary")
        print("6. Binary to decimal")
        print("7. Hexidecimal to decimal")
        print("8. Decimal to hexidecimal")
        print("9. Quit")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
             decimal_to_octal()
        elif choice == "2":
            octal_to_decimal()
        elif choice == "3":
            hexidecimal_to_binary()
        elif choice == "4":
            binary_to_hexadecimal()
        elif choice == "5":
            decimal_to_binary()
        elif choice == "6":
            binary_to_decimal()
        elif choice == "7":
            hexidecimal_to_decimal()
        elif choice == "8":
            decimal_to_hexidecimal()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please select options 1-9.")

if __name__ == "__main__":
    main_menu()
