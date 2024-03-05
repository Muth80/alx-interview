#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits (MSB)
    msb_1 = 1 << 7
    msb_2 = 1 << 6

    for num in data:
        # Mask to extract the 8 least significant bits
        mask = 1 << 7
        if n_bytes == 0:
            # If this is the start of a new character, count the number of 1's at the beginning
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # If there were only 1's or it was greater than 4 bytes, then it's invalid
            if n_bytes == 1 or n_bytes > 4:
                return False

            # If this is a single-byte character, nothing more to check, so continue
            if n_bytes == 0:
                continue
            
            # reduce the remaining checks for this character by one as we've checked the first byte
            n_bytes -= 1

        else:
            # If this is not the first byte, it must start with '10' to be valid.
            if not (num & msb_1 and not (num & msb_2)):
                return False
            # Reduce the remaining checks for this character by one
            n_bytes -= 1

    # If we're in the middle of a character, then it's not a valid sequence
    return n_bytes == 0

# Testing the function with the sample data

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
