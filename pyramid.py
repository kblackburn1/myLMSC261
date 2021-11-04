stacks = int(input("Enter a number from 1 to 8 to determine the height of the pyramid:"))

for row in range(stacks + 1):
    for space in range(1,(stacks-row) + 1):
      print(" ",end="")
    for symbol in range(1,row + 1):
      print("#", end="")

    print()
