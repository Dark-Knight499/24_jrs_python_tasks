l = []
words = []
print("Enter words and to exit -1")
while True:
    x = input("Enter a word : ")
    if x == "-1":
        break
    words.append(x)
    l.append(len(x))
max = 0
for i in range(len(l)):
    if l[i] > l[max]:
        max = i
print(words[max])
print(l[max])