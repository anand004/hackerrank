def average(array):
    new_array=set(array)
    count=0
    sum1=0
    for i in new_array:
        sum1+=i
        count+=1
    average=sum1/count
    return average
    

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)