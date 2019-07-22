if __name__ == '__main__':
    N = int(input())
    my_li=[]
    for _ in range(N):
        command=input().split()
        if command[0]=="insert":
            my_li.insert(int(command[1]),int(command[2]))
        if command[0]=="print":
            print(my_li)
        if command[0]=="remove":
            
            my_li.remove(int(command[1]))
        if command[0]=="append":
            my_li.append(int(command[1]))
        if command[0]=="sort":
            my_li.sort()
        if command[0]=="pop":
            my_li.pop()  
        if command[0]=="reverse":
            my_li.reverse()
        


