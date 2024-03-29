def hex_to_binary(hex_num):
    # Define a dictionary to map hexadecimal digits to their binary representation
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    binary_num = ''
    # Convert each hexadecimal digit to binary using the dictionary
    for digit in hex_num:
        if digit.upper() in hex_to_bin:
            binary_num += hex_to_bin[digit.upper()]
        else:
            return "Invalid hexadecimal digit: {}".format(digit)
    
    return binary_num

def main():
    hex_num = input("Enter a hexadecimal number: ")
    binary_num = hex_to_binary(hex_num)
    print("Binary representation:", binary_num)

if __name__ == "__main__":
    main()
print("Hello")
print("Everyone")
print("Welcome")
print("back")
