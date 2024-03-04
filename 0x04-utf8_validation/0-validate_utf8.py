#!/usr/bin/python3
"""
This script has a method that validates if a dataset represents a valid UTF-8 encoding.
"""

def validUTF8(data):

    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bit and the two most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:

        # Mask to fetch the 8 least significant bits of num
        mask = (1 << 8) - 1
        num = num & mask

        # If this is a character with n bytes in UTF-8, then we need to process n bytes.
        if n_bytes == 0:
            for i in range(5):
                if (num & (mask1 >> i)) == 0:
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0

# Test cases
data = [65]
print(validUTF8(data))  # Output should be True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output should be True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output should be False

