#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    # Helper function to check if a byte starts with '10'
    def is_following_byte(byte):
        return byte >> 6 == 0b10

    # Iterate through the data
    for i in range(len(data)):
        byte = data[i]

        # Check the number of bytes in the current character
        if byte >> 7 == 0b0:  # 1-byte character
            continue
        elif byte >> 5 == 0b110:  # 2-byte character
            if i + 1 >= len(data) or not is_following_byte(data[i + 1]):
                return False
        elif byte >> 4 == 0b1110:  # 3-byte character
            if i + 2 >= len(data) or not is_following_byte(data[i + 1]) or not is_following_byte(data[i + 2]):
                return False
        elif byte >> 3 == 0b11110:  # 4-byte character
            if i + 3 >= len(data) or not is_following_byte(data[i + 1]) or not is_following_byte(data[i + 2]) or not is_following_byte(data[i + 3]):
                return False
        else:
            # Invalid start byte for a character
            return False

    return True


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
