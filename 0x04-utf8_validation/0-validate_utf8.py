#!/usr/bin/python3

def validUTF8(data):
    """
    Validates a dataset of integers representing UTF-8 encoding.

    Args:
        data: A list of integers, each representing a single byte of UTF-8 data.

    Returns:
        True if the 'data' represents valid UTF-8 encoding, False otherwise.
    """

    num_bytes = 0  # Counter for bytes in a multi-byte character 

    for byte in data:
        mask = 1 << 7  # Mask to check the most significant bit
        if num_bytes == 0: 
            # First byte of a character:
            while byte & mask:  
                num_bytes += 1 
                mask >>= 1
            if num_bytes == 0:  # 1-byte character
                continue
            if num_bytes == 1 or num_bytes > 4:  # Invalid start byte
                return False  
        else:
            # Continuation byte:
            if not (byte & mask == 128 and byte & ~mask == 64):
                return False
            num_bytes -= 1  # Decrease count for multi-byte character

    return num_bytes == 0  # Valid if all multi-byte characters are complete 

