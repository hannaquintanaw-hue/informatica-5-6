def main():

    print("Target atmospheric layers: ")

    layer = input("Enter atmospheric layer: ")

    if layer == "Exosphere":
          print("Altitude level will be between 700–10,000 km")
          altitude = float(input("Enter exact altitude: "))

    elif layer == "Thermosphere":
          print("Altitude level will be between 85–700 km")
          altitude = float(input("Enter exact altitude: "))

    elif layer == "Mesosphere":
          print("Altitude level will be between 50–85 km")
          altitude = float(input("Enter exact altitude: "))

    elif layer == "Stratosphere":
          print("Altitude level will be between 12–50 km")
          altitude = float(input("Enter exact altitude: "))

    elif layer == "Troposphere":
          print("Altitude level will be between 0–12 km")
          altitude = float(input("Enter exact altitude: "))

    else:
          print("Not found, please enter target atmospheric layer")





if __name__== "__main__":
    main()

