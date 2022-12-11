import random
import re
plus = 0
negative =0
guess_count = 1
class Number:
    
    @classmethod
    def number_guess(cls):
       numbers = [0]
       while numbers[0] == 0:
        numbers = random.sample(range(10),4)
       return int(''.join(map(str,numbers))) 
   
    
   

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
                     new_game = input("New game (Y/N) :")
                     if new_game.lower() == "y":
                      number = cls.number_guess()
                      print(number)
                      guess = input("Your guess: ")
                      cls.num_check(guess,number)                        
                     else:
                        print("Thank you for playing")
                  else:
                     guess_count
                     new_game = input("New game (Y/N) :")
                     if new_game.lower() == "y":
                      number = cls.number_guess()
                      print(number)
                      guess = input("Your guess: ")
                      cls.num_check(guess,number)       
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
         
                  
                  
                          



