def sort_std(x):
    scores = [ ]

    for std in x:
        scores.append(std[1])
    sorted_score= sorted(set(scores))
    second_lowest=sorted_score[1]
    
    name_second_lowest=[]
    for std in x:
        if std[1]==second_lowest:
            name_second_lowest.append(std[0])
    name_second_lowest = sorted(name_second_lowest)
    for name in name_second_lowest:
        print(name)
    


if __name__ == '__main__':
    x=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name,score])
        
    sort_std(x)