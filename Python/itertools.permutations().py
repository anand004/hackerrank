# Enter your code here. Read input from STDIN. Print output to STDOUfro
from itertools import permutations
s,k = input().split()
out = list(permutations(s,int(k)))
out.sort()
for item in out:
    print("".join(item))
