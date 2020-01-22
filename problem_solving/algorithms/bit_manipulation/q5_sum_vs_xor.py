def sumXor(n):
    return 2 ** (bin(n).count('0') - 1) if n else 1
