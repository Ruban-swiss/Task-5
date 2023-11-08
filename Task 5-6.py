str1 = input ("Entert he first string: ")
str2 = input ("Enter the second string: ")
result = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while (
            (i + k) < len(str1) and (j + k) < len(str2) and str1[i + k] == str2[j + k]
        ):
            k = k + 1
        result = max(result, k)

print("Length of the longest common substring is:", result)