def main():
    w = int(input("Width?= "))
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)

    p = (2 * 1) + (2 * w)
    print("Perimeter:", p)
    a = (1 * w)
    print("Area:", a)
    d = ((1**2 + (w**2) )**0.5)
    print("Diagonal:", d)

    if __name__== "__main__":
        main()
