def print_formatted(number):
    w = len(str(bin(number))[2:])

    for i in range(1, number+1):
        b = bin(int(i))[2:].rjust(w, ' ')
        o = oct(int(i))[2:].rjust(w, ' ')
        h = hex(int(i))[2:].upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print(j, o, h, b)

        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)