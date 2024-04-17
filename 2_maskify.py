""" Maskify Function (maskify):
Input Validation:
Check if the mobile number provided is long enough to maskify.

Masking Process:
Replace all but the last three characters of the mobile number with "#" to mask it.
Output the masked number. """
def maskify(mobile_number):
    if len(mobile_number) < 3:
        print("Mobile number is too short to maskify.")
        return
    
    masked_number = "#" * (len(mobile_number) - 3) + mobile_number[-3:]
    print("Masked number:", masked_number)


mobile_number = input("Enter your mobile number: ")
maskify(mobile_number)
