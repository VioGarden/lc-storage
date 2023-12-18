def reverseBits(n):
    bits = 32
    result = 0
    for i in range(bits):
        shift_amount = bits - 1 - (2 * i)
        and_amount = 2 ** (bits - 1 - i)

        if shift_amount >= 0:
            result += (n << shift_amount) & and_amount
        else:
            result += (n >> (-1 * shift_amount)) & and_amount
    return result