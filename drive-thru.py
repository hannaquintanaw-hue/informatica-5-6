def main():
    welcome()
    user_order = input("What would you like to order?: ")
    get_item(user_order)

    def welcome()
        menu = ["Fries", "Sodas", "Hamburgers"]
        print("Welcome to To Chimichangas y mas")
        print("Here's the menu")
        for i in range(len(menu)):
            print(f"{i+1}. {menu[i]}")

    def get_item(order):
        order = order.strip().lower()
        if order == "Fries" or order == "1":
            print("Enjoy! 🍟")
        elif order == "Sodas" or order == "2":
            print("Enjoy! 🥤")
        elif order == "Hamburgers" or order == "3":
            print("Enjoy! 🍔")




if __name__ == "__main__":
    main()
