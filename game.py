
from number_initiazing import Number
import copy
from player import Player
import math
import re
import json

#Create json file to score players and their scores

filename = 'scores.json'



name = input("Please enter your name: ")
player = Player(name)
computer_number = Number()
computer_number1 = str(computer_number.number_guess())
print(computer_number1) 
guess= input("Enter your guess(4 digits): ")

guess_count =1
data = []
scores ={}

def json_update(filename):
    with open("scores.json") as json_file:
            data1 = json.load(json_file)
            temp = data1
            y = {"firstname":scores["firstname"] , "score": scores["score"]}
            temp.append(y)
    with open (filename,"w") as f:
            json.dump(data1,f)

def all_number(guess):
        return bool(re.search(r'\d',guess))

guess_correction =all_number(guess)
def game():
    global plus
    global negative
    global guess_count
    global filename
    global data
    global scores
   
    if guess_correction:
         count= Number.num_check(guess,computer_number1)
         print(count)
         player.point = count
         player.point_show()
         
         scores['firstname'] = player.name
         scores['score'] = player.point
         json_update('scores.json')  


        
game()
