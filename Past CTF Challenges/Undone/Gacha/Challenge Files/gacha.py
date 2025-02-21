import time
import random

FLAG = "blahaj{???}"

print("Initializing...")
for i in range(random.randint(1000000, 10000000)): pass  # Haha you cant guess the seed now!
start_seed = int(time.time()*10)


def main():
    print(welcome)
    turn = 0
    streak = 0
    won = [False] * 5
    while turn < 5000:
        i = None
        while i is None:
            try:
                i = input("Enter your guess: ")
                if i == "exit":
                    turn += 5000
                    break
                i = int(i)
                assert 0 <= i <= 9
            except:
                print("Invalid input!")
        random.seed(start_seed + turn)  # now my seed wont be the same anymore
        number = random.randint(1, 9)
        print(f"My number was: {number}")
        if i == number:
            streak += 1
            print(f"Congratulations! You currently have a streak of {streak}.")
            if streak == 50 and not won[0]:
                print("You won a 1-star chainhaj!")
                won[0] = True
            elif streak == 100 and not won[1]:
                print("You won a 2-star smolhaj!")
                won[1] = True
            elif streak == 200 and not won[2]:
                print("You won a 3-star blahaj!")
                won[2] = True
            elif streak == 300 and not won[3]:
                print("You won a 4-star bighaj!")
                won[3] = True
            elif streak == 500 and not won[4]:
                print("You won the 5-star SSR flag! Here it is:")
                print(FLAG)
                won[4] = True
        else:
            print("Oops! Better luck next time!")
            streak = 0
        turn += 1
        print()
    print("Thanks for playing, and see you next time!")


if __name__ == "__main__":
    main()