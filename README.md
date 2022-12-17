# Guess Number

I am trying to desing a guess number game.In the beginning computer choose a number between 1234 and 9876 because all numbers must be different. And you try to guess the number. For example computer chose 1234 and you guessed 1456 ,output would be +1 ,-1 because you did guess correct two number but one of them is in the correct position and the other is not.

At the end of the game , computer asks you for another game and saved your score.

- It is a game.

* Computer generated a number.
* You try to guess the computer generated number.
* Computer generate number from 1000 to 9999 but all numbers must be different.
* Number can not be 1000, 1222 ,1244,9999 etc..It means no repeating digits.
* Number can not start with 0.

I will go through the game step by step.

The game first ask your name and store it player variable.
![First name](./screen%20shots/ask_name.png)

Demonstration purposes, the generated number will be shown.

The game asks you for your guess.

![Guess](./screen%20shots/part_1.png)

There are some checks after a player enters their first guess.The game checks if user input is a digit, length is 4, has a repeating digits.

![Not digit](./screen%20shots/part_2.png)

If user enter a number that length is not 4,it will give you an error.

![Not for digit](./screen%20shots/part_3.png)

If the guess starts with 0, again it will give you length error.

![First Digit 0](./screen%20shots/part_4.png)

If there is a repeating number ,it gives an error.

![Repeating digit](./screen%20shots/part_5.png)

If gues number is passed all parts above, guess comparing parts begins.

![Guessing part](./screen%20shots/part_6.png)

![Guessing part](./screen%20shots/part_7.png)
![Guessing part](./screen%20shots/part_8.png)

If you guess the number correctly, the game asks you for another game and store your point.

![Guess correctly](./screen%20shots/part_9.png)

If your answer is y, new game starts.

![New game](./screen%20shots/part_10.png)

When you write n, game ends and display thanks for playing and game time. And also top three players... List item shows there for demostration purposes.

![End game](./screen%20shots/part_11.png)

# Desing Process

- First step: I developed class Player to store player names and scores. Initial score is 0

![Player Class](./screen%20shots/player_class.png)
