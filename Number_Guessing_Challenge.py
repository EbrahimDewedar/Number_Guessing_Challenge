import random
list = []
for num in range(1,101):
    list.append(num)

random_num = random.choice(list)



def compare(guess,random):
    if guess == random:
        print(f"you get it the answer is {random_num}")
    elif guess > random:
        print("too high \n guess again:")
    elif guess < random :
        print("too low \n guess again:")
    
print("""
                                                                                                     
                                                                                _              
  __ _  __ _ _ __ ___   ___    __ _ _   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _` | | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_| | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \__, |\__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
  __/ |                        __/ |                                                            
 |___/                        |___/                                                             
""")

print("welcome to the number guessing game! \n I am thinking of a number between 1 and 100 \n choose a difficulty easy or hard\n")
type = input("choose the difficulty: type 'easy' or 'hard' :")
end = False 
guess_num = 0
if type == "easy":
    tries = 10
else:
    tries = 5
print(f"you have {tries} attemps")

while not end:
    guess_num = int(input("make a guess:"))
    compare(guess_num, random_num)
    if guess_num == random_num:
        end = True
    else:
        tries -= 1
        print(f"you have {tries} attemps remaining to guess a number ")
        if tries == 0:
            print("you lose ,you run out of tries")
            end = True

