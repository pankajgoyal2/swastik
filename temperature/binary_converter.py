value = int(input("Enter a number for conversion from 1 to 1023: "))

def conversion(value):
    if value >= 512:
        binary_string += '1'
        value %= 512
    else:
        binary_string += '0'

        if value >= 512:
            binary_string += '1'
            value %= 512
        else:
            binary_string += '0'
            if value >= 256:
                binary_string += '1'
                value %= 256
            else:
                binary_string += '0'
                
