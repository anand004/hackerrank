
def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    mylist = []
    i = 0
    while i<n:
        if i == 0:
            mylist.append(a)   
        elif i == 1:
            mylist.append(b)
        else:
            c = a+b
            a = b
            b = c
            mylist.append(b)
        i+=1
    return mylist
cube = lambda x: x**3


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))