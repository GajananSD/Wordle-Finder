import matplotlib.pyplot as plt
import numpy as np

guess={}
with open('output_1.txt', 'r') as file:
    word_list = file.read().splitlines()
    l = len(word_list)
    for i in range(l):
        num = word_list[i][7:]
        if(int(num) not in guess):
            guess[int(num)]=1
        else:
            guess[int(num)]+=1

sorted_guess = dict(sorted(guess.items()))
print(sorted_guess)
# Extract keys and values for plotting
data = list(sorted_guess.keys())
frequency = list(sorted_guess.values())

def mean(key,value):
    l=len(key)
    SUM = 0
    Total_cnt=0
    for i in range(l):
        SUM+=(key[i]*value[i])
        Total_cnt+=value[i]
    return SUM/Total_cnt

def median(key, value):
    l=[]
    l1=len(key)
    for i in range(l1):
        l.extend([key[i]]*value[i])
    l.sort()
    total_cnt=len(l)
    if total_cnt % 2 == 1:
        # If the total count is odd, median is the middle value
        median = l[total_cnt // 2]
    else:
        # If the total count is even, median is the average of the two middle values
        middle1 = l[total_cnt // 2 - 1]
        middle2 = l[total_cnt // 2]
        median = (middle1 + middle2) / 2
    return median

def mode(key,value):
    m=max(value)
    i=value.index(m)
    return key[i]

def variance(key, value):
    mu = mean(key,value)
    total_count = sum(value)
    l=len(key)
    # Calculate the variance
    SUM=0
    for i in range(l):
        SUM+=(value[i]*((key[i]-mu)**2))
    SUM = SUM / total_count
    return SUM

def SD(key,value):
    v = variance(key,value)
    return v**0.5

print("mean = ",mean(data,frequency))
print("median = ",median(data,frequency))
print("mode = ",mode(data,frequency))
print("Variance = ",variance(data,frequency))
print("Standard Deviation = ",SD(data,frequency))

plt.bar(data, frequency)
plt.xlabel('No. of guesses')
plt.ylabel('Frequency')
plt.title('Word Guess Frequencies')
# Annotate bars with frequency values
for i in range(len(data)):
    plt.text(data[i], frequency[i] + 30, str(frequency[i]), ha='center',color = 'red')
# Set x-axis ticks with a difference of 1
plt.xticks(np.arange(min(data), max(data) + 1, 1))
#plt.savefig('1.png')
plt.show()


    

