import random
def main():
    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choise(coin)
        guess = input("Headsor tails?: ").strip().lower()

        print("The coin landedon", flip)

        if guess == flip:
            print("Winner")
            break
        else:
            print("Loser")

if __name__ == "__main__":
    main()
    




