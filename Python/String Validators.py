if __name__ == '__main__':
    s = input()
    alpha_num=False
    alpa=False
    digi=False
    lowercase=False
    uppercase=False
    for i in s:
        if i.isalnum():
            alpha_num=True
        if i.isalpha():
            alpa=True
        if i.isdigit():
            digi=True
        if i.islower():
            lowercase=True
        if i.isupper():
            uppercase=True
    print(alpha_num)
    print(alpa)
    print(digi)
    print(lowercase)
    print(uppercase)
