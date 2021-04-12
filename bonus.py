# Your game generates a random number and give only 10 tries for the user to guess that
# number.
# Get the user input and compare it with the random number.
# Display a hint message to the user in case the user number is smaller or bigger than the
# random number.
# If the user typed a number out of range(100), display a message that is not allowed and
# don’t count this as a try.
# if the user typed a number that has been entered before, display a hint message and
# don’t count this as a try also.
# In case the user entered a correct number within the 10 tries, display a congratulations
# message and let your
# application guess another random number with the remain number of tries.
# If the user finished his all tries, display a message to ask him if he want to play a gain or
# not.
# Next time the user open the game , he receives a welcome message tells him the number
# of games he played, how
# many times he won and how many he lost.

import json
import random

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 


print("********** Welcome to guess number game **********")
with open('data.txt') as json_file:
    data = json.load(json_file)
    game_count = int(data['game_count'])
    won_count = int(data['won_count'])
    loss_count = int(data['loss_count'])
print("game_count: " + str(game_count))
print("won_count: " + str(won_count))
print("loss_count: " + str(loss_count))
rand_num = random.randint(1, 100)
print(rand_num)
user_num = 0
ext_flag = 0
try_num = 0
score = 0
# game_count = 1
# won_count = 0  
# loss_count = 0 
user_list = []
while ext_flag == 0:
    while True:
        if try_num == 10:
            if score == 0:
                loss_count = loss_count + 1
            else:
                won_count = won_count + 1
            confirm = input("Do you want to play a gain(y/n)")
            if confirm.lower() == 'n':
                ext_flag = 1
                break
            else:
                game_count = game_count + 1
        if user_num != 0:
            user_list.append(user_num)
            print(user_list)
        user_num = inputNumber("Guess the integer number: ")
        print(user_num)
        print("try number : " , str(try_num + 1))
        if user_num > 100 :
            print("Your number is out of range")
            continue
        elif user_num < 1 :
            print("Your number is out of range") 
            continue   
        elif user_num in user_list :
            print("You have been entered this number before")
            continue
        if user_num > rand_num:
            print("Your number is bigger than our number")
            try_num = try_num + 1
        elif user_num < rand_num:
            print("Your number is smaller than our number")
            try_num = try_num + 1
        elif user_num == rand_num:
            user_list.clear()
            print("Congratulations this the right number")
            score = score + 1 
            print("score : " , str(score))
            try_num = try_num + 1
            rand_num = random.randint(1, 100)
            print(rand_num)
            break

data = {'game_count': str(game_count), 'won_count': str(won_count), 'loss_count': str(loss_count)}    
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print("Exiting the game...................")
        


 

