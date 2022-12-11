number ="1234"
index =0
guess = input("Please enter your guess: ")
plus = 0
negative =0
guess_count = 1
def number_guess(guess,number):
     global plus
     global negative
     global guess_count  
     for i in range(4):

         if guess[i] in number:
            for j in range(1):
                 if guess.index(guess[i]) == number.index(guess[i]):
                     plus+=1
                 else:
                     negative +=1   
         
     if plus > 0 and negative > 0 :
            print(f"Your guess is +{plus} amd - {negative}")
     elif plus >0 and negative == 0:
            print(f"Your guess is + {plus}")
     else:
            print(f"Your gues is -{negative}")   


    
     return print(f"Your point is {guess_count}")   

plus = 0
negative =0
x = number_guess(guess,number)

