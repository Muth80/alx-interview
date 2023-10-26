#!/usr/bin/python3

def validUTF8(data):
    count = 0
    for byte in data:
        byte = byte & 0b11111111
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
