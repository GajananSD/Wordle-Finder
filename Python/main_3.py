import random

guess=['candy','plume','riots'] # words choosen according to top 15 letters from letter frequency 

file = open('Text files/words.txt','r')
f = open('Text files/output_1.txt','w')
word_list = file.read().splitlines()

for inp in word_list:
    flag=0
    Green={}  # correct letters at correct position
    Orange={} # correct letters at wrong position
    Gray=[]   # Wrong letters
    attempts=0
    # choose first guess from list 'guess'
    for i in range(3):
        attempts+=1
        g = guess[i]
        if g==inp:
            flag=1
            #print("Correct guess:", g)
            #print("Attempts:", attempts)
            f.write(f"{g}: {attempts}\n")
            break
        for j in range(5):
            if g[j]==inp[j]:
                Green[g[j]]=j
            elif g[j] in inp and g[j]!=inp[j]:
                Orange.setdefault(g[j], []).append(j)
            else:
                Gray.append(g[j])


    while (flag==0):
        attempts+=1
        matching_words = []
        # print("* Green dictionary:")
        # print(Green)
        # print("* Orange dictionary:")
        # print(Orange)
        # print("* Gray:")
        # print(Gray)
        for word in word_list:
            if all(word[j] == letter for letter, j in Green.items()):
                if all(letter not in Gray for letter in word):
                    orange_conditions_met = True
                    cnt=len(Orange)
                    ind=0
                    for alph in Orange:
                        if alph in word:
                            ind+=1
                    if(ind==cnt):
                        for letter in Orange.keys():
                            positions = Orange[letter]         
                            for j in positions:
                                if word[j] == letter:
                                    orange_conditions_met = False
                                    break
                        if orange_conditions_met:
                            matching_words.append(word)
        #print(matching_words)
        guess_word = random.choice(matching_words)
        #print("Guessed word = ", guess_word)
        if guess_word == inp:
            # print("Correct guess:", guess_word)
            # print("Attempts:", attempts)
            f.write(f"{guess_word}: {attempts}\n")
            flag=1
            break
        # Update Green, Orange, and Gray based on the guess
        for j in range(5):
            if guess_word[j] == inp[j]:
                Green[guess_word[j]] = j
            elif guess_word[j] in inp and guess_word[j] != inp[j]:
                if guess_word[j] not in Orange:
                    Orange[guess_word[j]] = [j]
                else:
                    Orange[guess_word[j]].append(j)
            else:
                Gray.append(guess_word[j]) 

f.close()
file.close()
