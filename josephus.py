# def josephus(ls, skip):
#     skip -= 1 # pop automatically skips the dead guy
#     idx = skip
#     while len(ls) > 1:
#         ls.pop(idx) # kill prisoner at idx
#         idx = (idx + skip) % len(ls)
#     return str(ls[0])


def josephus(n):
    # Convert n to binary (`bin()` returns a string that
    # starts with '0b' to denote that it's in binary. So, I'll skip those).
    bn = bin(n)[2:]

    # Convert the binary number to base 10 after moving MSB to LSB.
    return int(bn[1:] + bn[0], 2)
