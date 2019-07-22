def merge_the_tools(string, k):
    for i in range(0,len(string),k): 
        new_string = string[i:i+k] 
        updated_string = ""
        for item in new_string: 
            if item not in updated_string: 
                updated_string += item 
        print(updated_string) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)