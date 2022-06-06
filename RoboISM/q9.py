print("Enter the String: ", end="")
str = input()

strLen = len(str)
for i in range(strLen):
    for j in range(strLen-1):
        if str[j] > str[j+1]:
            str = str[:j] + str[j+1] + str[j] + str[j+2:]

print("\nSorted String in Ascending:", str)