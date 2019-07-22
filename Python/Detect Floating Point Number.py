# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
T = int(input())
for i in range(T):
    s = input()
    if re.search(r"^[+-]?[0-9]*\.[0-9]+$",s):
        print(True)
    else:
        print(False)

