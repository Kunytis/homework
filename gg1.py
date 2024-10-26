"""
# 1

namew = input("Your name here!:....")
agew = int(input("Your age here!:...."))
print(f"Hi {namew}! you're {agew}! <3")



# 2
aget = int(input("Put you age here!: ..."))
if aget >18:
    print("YAY you're invited!")

else:
    print("not invited.")



# 3
import random

miku_number = random.randint(1, 10)
tries = 3

print("guess the miku number!(1~10)   3 tries.")

for i in range(tries):
    if guess == miku_number:
        print("Miku is happy! you guessed it!")
        break
    elif guess > miku_number:
        ("miku says try smaller number!")
    else:
        print("miku says try bigger numbers!")
if guess != miku_number:
    print(f"uh oh! you ran out of attempts, the miku number was {miku_number}")


# 4
start = int(input("input start number ..."))
finish = int(input("input ending number ..."))

for number in range(start, finish +1):
    print(number, finish = " ")

# nom
n = int(input("Put a number, (example 32): ..."))

for number in range(n, 0, -1):
    if number % 2 == 0:
        print(number, end= "")
        break

# 5
n = int(input("enter number n: ..."))
factorial = 1

for i in range(1, n + 1):
    factorial *=i

print(f" factorial {n} equals to {factorial}, yay!")
"""
