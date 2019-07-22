def minion_game(string):
    stuart_score=0
    kevin_score=0
    vowel=["A","E","I","O","U"]
    for i in range(len(string)):
        if string[i] not in vowel:
            stuart_score+=(len(string)-i)
        else:
            kevin_score+=(len(string)-i)
    if stuart_score>kevin_score:
        print("Stuart",stuart_score)
    elif stuart_score<kevin_score:
        print("Kevin",kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)