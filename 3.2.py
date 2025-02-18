f = open("user_input.txt.txt", 'w')
f.write(str(input()))

s = open('ex1.txt', 'a')
s.write(input())


f = [int(str(x)) for x in open("ex1.txt").readlines()]
print(f)

f = open("ex1.txt")
for s in f:
    print(s)

with open("ex1.txt", 'r') as file:
    s = file.read()
print(s)