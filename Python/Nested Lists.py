if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        new_list = []
        name = input()
        score = float(input())
        new_list.append(name)
        new_list.append(score)
        my_list.append(new_list)
    my_list.sort(key = lambda x :(x[1],x[0]))
    lowest=my_list[0][1]
    for x in range(len(my_list)):
        if my_list[x][1]>lowest:
            lowest=my_list[x][1]
            break
    for i in range(len(my_list)):
        if lowest == my_list[i][1]:
            print(my_list[i][0])
