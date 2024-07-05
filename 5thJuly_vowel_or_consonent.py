s = input("Enter a string ")
l = ["a","A","E","e","I","i","o","O","U","u"]
def isvowel(s,l):
    count = 0
    for i in range(len(s)):
        if s[i] in l:
            count = count + 1
    return count
def isalpha(l):
    count = 0
    for i in range(len(s)):
        if s[i]<"a" or s[i]>"z":
            if s[i]<"A" or s[i]>"Z":
                count = count + 1
    return count
vowel = isvowel(s,l)
notalpha = isalpha(s)
conso = len(s) - vowel - notalpha
print("Vowels = ",vowel)
print("Conso = ",conso)
print()