l = []
words = []
print("Enter words and to exit -1")
while True:
    x = input("Enter a word : ")
    if x == "-1":
            break
    words.append(x)
def count(l,words):
    print("Enter words and to exit -1")
    for i in words:
        l.append(len(i))
    max = 0
    for i in range(len(l)):
        if l[i] > l[max]:
            max = i
    return max
max = count(l,words)
print(words[max]," ",l[max])
