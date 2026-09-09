import random

def main():
     print("Welcome to my learning app")

     attempts = 0

     while attempts < 3:

          n1 = random.randint(1, 99)
          n2 = random.randint(1, 99)
          print(f"The problem: {n1}+{n2}")
          user = int(input("Write your answer: "))
          if user == n1+n2:
               print("Congratulations!")
               attempts += 1
               print("Streak:")
               print("⭐" * attempts)

          else:
               print("Wrong")


if __name__ == "__main__":
    main()



