
from player import Player
from timeit import default_timer as timer
import re
import json
import random
import csv
from sys import argv
import math
#Create json file to score players and their scores.name input creating

filename = 'scores.json'
scores ={}
name = input("Please enter your name: ")

# Initial values

guess_count =1
plus = 0
negative =0

# Number class created for number_creation, number_checking
class Number:
    # number creation for guessing
    @classmethod
    def number_guess(cls):
       numbers = [0]
       while numbers[0] == 0:
        numbers = random.sample(range(10),4)
       return (''.join(map(str,numbers))) 

# check guess length, if it is not 4 digits give an error to try again
    @classmethod   
    def check_lenght(cls,guess):
    
      if len(str(guess)) != 4:
            guess= (input("Enter your guess(4 digits): "))
            Number.check_lenght(guess)
      else:

        return True
    
    # Check all digits are different
    @classmethod
    def different_digits(cls,number):
        for d in str(number):
            if str(number).count(d) >1:
                
                return True
        return False
        
              
        
    # num_check function to check if guess is correct ot not          
    @classmethod
    def num_check(cls,guess,number):
      global plus
      global negative
      global guess_count
      
      guess = str(guess)  
      # First guess and correct guess
      
      
                  
      if number == (guess):
                  print("You win")
                  
                  if guess_count == 1:
                     guess_count = 1
                # it is not first guess          
                  else:
                     guess_count
                  print(f"Your point is {guess_count}")
                  return guess_count
      else: 
       
        guess = str(guess)    
        guess_count+=1
        
        # check after first guess if it is not correct one ,is digit,length and repating digit
        
        if guess.isnumeric() and len(guess) == 4 and  not Number.different_digits(int(guess)):
        
             
            #  if Number.check_lenght(guess) and Number.check_number(guess):
            for i in range(len((guess))):
                    if (guess[i]) in number:
                                    if guess.index((guess[i])) == number.index((guess[i])):
                                        plus+=1
                                                
                                                                    
                                    else:
                                        negative += 1
            # display output                                        
            if plus > 0 and negative > 0 :
                                print(f"Your guess is +{plus} and - {negative}")
            elif plus >0 and negative == 0:
                                print(f"Your guess is + {plus}")
                              
            else:
                                print(f"Your guess is -{negative}")
            plus = 0
            negative =0
            guess = input("Your guess: ")            
            Number.num_check(guess,number)    
            return guess_count
        # if it is not a valid guess        
        else:
             guess= (input("Wrong format.Pleae enter your 4 digit guess: "))
             Number.num_check(guess,number)    
# username checking

def name_check(str):
    global name
    if str == '':
        name=input("Name can not be empty: ")
        name_check(name)
    return name   
 #player creating     


#Number generating
computer_number = Number()
computer_number1 = str(computer_number.number_guess())
print(computer_number1)
# update json file         
def json_update(filename):
    global scores
    with open("./src/scores.json") as json_file:
            data1 = json.load(json_file)
            temp = data1
            y = {"firstname":scores["firstname"],"score":str(scores['score'])}
            temp.append(y)
    with open (filename,"w") as f:
            json.dump(data1,f)      
    
def all_number(guess):
        
        return bool(re.search(r'\d',str(guess)))
 # csv file update   
def csv_update(filename):
    global scores
    with open("./src/scores.json") as csv_file:
            data1 = json.load(csv_file)
            temp = data1
            y = [{"firstname":scores["firstname"] , "score": scores["score"]}]
            temp.append(y)
            
    with open (filename,"a") as f:
            writer = csv.DictWriter(f,fieldnames=['firstname','score'])
            writer.writeheader()
            writer.writerows(y)
            
# game coding                
def game():
    global plus
    global negative
    global guess_count
    global filename
    global name
    global scores
    global guess
    
    global computer_number1
    
    name = name_check(name)
    
    player = Player(name)
    while True:    
            try: 
               guess= int(input("Enter your 4 digit guess: "))
            except ValueError:
                
                print("That is not a number")
                continue
            if len(str(guess)) !=4:
                print("Sorry your guess must have 4 digits: ")
            elif Number.different_digits(guess):
                print("All digits must be different: ")
        
            else:
                break
    
            
    
    count= Number.num_check(str(guess),computer_number1)
    
    player.point = count
    player.point_show()
    scores['firstname'] = player.name
    scores['score'] = player.point
    json_update('./src/scores.json')
    csv_update('./src/scores.csv')  
    new_game = input("New game :(Y/N)")
    if new_game.lower() == 'y' or new_game == "Y":
                    computer_number = Number()
                    computer_number1 = str(computer_number.number_guess())
                    
                    game()
    else:
                    print("Thank you for playing")    
                
# game play and calculate timing                         
start =timer()
game()

end =timer()

print(f"Game took {math.trunc(end-start)} seconds to finish.")
#Top three sorted and printing
with open("./src/scores.json") as json_file:
    data3 = json.load(json_file)
    # x = [tuple(d.values()) for d in data3]
    
    # y= sorted(x, key=lambda scores: scores[1])
    x =sorted(data3,key=lambda product:product['score'])

   
    if (len(x)< 3):
        print("Top three is not avaliable yet.")
    else:
            
     print(f"Top three is: {x[0]['firstname']} point is {x[0]['score']} ,{x[1]['firstname']} point is {x[1]['score']},{x[2]['firstname']} point is {x[2]['score']} ")