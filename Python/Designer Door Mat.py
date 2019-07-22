# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = list(map(int,input().split()))
m = (k-3)//2

for i in range(n//2):
    for j in range(m):
        print("-",end = "")
    for l in range(2*i+1):
        print(".|.",end="")
    for o in range(m):
        print("-",end="")
    m = m-3
    print("\r")
for i in range((k-7)//2):
    print("-",end="")
print("WELCOME",end="")
for j in range((k-7)//2):
    print("-",end="")
print("\r")
m = 3
for i in range(n//2-1,-1,-1):
    for j in range(m):
        print("-",end = "")
    for l in range(2*i+1):
        print(".|.",end="")
    for o in range(m):
        print("-",end="")
    m = m+3
    print("\r")

