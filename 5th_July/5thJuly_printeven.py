def input_list(l,x):
  for i in range(x):
    l.append(int(input()))

def create_even_list(l):
  even_only = []
  for i in l:
    if i%2==0:
      even_only.append(i)
  return even_only

def print_list(l):
  for i in l:
    print(i)

x = 3
l = []
print("Enter Numbers")
input_list(l,x)
print("Even Numbers")
even_list = create_even_list(l)
print_list(even_list)
