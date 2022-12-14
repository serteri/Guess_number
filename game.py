

from player import Player
import math
import re
import json
import random
import csv
from operator import itemgetter, attrgetter
#Create json file to score players and their scores

filename = 'scores.json'
scores ={}
name = input("Please enter your name: ")


message =''
guess_count =1
plus = 0
negative =0

class Number:
    
    @classmethod
    def number_guess(cls):
       numbers = [0]
       while numbers[0] == 0:
        numbers = random.sample(range(10),4)
       return (''.join(map(str,numbers))) 

    @classmethod   
    def check_lenght(cls,guess):
    
      if len(str(guess)) != 4:
            guess= (input("Enter your guess(4 digits): "))
            Number.check_lenght(guess)
      else:

        return True          
    @classmethod
    def num_check(cls,guess,number):
      global plus
      global negative
      global guess_count
      
      guess = str(guess)          
      if number == (guess):
                  print("You win")
                  print(f"Your point is {guess_count}")
                  if guess_count == 1:
                     guess_count = 1     
                  else:
                     guess_count

                  return guess_count
      else: 
       
        guess = str(guess)    
        guess_count+=1
        if guess.isnumeric() and len(guess) == 4:
             
            #  if Number.check_lenght(guess) and Number.check_number(guess):
            for i in range(len((guess))):
                    if (guess[i]) in number:
                                    if guess.index((guess[i])) == number.index((guess[i])):
                                        plus+=1
                                                
                                                                    
                                    else:
                                        negative += 1
                                                    
            if plus > 0 and negative > 0 :
                                print(f"Your guess is +{plus} amd - {negative}")
            elif plus >0 and negative == 0:
                                print(f"Your guess is + {plus}")
            else:
                                print(f"Your gues is -{negative}")
            plus = 0
            negative =0
            guess = input("Your guess: ")            
            Number.num_check(guess,number)    
            return guess_count        
             




def name_check(str):
    if str == '':
        name = input("Please enter your name: ")
        name_check(name)
      
player = Player(name)
computer_number = Number()
computer_number1 = str(computer_number.number_guess())
print(computer_number1)         
def json_update(filename):
    global scores
    with open("scores.json") as json_file:
            data1 = json.load(json_file)
            temp = data1
            y = {"firstname":scores["firstname"],"score":str(scores['score'])}
            temp.append(y)
    with open (filename,"w") as f:
            json.dump(data1,f)         
    
           

def all_number(guess):
        return bool(re.search(r'\d',str(guess)))
    
def csv_update(filename):
    global scores
    with open("scores.json") as csv_file:
            data1 = json.load(csv_file)
            temp = data1
            y = [{"firstname":scores["firstname"] , "score": scores["score"]}]
            temp.append(y)
            print(y)
    with open (filename,"w") as f:
            writer = csv.DictWriter(f,fieldnames=['firstname','score'])
            writer.writeheader()
            writer.writerows(y)    

# guess_correction =all_number(guess)

def game():
    global plus
    global negative
    global guess_count
    global filename
    global data
    global scores
    global guess
    global message
    global computer_number1
    
    name_check(name)
   
 # if Number.check_lenght(guess) and Number.check_number(guess):
    while True:    
            try: 
               guess= int(input("Enter your 4 digit guess: "))
            except ValueError:
                
                print("That is not a number")
                continue
            if len(str(guess)) >4 or len(str(guess)) <=3:
                print("Sorry your guess must have 4 digits: ")
            else:
                break    
    
    count= Number.num_check(str(guess),computer_number1)
    player.point = count
    player.point_show()
    scores['firstname'] = player.name
    scores['score'] = player.point
    json_update('scores.json')
    csv_update('scores.csv')  
    new_game = input("New game :(Y/N)")
    if new_game.lower() == 'y':
                    computer_number = Number()
                    computer_number1 = str(computer_number.number_guess())
                    print(computer_number1) 
                  
                    game()
    else:
                    print("Thank you for playing")    
                
                
                
                                
                        

            
    print(count)
    

            
    print(count) 
         


game()

with open("scores.json") as json_file:
    data3 = json.load(json_file)
    x = [tuple(d.values()) for d in data3]
    
    y= sorted(x, key=lambda scores: scores[1])
    print(y[0][1])
    if (len(y)< 3):
        print("Top three is not avaliable yet.")
    else:
            
     print(f"Top three is: {y[0][0]} point is {y[0][1]} ,{y[1][0]} point is {y[1][1]},{y[2][0]} point is {y[2][1]} ")