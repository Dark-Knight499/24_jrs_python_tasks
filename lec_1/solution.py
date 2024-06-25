#question1

#Method 1
print("Question1")
print("")
def q1_1():
	x = int(input("Enter a number : "))
	l = len(str(x))
	print(f"Number of digits is = {l}")

#method 2
def q1_2():
	x = int(input("Enter a number : "))
	l = 0
	#0 is a single digit?
	while(x>0):
		l = l+1
		x = x//10
	print(f"Number of digits is = {l}")
q1_1()
q1_2()

#question 2
print("Question2")
print("")
#for factorial
def fact(x):
    f = 1
    for i in range(x):
        f = f * (i+1)
    return f
#input
x = input("Enter a number ")
l = len(x)
flag = 0
#for checking if it is a number
for i in range(l):
    if(x[i]>="0" and x[i]<="9"):
        continue
    else:
        flag = 1
        break
#final result
if flag == 0 :
    x = int(x)
    print(f"Factorial of {x} = {fact(x)}")
else:
    print("not a number")

#question 3
print("Question3")
print("")

Computers = {
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand = []
os = []
for i in Computers:
    brand.append(Computers[i]["brand"])
    os.append(Computers[i]["OS"])
print(brand)
print(os)
