vowel = 0

word = input("input word : ")

for i in word:
    small = i.lower()
    if i == "a" or i == "i" or i == "u" or i == "e" or i == "o":
        vowel += 1

print("vowel = ", len(vowel))