def birthdayCakeCandles(ar):
    last = sorted(ar)[-1]
    return len([i for i, n in enumerate(ar) if n == last])
