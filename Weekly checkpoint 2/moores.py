def main():

    Transistors= 17800000000
    Years=int(input("How many more years into the future?"))
    Transistors*=round(2**(years/2))
    print(f"{Transistors:,}")

 if_name_=="_main_":
    main()

