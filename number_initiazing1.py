import random
from game import game

class Number:

    # def __init__(self,number,guess):
    #     self.number = number
    #     self.guess = guess
    def number_guess(self):
       numbers = [0]
       while numbers[0] == 0:
        numbers = random.sample(range(10),4)
       return int(''.join(map(str,numbers))) 
    # def all_number(self,guess):
    #     return bool(re.search(r'\d',guess))

    # def num_check(self,guess,number):
    #     if self.all_number(guess):
    #         if number == guess:
    #                             print("You win")
    #                             print(f"Your point is {guess_count}")
    #                             guess_count = 1
    #                             new_game = input("New game (Y/N) :")
    #                             if new_game.lower() == "y":
    #                                 Number().number_guess()
    #                                 print(number) 
    #                                 game()
    #                             else:
    #                                 print("Thank you for playing")
    #         else:               
    #                     while number != guess:
    #                             guess_count+=1
    #                             for i in range(len(guess)):
    #                                 if guess[i] in number:
    #                                     if guess.index(guess[i]) == number.index(guess[i]):
    #                                                 plus+=1
                                                    
    #                                     else:
    #                                                 negative+=1
    #                                 if plus > 0 and negative > 0 :
    #                                         print(f"Your guess is +{plus} amd - {negative}")
    #                                 elif plus >0 and negative == 0:
    #                                         print(f"Your guess is + {plus}")
    #                                 else:
    #                                         print(f"Your gues is -{negative}")
    #                                 plus = 0
    #                                 negative =0
    #                                 if number == guess:
    #                                     new_game = input("New game (Y/N) :")
    #                                     if new_game.lower() == "y":
    #                                         number = Number().number_guess()
    #                                         print(number)
    #                                         game()
    #                                     else:
    #                                         print("Thank you for playing")
    #                                         break 
    #                                 else:

    #                                     game()  
    #                                 print(f"Your point is {guess_count}")
    #                                 guess_count = 1
    #                                 new_game = input("New game (Y/N) :")
    #                                 if new_game.lower() == "y":
    #                                     number = Number().number_guess()
    #                                     print(number)
    #                                     game()
    #                                 else:
    #                                     print("Thank you for playing")
    #                                     break 
    #     else:
    #         print("Please enter all digit numbers: ")
    #         game()
