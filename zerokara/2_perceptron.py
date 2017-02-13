import sys

def calc(x1, x2, w, b):
    return 1 if 0 < x1 * w + x2 * w + b else 0

def AND(x1, x2):
    return calc(x1, x2, 0.5, -0.9)

def OR(x1, x2):
    return calc(x1, x2, 0.5, -0.4)

def NAND(x1, x2):
    return calc(x1, x2, -0.5, 1)

def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))

def check(expect, x1, x2, f):
    fact = f(x1, x2)
    if expect == fact:
        sys.stdout.write(".")
    else:
        sys.stdout.write("expect {} but fact {} x1={} x2={}\n".format(
            expect, fact, x1, x2))

def main():
    check(1, 1, 1, AND)
    check(0, 0, 1, AND)
    check(0, 1, 0, AND)
    check(0, 0, 0, AND)

    check(1, 1, 1, OR)
    check(1, 0, 1, OR)
    check(1, 1, 0, OR)
    check(0, 0, 0, OR)

    check(0, 1, 1, NAND)
    check(1, 0, 1, NAND)
    check(1, 1, 0, NAND)
    check(1, 0, 0, NAND)

    check(0, 1, 1, XOR)
    check(1, 0, 1, XOR)
    check(1, 1, 0, XOR)
    check(0, 0, 0, XOR)

if __name__ == "__main__":
    main()
    sys.stdout.write("\n")
