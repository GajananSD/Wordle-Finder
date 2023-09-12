# Wordle-Finder 
[YouTube Link](https://youtu.be/bsNv2LcR04c)

##### Wordle Game   
https://www.nytimes.com/games/wordle <br>
https://wordlegame.org/

# What is Wordle? <br>
![](assets/I1.jpeg)<br>
Wordle is a daily online word game created by Josh Wardle and later sold to The New York Times Company. Every 24 hours, there is a new word of the day, and we have to figure it out in 6 tries. Since its launch, the game has become very popular. According to The New Times, over 300,000 people play the game daily. <br>

![](assets/I2.jpeg)<br>

# Problem statement: 
Find a strategy to guess the right word in Wordle in the least number of guesses.

### Methodology:

1. Downloading a database of 5-letter words.
2. Analyse these words
3. Propose a strategy based on the analysis
4. Testing our strategy.
5. Write a program to guess the correct word using our strategy.
6. Apply the program for every word in the database and take the average number of guesses.
7. Develop a program to apply an algorithm on the Wordle website to guess the word.

# Analysis

Used Python to analyse a 5760 word database of 5-letter words. This data is used to plot graphs, which helped further analyze the data.
![](assets/I3.jpeg) ![](assets/I4.png)<br>

Here, the frequency of each letter occurring in all words.

# Strategy

Based on the analysis done on our database, I developed strategies to guess the right word in the least number of guesses and within 6 guesses. First, pass fixed words as initial guesses and then the code will find the correct position, wrong positions and letters not present in the word. Based on those details, the code will decide the next guess.

***Method -1:***
<br>
Let's choose the first 5 most occurring letters: [ S, E, A, O, R]
Make one word from it: {AROSE}
So, the first initial guess will be the word ‘AROSE’ each time, and then the code will provide further guesses.

**Result:** 
After applying this algorithm for all words, the output is as follows.
![](assets/I5.jpeg) <br>
![](assets/I6.png) <br>
But we can see here that 705 words are guessed at an attempt larger than 6.

