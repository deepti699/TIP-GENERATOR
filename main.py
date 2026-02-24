import random

a = input("Enter your name")

b = input("Enter your name")

c = input("Enter your name")

d = input("Enter your name")

random_tt = random.randint(0,4)

if random_tt == 0:

  print("{a} should pay the bill")

elif random_tt == 1:

  print("{b} should pay the bill")

elif random_tt == 2:

  print("{c} should apy the bill")

else:

  print("{d} should pay the bill")
