def validUTF8(data):
    # Function to check if an integer represents a valid UTF-8 character
    def is_valid_utf8_char(byte):
        # Check if the integer starts with "10" to indicate a continuation byte
        return (byte & 0b11000000) == 0b10000000

    # Initialize a variable to keep track of the expected number of continuation bytes
    expected_cont_bytes = 0

    for num in data:
        # Check the first byte of the character
        if expected_cont_bytes == 0:
            if (num & 0b10000000) == 0:
                expected_cont_bytes = 0
            elif (num & 0b11100000) == 0b11000000:
                expected_cont_bytes = 1
            elif (num & 0b11110000) == 0b11100000:
                expected_cont_bytes = 2
            elif (num & 0b11111000) == 0b11110000:
                expected_cont_bytes = 3
            else:
                return False
        else:
            # Check continuation bytes
            if not is_valid_utf8_char(num):
                return False
            expected_cont_bytes -= 1

    # Check if all characters have the expected number of continuation bytes
    return expected_cont_bytes == 0

# Test cases
data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False

