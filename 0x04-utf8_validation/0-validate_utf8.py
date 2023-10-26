#!/usr/bin/python3

def validUTF8(data):
    count = 0
    for i in data:
        i = format(i, '#010b')[-8:]
        if count == 0:
            for bit in i:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (i[0] == '1' and i[1] == '0'):
                return False
        count = count - 1 if count > 0 else 0
    if count == 0:
        return True
    return False
