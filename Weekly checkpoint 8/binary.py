def main():
    print("Binary to Decimal Converter")
    print()
    print(" Welcome, in this program you will be able to convert Binary numbers to Decimal numbers! ")
    binary = int(input("Enter a binary decimal: "))
    binary_to_decimal(binary)



    def binary_to_decimal(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)













if __name__ == "__main__":
    main()
