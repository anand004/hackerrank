# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    values=input().split()
    try:
        print(int(values[0])//int(values[1]))
    except Exception as err:
        print("Error Code:", err)
