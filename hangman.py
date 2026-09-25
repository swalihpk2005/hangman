import random
from movies import movies
movie=random.choice(movies).upper()
display=[]
for i in range(len(movie)):
  if movie[i]==" ":
      display.append(" ")
  else:
    display.append("_")
for letters in display:
    print(letters, end=" ")
print()
lives_remaining=10
guessed_letters=[]
while True:
        guess=input("Enter a letter: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Letter already typed!")
                print()
                continue
            else:
                guessed_letters.append(guess)
                if guess in movie:
                    print("Correct!")
                    print()
                    for index, letter in enumerate(movie):
                        if letter==guess:
                            display[index]=guess
                    for letters in display:
                        print(letters, end=" ")
                    print()
                    if "".join(display)==movie:
                        print("You won!")
                        print(f"Movie: {movie}")
                        break
                    else:
                        continue
                else:
                    print("Wrong!")
                    lives_remaining-=1
                    print(f"Lives remaining: {lives_remaining}")
                    print()
                    
                    if lives_remaining==0:
                        print("GAME OVER")
                        print(f"WORD: {movie}")
                        break
        else:
            print("Invalid input!")
            continue


