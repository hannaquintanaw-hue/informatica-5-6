import random

def main():
    print("Hello! What is your name?")
    name = input("")
    print(f"Well, {name}, I am thinking of a number 1 and 100.")

    number = random.randint(1, 100)
    guess = 0 #initialize

    while guess != number:
        guess = int(input("Take a guess:"))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")
    print(f"Good job, {name}! You guessed my number!")




if __name__ == "__main__":
    main()
