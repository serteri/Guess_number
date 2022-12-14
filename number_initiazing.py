import random
import re
import json_update
import json
plus = 0
negative =0
guess_count = 1

data = []

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
            guess= int(input("Enter your guess(4 digits): "))
            Number.check_lenght(cls,guess)

    @classmethod
    def num_check(cls,guess,number):
      global plus
      global negative
      global guess_count
      
      if number == guess:
                  print("You win")
                  print(f"Your point is {guess_count}")
                  if guess_count == 1:
                     guess_count = 1 
         
         
                    
                  else:
                     guess_count
                    
                          
                  return guess_count
      else: 
         guess_count+=1
         for i in range(len(guess)):
                     if guess[i] in number:
                        if guess.index(guess[i]) == number.index(guess[i]):
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
         cls.num_check(guess,number)    
         return guess_count        
         
                  
                  
                          



