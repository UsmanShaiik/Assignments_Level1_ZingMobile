""" Hexadecimal to Decimal Conversion Function (hexadecimal_to_decimal):
Input Validation:
Check if the input provided is a valid hexadecimal number.

Conversion Process:
Convert the hexadecimal number to its decimal representation.
Use a for loop to iterate over each digit of the hexadecimal number and calculate its decimal equivalent.
Output the decimal representation. """
def hexadecimal_to_decimal(hexadecimal):
    hexadecimal = hexadecimal.upper()
    hex_chars = "0123456789ABCDEF"
    decimal_num = 0
    
    for digit in hexadecimal:
        if digit not in hex_chars:
            print("Invalid input: Please enter a valid hexadecimal number.")
            return
        
        decimal_num = decimal_num * 16 + hex_chars.index(digit)
    
    print("Decimal:", decimal_num)

# Test the function
hexadecimal_input = input("Enter a hexadecimal number: ")
hexadecimal_to_decimal(hexadecimal_input)
