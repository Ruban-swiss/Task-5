
str =  input('Enter the string : ')

# Finding the maximum frequency character of the string 
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxFreqChar = max(freq, key = freq.get)

print("Entered String is ", str)
print(maxFreqChar , "is the maximum frequency character with frequency of " , freq[maxFreqChar])