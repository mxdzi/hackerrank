def catAndMouse(x, y, z):
    return ("Mouse C" if abs(z - y) == abs(z - x)
            else "Cat B" if abs(z - y) < abs(z - x) else "Cat A")
