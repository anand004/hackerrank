if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newli =sorted(set(arr))
    print(newli[-2])
