# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoe_list = list(map(int,input().split()))
my_dict = dict(Counter(shoe_list))
total_sum = 0
n = int(input())
for _ in range(n):
    cust = list(map(int,input().split()))
    if cust[0] in my_dict and my_dict[cust[0]] > 0:
        total_sum+=cust[1]
        my_dict[cust[0]] -= 1
print(total_sum)


