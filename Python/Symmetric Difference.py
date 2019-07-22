# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
set1=set(map(int,input().split()))
N = int(input())
set2=set(map(int,input().split()))
a=set1.difference(set2)
b=set2.difference(set1)
c=a.union(b)
for i in sorted(c):
    print(i)
