#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the first and second most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # If this is a starting byte
        if n_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            
            # 1 byte characters
            if n_bytes == 0:
                continue
            
            # Invalid scenarios according to the UTF-8 encoding
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For non-starting bytes, check if they start with 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False
        
        n_bytes -= 1
    
    # We should have processed all bytes in the UTF-8 character
    return n_bytes == 0

# Main file for testing
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    # 256 is not a valid byte, it's outside the range of 0-255
    data = [229, 65, 127, 256]
    print(validUTF8(data))
