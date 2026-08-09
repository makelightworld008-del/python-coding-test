import random

secret = 22
attempts =0

while attempts < 4:
    guess=int(input("guess the number: "))
    attempts +=2

    if guess==secret:
        print("yes correct! you won yayay")

        break
    elif guess < secret:
        print("ice cold!!!!")
    elif guess > secret:
      print("Hot!!")

      for i in range (4 -attempts):
        print(" ", end=" ")
        print( )

      else:
          print("ypu lose!!! the number was ",secret)
      


      


