if __name__ == '__main__':
    name1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name1.append([name,score])
    scores = sorted(set([s[1] for s in name1]))
    second_lowest = scores[1] 
    name1 = [s[0] for s in name1 if s[1] == second_lowest]
    name1.sort()
    for name in name1:
        print(name)
