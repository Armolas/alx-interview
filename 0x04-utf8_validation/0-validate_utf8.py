#!/usr/bin/python3
'''utf-8 validation interview task'''


def validUTF8(data):
    '''
    Number of bytes in the current UTF-8 character
    '''
    n_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer in the data
    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of leading 1's
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # 1-byte characters (0xxxxxxx) or invalid if n_bytes is 1 or > 4
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the next bytes start with 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes remaining in the current character
        n_bytes -= 1

    # If n_bytes is not zero, then we have an incomplete character at the end
    return n_bytes == 0
