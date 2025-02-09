if __name__ == '__main__':
    N = int(input())
    List=[];
    for i in range(N):
        x=input().split();
        if x[0] == "insert":
            List.insert(int(x[1]),int(x[2]))
        elif x[0] == "append":
            List.append(int(x[1]))
        elif x[0] == "pop":
            List.pop();
        elif x[0] == "print":
            print(List)
        elif x[0] == "remove":
            List.remove(int(x[1]))
        elif x[0] == "sort":
            List.sort();
        else:
            List.reverse();