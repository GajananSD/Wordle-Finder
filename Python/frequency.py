import matplotlib.pyplot as plt
file = open('words.txt','r')
d={}  # dictionary to find letter frequency

for word in file:
    for letter in word:
        letter=letter.rstrip('\n')
        if letter.isalpha():
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1  

d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
#print(d)


# # ----- Plotting the letter frequncy appeared in all words. -----

# names = list(d.keys())
# values = list(d.values())
# plt.bar(range(len(d)), values, tick_label=names)
# plt.title("Letter Frequency Bar Plot")
# plt.xlabel("Letters")
# plt.ylabel("Frequency")
# plt.show()


#    #----- Adding frequency data to .txt file -----

# file1 = open('LetterFrequency.txt', 'w') 
# for key, value in d.items():
#     file1.write(f"{key}: {value}\n")
# file1.close()

# file.close()
