def swap_case(s):
    x=""
    for i in s :
        if i.islower() == True:
            x+=(i.upper())
        else:
            x+=(i.lower())
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)