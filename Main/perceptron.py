def AND(x1, x2):
    b = -0.7
    tmp = x1 * 0.5 + x2 * 0.5 + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    b = 0.7
    tmp = x1 * (-0.5) + x2 * (-0.5) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    b = -0.3
    tmp = x1 * 0.5 + x2 * 0.5 + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == "__main__":
    print(XOR(0, 0))
    print(XOR(1, 0))
    print(XOR(0, 1))
    print(XOR(1, 1))
    pass