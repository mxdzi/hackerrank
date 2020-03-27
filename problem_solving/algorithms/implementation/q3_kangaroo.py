def kangaroo(x1, v1, x2, v2):
    return "YES" if (v1 - v2) > 0 and ((x2 - x1) / (v1 - v2)).is_integer() else "NO"
