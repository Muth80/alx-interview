#!/usr/bin/python3

def validUTF8(data):
    count = 0
    for byte in data:
        byte = byte & 0b11111111  # Mask the integer with 0xFF to consider only the 8 least significant bits
        byte = format(byte, '#010b')[-8:]
        if count == 0:
            for bit in byte:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        count = count - 1 if count > 0 else 0
    if count == 0:
        return True
    return False

# Test cases
data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False

